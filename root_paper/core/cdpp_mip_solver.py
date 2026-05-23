"""
cdpp_mip_solver.py — CDPP solvers ported to python-mip (HiGHS / CBC backend).

Drop-in replacement for the gurobipy-based CDPPSolver in srv_reimplement_0.py.
Supports both HiGHS and CBC via python-mip's unified API.

Usage:
    solver = CDPPMipSolver(instance, backend="highs")  # or "cbc"
    result = solver.solve_cdpp_mip(q=3, parking_time=5.0)
"""

from __future__ import annotations

import itertools
import time
from dataclasses import dataclass, field
from typing import Any, Iterable, Literal

from mip import Model, xsum, BINARY, INTEGER, CONTINUOUS, OptimizationStatus, CBC, HIGHS


# Re-use data structures from srv_reimplement_0 if available, else define standalone
try:
    from root_paper.core.srv_reimplement import CDPPInstance, Location, ServiceSetSelection, SolverResult, SRVLogger
except ImportError:
    @dataclass(frozen=True)
    class Location:
        original_idx: int
        lat: float
        lon: float

    @dataclass(frozen=True)
    class CDPPInstance:
        name: str
        locations: list[Location]
        walking: list[list[float]]
        driving: list[list[float]]

        @property
        def node_count(self) -> int:
            return len(self.locations)

        @property
        def customer_count(self) -> int:
            return max(0, self.node_count - 1)

        @property
        def depot(self) -> int:
            return 0

        @property
        def customers(self) -> list[int]:
            return list(range(1, self.node_count))

        @property
        def parking_nodes(self) -> list[int]:
            return self.customers

    @dataclass(frozen=True)
    class ServiceSetSelection:
        parking: int
        customers: tuple[int, ...]
        walking_cost: float

    @dataclass
    class SolverResult:
        name: str
        status: str
        objective: float | None
        runtime: float
        variables: int
        constraints: int
        route: list[int] = field(default_factory=list)
        open_parking: list[int] = field(default_factory=list)
        service_sets: list[ServiceSetSelection] = field(default_factory=list)
        driving_time: float = 0.0
        parking_time: float = 0.0
        walking_time: float = 0.0
        loading_time: float = 0.0
        weighted_value: float | None = None

        def summary(self) -> str:
            return (
                f"{self.name}: status={self.status}, objective={self.objective}, "
                f"runtime={self.runtime:.3f}s, open={self.open_parking}, route={self.route}, "
                f"driving={self.driving_time:.3f}, parking={self.parking_time:.3f}, "
                f"walking={self.walking_time:.3f}, loading={self.loading_time:.3f}, "
                f"service_sets={[(s.parking, s.customers) for s in self.service_sets]}"
            )

    class SRVLogger:
        def print(self, msg, level=None):
            print(msg)


BACKEND_MAP = {"highs": HIGHS, "cbc": CBC}


class CDPPMipSolver:
    """CDPP solver using python-mip with selectable HiGHS/CBC backend."""

    def __init__(self, instance: CDPPInstance, backend: str = "highs") -> None:
        self.instance = instance
        self.backend = BACKEND_MAP.get(backend.lower(), HIGHS)
        self.backend_name = backend.lower()

    def _parking_time_value(self, parking_time: float | dict[int, float], node: int) -> float:
        if node == self.instance.depot:
            return 0.0
        if isinstance(parking_time, dict):
            return float(parking_time.get(node, 0.0))
        return float(parking_time)

    def shortest_walking_loop(self, parking: int, customers: tuple[int, ...]) -> float:
        if not customers:
            return 0.0
        best = float("inf")
        for perm in itertools.permutations(customers):
            path = (parking, *perm, parking)
            cost = sum(self.instance.walking[path[i]][path[i + 1]] for i in range(len(path) - 1))
            if cost < best:
                best = cost
        return best

    def generate_service_sets(
        self,
        q: int,
        parking_nodes: Iterable[int] | None = None,
        customers: Iterable[int] | None = None,
        contiguous_order: list[int] | None = None,
    ) -> list[ServiceSetSelection]:
        pnodes = list(parking_nodes if parking_nodes is not None else self.instance.parking_nodes)
        cust_list = list(customers if customers is not None else self.instance.customers)
        service_sets: list[ServiceSetSelection] = []

        if contiguous_order is not None:
            order = list(contiguous_order)
            for start in range(len(order)):
                for length in range(1, min(q, len(order) - start) + 1):
                    subset = tuple(order[start: start + length])
                    for parking in pnodes:
                        service_sets.append(
                            ServiceSetSelection(parking=parking, customers=subset,
                                                walking_cost=self.shortest_walking_loop(parking, subset))
                        )
            return service_sets

        for parking in pnodes:
            for size in range(1, min(q, len(cust_list)) + 1):
                for subset in itertools.combinations(cust_list, size):
                    service_sets.append(
                        ServiceSetSelection(parking=parking, customers=tuple(subset),
                                            walking_cost=self.shortest_walking_loop(parking, tuple(subset)))
                    )
        return service_sets

    def _extract_route(self, x_vars: dict, nodes: list[int], start: int = 0) -> list[int]:
        succ = {}
        for i in nodes:
            for j in nodes:
                if i != j and (i, j) in x_vars and x_vars[(i, j)].x > 0.5:
                    succ[i] = j
        route = []
        cur = start if start in succ else (next(iter(succ)) if succ else start)
        visited = set()
        while cur not in visited and cur in succ:
            route.append(cur)
            visited.add(cur)
            cur = succ[cur]
        if cur == start:
            route.append(start)
        return route

    def _route_driving_time(self, route: list[int]) -> float:
        if len(route) < 2:
            return 0.0
        return sum(self.instance.driving[route[i]][route[i + 1]] for i in range(len(route) - 1))

    # -------------------------------------------------------------------------
    # 1. CDPP MIP exact — Paper Eq. (1)-(12)
    # -------------------------------------------------------------------------

    def solve_cdpp_mip(
        self,
        q: int = 3,
        parking_time: float | dict[int, float] = 5.0,
        loading_time_per_package: float = 2.1,
        time_limit: float | None = None,
        candidate_sets: list[ServiceSetSelection] | None = None,
        name: str = "CDPP_MIP",
    ) -> SolverResult:
        inst = self.instance
        customers = inst.customers
        parking_nodes = inst.parking_nodes
        all_nodes = [inst.depot] + parking_nodes
        n_customers = len(customers)

        service_sets = candidate_sets if candidate_sets is not None else self.generate_service_sets(q=q)

        t0 = time.perf_counter()
        m = Model(name, solver_name=self.backend)
        m.verbose = 0
        if time_limit is not None:
            m.max_seconds = time_limit

        arcs = [(i, k) for i in all_nodes for k in all_nodes if i != k]
        flow_arcs = [(i, k) for i in all_nodes for k in parking_nodes if i != k]

        # Decision variables
        x = {}
        for i, k in arcs:
            x[(i, k)] = m.add_var(var_type=BINARY, name=f"x_{i}_{k}")

        z = [m.add_var(var_type=BINARY, name=f"z_{j}") for j in range(len(service_sets))]

        v = {}
        for i, k in flow_arcs:
            v[(i, k)] = m.add_var(var_type=INTEGER, lb=0, ub=n_customers, name=f"v_{i}_{k}")

        # Objective: Eq. (1)
        m.objective = (
            xsum((inst.driving[i][k] + self._parking_time_value(parking_time, k)) * x[(i, k)] for i, k in arcs)
            + xsum((ss.walking_cost + loading_time_per_package * len(ss.customers)) * z[j]
                   for j, ss in enumerate(service_sets))
        )

        # (2)+(3) vehicle leaves/returns depot
        m += xsum(x[(inst.depot, i)] for i in parking_nodes) == 1
        m += xsum(x[(i, inst.depot)] for i in parking_nodes) == 1

        # (4) each customer served once
        for c in customers:
            m += xsum(z[j] for j, ss in enumerate(service_sets) if c in ss.customers) == 1

        # (5) flow conservation at parking nodes
        for i in parking_nodes:
            m += (xsum(x[(k, i)] for k in all_nodes if k != i)
                  == xsum(x[(i, k)] for k in all_nodes if k != i))

        # (6) service set requires vehicle visit
        for j, ss in enumerate(service_sets):
            i = ss.parking
            m += z[j] <= xsum(x[(k, i)] for k in all_nodes if k != i)

        # (7) n packages leave depot
        m += xsum(v[(inst.depot, i)] for i in parking_nodes) == n_customers

        # (8) flow link
        for i, k in flow_arcs:
            m += v[(i, k)] <= n_customers * x[(i, k)]

        # (9) flow balance
        for i in parking_nodes:
            delivered = xsum(len(ss.customers) * z[j] for j, ss in enumerate(service_sets) if ss.parking == i)
            inbound = xsum(v[(k, i)] for k in all_nodes if k != i)
            outbound = xsum(v[(i, k)] for k in parking_nodes if k != i)
            m += inbound - outbound == delivered

        m.optimize()
        elapsed = time.perf_counter() - t0
        has_sol = m.num_solutions > 0

        selected_sets = [ss for j, ss in enumerate(service_sets) if has_sol and z[j].x > 0.5]
        open_parking = sorted({ss.parking for ss in selected_sets})
        route = self._extract_route(x, all_nodes, start=inst.depot) if has_sol else []

        return SolverResult(
            name=f"{name}_{self.backend_name}",
            status=m.status.name,
            objective=m.objective_value if has_sol else None,
            runtime=elapsed,
            variables=m.num_cols,
            constraints=m.num_rows,
            route=route,
            open_parking=open_parking,
            service_sets=selected_sets,
            driving_time=self._route_driving_time(route),
            parking_time=sum(self._parking_time_value(parking_time, p) for p in open_parking),
            walking_time=sum(ss.walking_cost for ss in selected_sets),
            loading_time=loading_time_per_package * sum(len(ss.customers) for ss in selected_sets),
        )

    # -------------------------------------------------------------------------
    # 2. PA-R (Parking Assignment and Routing) — Section 3.3.1
    # -------------------------------------------------------------------------

    def solve_pa_r(self, parking_time: float = 5.0) -> SolverResult:
        inst = self.instance
        customers = inst.customers
        parking_nodes = inst.parking_nodes

        t0 = time.perf_counter()
        m = Model("PA_R", solver_name=self.backend)
        m.verbose = 0

        p_open = {i: m.add_var(var_type=BINARY, name=f"p_{i}") for i in parking_nodes}
        a = {(i, k): m.add_var(var_type=BINARY, name=f"a_{i}_{k}")
             for i in parking_nodes for k in customers}

        m.objective = (
            parking_time * xsum(p_open[i] for i in parking_nodes)
            + xsum(inst.walking[i][k] * a[(i, k)] for i in parking_nodes for k in customers)
        )

        for k in customers:
            m += xsum(a[(i, k)] for i in parking_nodes) == 1
        for i in parking_nodes:
            for k in customers:
                m += a[(i, k)] <= p_open[i]
        for i in parking_nodes:
            m += p_open[i] <= xsum(a[(i, k)] for k in customers)

        m.optimize()
        elapsed = time.perf_counter() - t0
        has_sol = m.num_solutions > 0

        assignment: dict[int, list[int]] = {}
        service_sets = []
        if has_sol:
            for i in parking_nodes:
                if p_open[i].x > 0.5:
                    assignment[i] = [k for k in customers if a[(i, k)].x > 0.5]
                    service_sets.append(ServiceSetSelection(i, tuple(assignment[i]), 0.0))

        return SolverResult(
            name=f"PA_R_{self.backend_name}",
            status=m.status.name,
            objective=m.objective_value if has_sol else None,
            runtime=elapsed,
            variables=m.num_cols,
            constraints=m.num_rows,
            open_parking=sorted(assignment),
            service_sets=service_sets,
        )

    # -------------------------------------------------------------------------
    # 3. TSP over nodes — MTZ formulation
    # -------------------------------------------------------------------------

    def solve_tsp_over_nodes(self, nodes: list[int], name: str = "TSP") -> SolverResult:
        inst = self.instance
        nodes = list(dict.fromkeys(nodes))
        if inst.depot not in nodes:
            nodes = [inst.depot] + nodes

        if len(nodes) <= 1:
            return SolverResult(name=name, status="TRIVIAL", objective=0.0,
                                runtime=0.0, variables=0, constraints=0, route=nodes)

        t0 = time.perf_counter()
        m = Model(name, solver_name=self.backend)
        m.verbose = 0

        x = {}
        for i in nodes:
            for j in nodes:
                if i != j:
                    x[(i, j)] = m.add_var(var_type=BINARY, name=f"x_{i}_{j}")

        u = {i: m.add_var(var_type=CONTINUOUS, lb=0, ub=len(nodes) - 1, name=f"u_{i}") for i in nodes}

        m.objective = xsum(inst.driving[i][j] * x[(i, j)] for i in nodes for j in nodes if i != j)

        for i in nodes:
            m += xsum(x[(i, j)] for j in nodes if j != i) == 1
            m += xsum(x[(j, i)] for j in nodes if j != i) == 1

        root = inst.depot
        m += u[root] == 0
        for i in nodes:
            if i != root:
                m += u[i] >= 1
        for i in nodes:
            for j in nodes:
                if i != j and i != root and j != root:
                    m += u[i] - u[j] + len(nodes) * x[(i, j)] <= len(nodes) - 1

        m.optimize()
        elapsed = time.perf_counter() - t0
        has_sol = m.num_solutions > 0
        route = self._extract_route(x, nodes, start=root) if has_sol else []

        return SolverResult(
            name=f"{name}_{self.backend_name}",
            status=m.status.name,
            objective=m.objective_value if has_sol else None,
            runtime=elapsed,
            variables=m.num_cols,
            constraints=m.num_rows,
            route=route,
            driving_time=self._route_driving_time(route),
        )

    # -------------------------------------------------------------------------
    # 4. SSA (Service Set Assignment) — Section 3.3.2
    # -------------------------------------------------------------------------

    def solve_ssa_for_groups(self, groups: dict[int, list[int]], q: int = 3) -> SolverResult:
        selected: list[ServiceSetSelection] = []
        total_runtime = 0.0
        total_vars = 0
        total_constraints = 0
        total_obj = 0.0

        for parking, customers in groups.items():
            if not customers:
                continue
            candidates = self.generate_service_sets(q=q, parking_nodes=[parking], customers=customers)

            t0 = time.perf_counter()
            m = Model(f"SSA_{parking}", solver_name=self.backend)
            m.verbose = 0
            y = [m.add_var(var_type=BINARY, name=f"y_{j}") for j in range(len(candidates))]
            m.objective = xsum(candidates[j].walking_cost * y[j] for j in range(len(candidates)))

            for c in customers:
                m += xsum(y[j] for j, ss in enumerate(candidates) if c in ss.customers) == 1

            m.optimize()
            elapsed = time.perf_counter() - t0
            total_runtime += elapsed
            total_vars += m.num_cols
            total_constraints += m.num_rows
            if m.num_solutions > 0:
                total_obj += m.objective_value
                selected.extend(candidates[j] for j in range(len(candidates)) if y[j].x > 0.5)

        return SolverResult(
            name=f"SSA_{self.backend_name}",
            status="OK",
            objective=total_obj,
            runtime=total_runtime,
            variables=total_vars,
            constraints=total_constraints,
            open_parking=sorted(groups),
            service_sets=selected,
            walking_time=sum(ss.walking_cost for ss in selected),
        )

    # -------------------------------------------------------------------------
    # 5. Two-echelon heuristic — PA-R + TSP + SSA
    # -------------------------------------------------------------------------

    def solve_two_echelon_heuristic(
        self, q: int = 3, parking_time: float = 5.0, loading_time_per_package: float = 2.1,
    ) -> SolverResult:
        pa = self.solve_pa_r(parking_time=parking_time)
        groups = {ss.parking: list(ss.customers) for ss in pa.service_sets}
        tsp = self.solve_tsp_over_nodes(pa.open_parking, name="TSP_parking")
        ssa = self.solve_ssa_for_groups(groups, q=q)

        objective = (
            (tsp.objective or 0.0)
            + parking_time * len(pa.open_parking)
            + (ssa.objective or 0.0)
            + loading_time_per_package * self.instance.customer_count
        )
        return SolverResult(
            name=f"TwoEchelon_{self.backend_name}",
            status="OK",
            objective=objective,
            runtime=pa.runtime + tsp.runtime + ssa.runtime,
            variables=pa.variables + tsp.variables + ssa.variables,
            constraints=pa.constraints + tsp.constraints + ssa.constraints,
            route=tsp.route,
            open_parking=pa.open_parking,
            service_sets=ssa.service_sets,
            driving_time=tsp.driving_time,
            parking_time=parking_time * len(pa.open_parking),
            walking_time=ssa.walking_time,
            loading_time=loading_time_per_package * self.instance.customer_count,
        )

    # -------------------------------------------------------------------------
    # 6. Modified TSP benchmark — Section 5.2.1
    # -------------------------------------------------------------------------

    def solve_modified_tsp(
        self, q: int = 3, parking_time: float = 5.0,
        loading_time_per_package: float = 2.1, time_limit: float | None = None,
    ) -> SolverResult:
        tsp_all = self.solve_tsp_over_nodes(self.instance.customers, name="TSP_all")
        order = [node for node in tsp_all.route if node != self.instance.depot]
        if not order:
            order = self.instance.customers
        restricted_sets = self.generate_service_sets(q=q, contiguous_order=order)
        return self.solve_cdpp_mip(
            q=q, parking_time=parking_time, loading_time_per_package=loading_time_per_package,
            time_limit=time_limit, candidate_sets=restricted_sets, name="ModifiedTSP",
        )

    # -------------------------------------------------------------------------
    # 7. Relaxed M-S benchmark — Section 5.2.2
    # -------------------------------------------------------------------------

    def solve_relaxed_ms(
        self, alpha: float = 0.6, q: int = 3, parking_time: float = 5.0,
        loading_time_per_package: float = 2.1, time_limit: float | None = None,
    ) -> SolverResult:
        inst = self.instance
        service_sets = self.generate_service_sets(q=q)
        customers = inst.customers
        parking_nodes = inst.parking_nodes
        all_nodes = [inst.depot] + parking_nodes
        n_customers = len(customers)

        t0 = time.perf_counter()
        m = Model(f"Relaxed_MS_{alpha}", solver_name=self.backend)
        m.verbose = 0
        if time_limit is not None:
            m.max_seconds = time_limit

        arcs = [(i, k) for i in all_nodes for k in all_nodes if i != k]
        flow_arcs = [(i, k) for i in all_nodes for k in parking_nodes if i != k]

        x = {(i, k): m.add_var(var_type=BINARY, name=f"x_{i}_{k}") for i, k in arcs}
        z = [m.add_var(var_type=BINARY, name=f"z_{j}") for j in range(len(service_sets))]
        v = {(i, k): m.add_var(var_type=INTEGER, lb=0, ub=n_customers, name=f"v_{i}_{k}") for i, k in flow_arcs}

        # Weighted objective: alpha * driving + (1-alpha) * walking + loading
        m.objective = (
            alpha * xsum(inst.driving[i][k] * x[(i, k)] for i, k in arcs)
            + (1 - alpha) * xsum(service_sets[j].walking_cost * z[j] for j in range(len(service_sets)))
            + loading_time_per_package * n_customers
        )

        # Same constraints as CDPP
        m += xsum(x[(inst.depot, i)] for i in parking_nodes) == 1
        m += xsum(x[(i, inst.depot)] for i in parking_nodes) == 1
        for c in customers:
            m += xsum(z[j] for j, ss in enumerate(service_sets) if c in ss.customers) == 1
        for i in parking_nodes:
            m += xsum(x[(k, i)] for k in all_nodes if k != i) == xsum(x[(i, k)] for k in all_nodes if k != i)
        for j, ss in enumerate(service_sets):
            m += z[j] <= xsum(x[(k, ss.parking)] for k in all_nodes if k != ss.parking)
        m += xsum(v[(inst.depot, i)] for i in parking_nodes) == n_customers
        for i, k in flow_arcs:
            m += v[(i, k)] <= n_customers * x[(i, k)]
        for i in parking_nodes:
            delivered = xsum(len(ss.customers) * z[j] for j, ss in enumerate(service_sets) if ss.parking == i)
            inbound = xsum(v[(k, i)] for k in all_nodes if k != i)
            outbound = xsum(v[(i, k)] for k in parking_nodes if k != i)
            m += inbound - outbound == delivered

        m.optimize()
        elapsed = time.perf_counter() - t0
        has_sol = m.num_solutions > 0

        selected_sets = [ss for j, ss in enumerate(service_sets) if has_sol and z[j].x > 0.5]
        open_parking = sorted({ss.parking for ss in selected_sets})
        route = self._extract_route(x, all_nodes, start=inst.depot) if has_sol else []

        driving_total = self._route_driving_time(route)
        walking_total = sum(ss.walking_cost for ss in selected_sets)
        parking_total = parking_time * len(open_parking)
        loading_total = loading_time_per_package * n_customers

        return SolverResult(
            name=f"RelaxedMS_a{alpha}_{self.backend_name}",
            status=m.status.name,
            objective=driving_total + walking_total + parking_total + loading_total if has_sol else None,
            runtime=elapsed,
            variables=m.num_cols,
            constraints=m.num_rows,
            route=route,
            open_parking=open_parking,
            service_sets=selected_sets,
            driving_time=driving_total,
            parking_time=parking_total,
            walking_time=walking_total,
            loading_time=loading_total,
            weighted_value=m.objective_value if has_sol else None,
        )
