from __future__ import annotations

"""
srv_reimplement_final.py

A compact reproduction scaffold for the paper:
"Does parking matter? The impact of parking time on last-mile delivery optimization"

The file is designed to run SMALL sampled instances first, then scale the same
pipeline to the Illinois dataset experiments.

Implemented solvers:
1. CDPP MIP-like exact model with service-set variables and vehicle route variables.
2. Modified TSP benchmark: TSP order first, then restricted service sets.
3. Relaxed M-S benchmark: weighted driving/walking objective, parking added after.
4. Two-echelon heuristic: PA-R + TSP over opened parking + SSA.

Notes:
- The paper uses depot 0 and customers C. This implementation explicitly reserves
  local node 0 as depot. Sampled customers are local nodes 1..n.
- For sample experiments, choose a small num_customers, e.g. 6-10.
- For paper-scale runs, increase num_customers and instance_count, but expect the
  CDPP exact model to become large quickly because service sets grow combinatorially.
"""

import ast
import csv
import itertools
import logging
import math
import os
import random
import threading
import time
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any, Iterable, Literal

try:
    import gurobipy as gp  # type: ignore
    from gurobipy import GRB  # type: ignore
except ImportError:  # pragma: no cover
    gp = None
    GRB = None

try:
    import psutil
except ImportError:  # pragma: no cover
    psutil = None


# =============================================================================
# Logging
# =============================================================================


class SRVLogger:
    _instance = None

    class Level(IntEnum):
        DEBUG = logging.DEBUG
        INFO = logging.INFO
        WARNING = logging.WARNING
        ERROR = logging.ERROR
        CRITICAL = logging.CRITICAL

    @dataclass
    class Args:
        file: str | Path | None = None
        level: int = logging.INFO
        memory: bool = False
        memory_interval_ms: int = 10000

        def __post_init__(self) -> None:
            if isinstance(self.file, str):
                self.file = Path(self.file)

    def __new__(cls, *args: Any, **kwargs: Any) -> "SRVLogger":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, args: Args | None = None) -> None:
        if self._initialized:
            return

        self.args = args if args is not None else self.Args()
        logging.basicConfig(
            level=self.args.level,
            filename=self.args.file,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True,
        )
        self.logger = logging.getLogger("SRVLogger")
        self.mem = 0.0
        self._stop_memory_logger = threading.Event()
        self._memory_thread: threading.Thread | None = None
        self._initialized = True

        if self.args.memory:
            self._memory_thread = threading.Thread(
                target=self._memory_logging_loop,
                daemon=True,
            )
            self._memory_thread.start()

    def print(self, message: str, level: int | None = None) -> None:
        self.logger.log(level if level is not None else self.args.level, message)
        print(message)

    def _memory_logging_loop(self) -> None:
        if psutil is None:
            self.print("psutil is not installed; memory logging is disabled", self.Level.WARNING)
            return
        process = psutil.Process(os.getpid())
        while not self._stop_memory_logger.is_set():
            current_mem = process.memory_info().rss / (1024 * 1024)
            if current_mem != self.mem:
                self.print(f"Memory usage: {current_mem:.2f} MB ({current_mem - self.mem:+.2f} MB)")
                self.mem = current_mem
            self._stop_memory_logger.wait(max(self.args.memory_interval_ms, 1) / 1000)

    def stop_memory_logging(self) -> None:
        self._stop_memory_logger.set()
        if self._memory_thread and self._memory_thread.is_alive():
            self._memory_thread.join(timeout=1)


# =============================================================================
# Data model and Illinois loader
# =============================================================================


@dataclass(frozen=True)
class Location:
    original_idx: int
    lat: float
    lon: float


@dataclass(frozen=True)
class CDPPInstance:
    """Local node 0 is depot; local nodes 1..n are customers and parking candidates."""

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
        # Paper experimental assumption: Pi = C union {0}, but parking is only needed at customers.
        return self.customers


class IllinoisDataLoader:
    def __init__(self, base_dir: str | Path | None = None) -> None:
        self.logger = SRVLogger()
        self.base_dir = Path(base_dir) if base_dir is not None else self._default_base_dir()

    @staticmethod
    def _default_base_dir() -> Path:
        return (
            Path(__file__).resolve().parents[2]
            / "data/illinois_cdpp_instances/data/Urban_Rural_Instances"
        )

    def paths_for_county_instance(self, county_prefix: str, instance_id: int) -> tuple[Path, Path, Path]:
        stem = f"{county_prefix}_{instance_id}"
        return (
            self.base_dir / f"{stem}.csv",
            self.base_dir / f"{stem}_Walking.csv",
            self.base_dir / f"{stem}_Driving.csv",
        )

    @staticmethod
    def _parse_pair_key(raw_key: str) -> tuple[int, int]:
        parsed = ast.literal_eval(raw_key)
        if not isinstance(parsed, tuple) or len(parsed) != 2:
            raise ValueError(f"Invalid pair key: {raw_key!r}")
        return int(parsed[0]), int(parsed[1])

    @staticmethod
    def _as_float(value: str | None, default: float = 0.0) -> float:
        if value is None or value == "":
            return default
        return float(value)

    def _load_locations(self, path: str | Path) -> list[Location]:
        path = Path(path)
        result: list[Location] = []
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader):
                result.append(Location(original_idx=idx, lat=float(row["lat"]), lon=float(row["lon"])))
        return result

    def _load_time_entries(self, path: str | Path) -> dict[int, dict[int, float]]:
        path = Path(path)
        raw: dict[int, dict[int, float]] = {}
        max_key = -1
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                i, j = self._parse_pair_key(row.get("key", ""))
                max_key = max(max_key, i, j)
                raw.setdefault(i, {})[j] = self._as_float(row.get("Time"))
        return raw

    @staticmethod
    def _maybe_shift_to_zero_based(
        entries: dict[int, dict[int, float]],
        location_count: int,
    ) -> dict[int, dict[int, float]]:
        if not entries:
            return entries
        max_key = max(max(entries), max(max(v) if v else -1 for v in entries.values()))
        min_key = min(min(entries), min(min(v) if v else math.inf for v in entries.values()))
        # Many CSVs encode keys as 1..n. Shift to 0..n-1 when detected.
        if min_key >= 1 and max_key >= location_count:
            shifted: dict[int, dict[int, float]] = {}
            for i, row in entries.items():
                shifted[i - 1] = {j - 1: value for j, value in row.items()}
            return shifted
        return entries

    @staticmethod
    def _build_matrix(entries: dict[int, dict[int, float]], indexes: list[int]) -> list[list[float]]:
        matrix: list[list[float]] = []
        for i in indexes:
            row: list[float] = []
            for j in indexes:
                row.append(0.0 if i == j else float(entries.get(i, {}).get(j, float("inf"))))
            matrix.append(row)
        return matrix

    def load_instance_from_files(
        self,
        location_path: str | Path,
        walking_path: str | Path,
        driving_path: str | Path,
        num_customers: int = 8,
        seed: int | None = 42,
        depot_policy: Literal["first_sampled", "first_file"] = "first_sampled",
        name: str = "sample",
    ) -> CDPPInstance:
        locations_all = self._load_locations(location_path)
        walking_raw = self._maybe_shift_to_zero_based(self._load_time_entries(walking_path), len(locations_all))
        driving_raw = self._maybe_shift_to_zero_based(self._load_time_entries(driving_path), len(locations_all))

        if len(locations_all) < 2:
            raise ValueError("Need at least one depot and one customer")

        rng = random.Random(seed)
        if depot_policy == "first_file":
            depot_original = 0
            available_customers = [i for i in range(len(locations_all)) if i != depot_original]
            sampled_customers = sorted(rng.sample(available_customers, min(num_customers, len(available_customers))))
            sampled_indexes = [depot_original] + sampled_customers
        else:
            needed = min(num_customers + 1, len(locations_all))
            sampled_indexes = sorted(rng.sample(list(range(len(locations_all))), needed))
            # local 0 becomes the first sampled index and is treated as the depot.

        local_locations = [locations_all[i] for i in sampled_indexes]
        walking = self._build_matrix(walking_raw, sampled_indexes)
        driving = self._build_matrix(driving_raw, sampled_indexes)

        if any(math.isinf(v) for row in walking for v in row) or any(math.isinf(v) for row in driving for v in row):
            self.logger.print(
                "Warning: at least one sampled arc has inf time. Check CSV key indexing and completeness.",
                SRVLogger.Level.WARNING,
            )

        return CDPPInstance(name=name, locations=local_locations, walking=walking, driving=driving)

    def load_county_sample(
        self,
        county_prefix: str = "Adams",
        instance_id: int = 1,
        num_customers: int = 8,
        seed: int | None = 42,
        depot_policy: Literal["first_sampled", "first_file"] = "first_sampled",
    ) -> CDPPInstance:
        location_path, walking_path, driving_path = self.paths_for_county_instance(county_prefix, instance_id)
        return self.load_instance_from_files(
            location_path=location_path,
            walking_path=walking_path,
            driving_path=driving_path,
            num_customers=num_customers,
            seed=seed,
            depot_policy=depot_policy,
            name=f"{county_prefix}_{instance_id}_n{num_customers}",
        )


# =============================================================================
# Optimization result structures
# =============================================================================


@dataclass
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

    @property
    def completion_time(self) -> float | None:
        if self.objective is None:
            return None
        return self.objective

    def summary(self) -> str:
        return (
            f"{self.name}: status={self.status}, objective={self.objective}, "
            f"runtime={self.runtime:.3f}s, open={self.open_parking}, route={self.route}, "
            f"driving={self.driving_time:.3f}, parking={self.parking_time:.3f}, "
            f"walking={self.walking_time:.3f}, loading={self.loading_time:.3f}, "
            f"service_sets={[ (s.parking, s.customers) for s in self.service_sets ]}"
        )


# =============================================================================
# Solvers
# =============================================================================


class CDPPSolver:
    def __init__(self, instance: CDPPInstance) -> None:
        self.instance = instance
        self.logger = SRVLogger()
        self._require_gurobi()

    @staticmethod
    def _require_gurobi() -> None:
        if gp is None or GRB is None:
            raise ImportError("gurobipy is required. Install Gurobi and gurobipy to run this file.")

    def _parking_time_value(self, parking_time: float | dict[int, float], node: int) -> float:
        if node == self.instance.depot:
            return 0.0
        if isinstance(parking_time, dict):
            return float(parking_time.get(node, 0.0))
        return float(parking_time)

    def shortest_walking_loop(self, parking: int, customers: tuple[int, ...]) -> float:
        if not customers:
            return 0.0
        # q in the paper experiments is small. Exact permutation is fine for sample runs.
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
        parking_nodes = list(parking_nodes if parking_nodes is not None else self.instance.parking_nodes)
        customers_list = list(customers if customers is not None else self.instance.customers)
        service_sets: list[ServiceSetSelection] = []

        if contiguous_order is not None:
            order = list(contiguous_order)
            for start in range(len(order)):
                for length in range(1, min(q, len(order) - start) + 1):
                    subset = tuple(order[start : start + length])
                    # For Modified TSP, restrict parking candidates to nodes in the fixed TSP order.
                    # We allow every customer location as a possible parking node, then the route model
                    # decides which opened parking nodes to use.
                    for parking in parking_nodes:
                        service_sets.append(
                            ServiceSetSelection(
                                parking=parking,
                                customers=subset,
                                walking_cost=self.shortest_walking_loop(parking, subset),
                            )
                        )
            return service_sets

        for parking in parking_nodes:
            for size in range(1, min(q, len(customers_list)) + 1):
                for subset in itertools.combinations(customers_list, size):
                    service_sets.append(
                        ServiceSetSelection(
                            parking=parking,
                            customers=tuple(subset),
                            walking_cost=self.shortest_walking_loop(parking, tuple(subset)),
                        )
                    )
        return service_sets

    def _extract_route(self, x: Any, nodes: list[int], start: int = 0) -> list[int]:
        succ = {}
        for i in nodes:
            for j in nodes:
                if i != j and x[i, j].X > 0.5:
                    succ[i] = j
        route: list[int] = []
        cur = start if start in succ else (next(iter(succ)) if succ else start)
        visited: set[int] = set()
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
    # 1. CDPP MIP, structurally aligned with paper Eq. (1)-(12)
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

        model = gp.Model(name)
        model.Params.OutputFlag = 0
        if time_limit is not None:
            model.Params.TimeLimit = time_limit

        arcs = [(i, k) for i in all_nodes for k in all_nodes if i != k]
        flow_arcs = [(i, k) for i in all_nodes for k in parking_nodes if i != k]

        x = model.addVars(arcs, vtype=GRB.BINARY, name="x_drive")
        z = model.addVars(len(service_sets), vtype=GRB.BINARY, name="z_service")
        v = model.addVars(flow_arcs, vtype=GRB.INTEGER, lb=0, ub=n_customers, name="v_flow")

        driving_parking_expr = gp.quicksum(
            (inst.driving[i][k] + self._parking_time_value(parking_time, k)) * x[i, k]
            for i, k in arcs
        )
        walking_loading_expr = gp.quicksum(
            (service_sets[j].walking_cost + loading_time_per_package * len(service_sets[j].customers)) * z[j]
            for j in range(len(service_sets))
        )
        model.setObjective(driving_parking_expr + walking_loading_expr, GRB.MINIMIZE)

        # (2) vehicle leaves depot once and (3) returns once.
        model.addConstr(gp.quicksum(x[inst.depot, i] for i in parking_nodes) == 1, name="leave_depot_once")
        model.addConstr(gp.quicksum(x[i, inst.depot] for i in parking_nodes) == 1, name="return_depot_once")

        # (4) each customer is served exactly once by selected service sets.
        for c in customers:
            model.addConstr(
                gp.quicksum(z[j] for j, ss in enumerate(service_sets) if c in ss.customers) == 1,
                name=f"serve_customer_{c}_once",
            )

        # (5) vehicle flow conservation at parking nodes.
        for i in parking_nodes:
            model.addConstr(
                gp.quicksum(x[k, i] for k in all_nodes if k != i)
                == gp.quicksum(x[i, k] for k in all_nodes if k != i),
                name=f"drive_flow_{i}",
            )

        # (6) service set can be served from i only if vehicle visits i.
        for j, ss in enumerate(service_sets):
            i = ss.parking
            model.addConstr(
                z[j] <= gp.quicksum(x[k, i] for k in all_nodes if k != i),
                name=f"service_requires_visit_{j}",
            )

        # (7) n packages leave depot in the commodity flow.
        model.addConstr(gp.quicksum(v[inst.depot, i] for i in parking_nodes) == n_customers, name="flow_from_depot")

        # (8) flow can only use selected driving arcs.
        for i, k in flow_arcs:
            model.addConstr(v[i, k] <= n_customers * x[i, k], name=f"flow_link_{i}_{k}")

        # (9) flow decreases by number of customers served at each parking node.
        for i in parking_nodes:
            delivered_at_i = gp.quicksum(len(ss.customers) * z[j] for j, ss in enumerate(service_sets) if ss.parking == i)
            inbound = gp.quicksum(v[k, i] for k in all_nodes if k != i)
            outbound = gp.quicksum(v[i, k] for k in parking_nodes if k != i)
            model.addConstr(inbound - outbound == delivered_at_i, name=f"flow_balance_{i}")

        model.optimize()

        selected_sets = [ss for j, ss in enumerate(service_sets) if model.SolCount > 0 and z[j].X > 0.5]
        open_parking = sorted({ss.parking for ss in selected_sets})
        route = self._extract_route(x, all_nodes, start=inst.depot) if model.SolCount > 0 else []

        driving_time = self._route_driving_time(route)
        parking_total = sum(self._parking_time_value(parking_time, p) for p in open_parking)
        walking_total = sum(ss.walking_cost for ss in selected_sets)
        loading_total = loading_time_per_package * sum(len(ss.customers) for ss in selected_sets)

        return SolverResult(
            name=name,
            status=model.StatusName if hasattr(model, "StatusName") else str(model.Status),
            objective=model.ObjVal if model.SolCount > 0 else None,
            runtime=model.Runtime,
            variables=model.NumVars,
            constraints=model.NumConstrs,
            route=route,
            open_parking=open_parking,
            service_sets=selected_sets,
            driving_time=driving_time,
            parking_time=parking_total,
            walking_time=walking_total,
            loading_time=loading_total,
        )

    # -------------------------------------------------------------------------
    # 2. PA-R + TSP + SSA heuristic from paper Section 3.3
    # -------------------------------------------------------------------------

    def solve_pa_r(self, parking_time: float = 5.0) -> SolverResult:
        inst = self.instance
        customers = inst.customers
        parking_nodes = inst.parking_nodes

        model = gp.Model("PA_R")
        model.Params.OutputFlag = 0

        p_open = model.addVars(parking_nodes, vtype=GRB.BINARY, name="p_open")
        a = model.addVars(parking_nodes, customers, vtype=GRB.BINARY, name="assign")

        model.setObjective(
            parking_time * gp.quicksum(p_open[i] for i in parking_nodes)
            + gp.quicksum(inst.walking[i][k] * a[i, k] for i in parking_nodes for k in customers),
            GRB.MINIMIZE,
        )

        for k in customers:
            model.addConstr(gp.quicksum(a[i, k] for i in parking_nodes) == 1, name=f"assign_once_{k}")
        for i in parking_nodes:
            for k in customers:
                model.addConstr(a[i, k] <= p_open[i], name=f"assign_requires_open_{i}_{k}")
        for i in parking_nodes:
            model.addConstr(p_open[i] <= gp.quicksum(a[i, k] for k in customers), name=f"open_requires_customer_{i}")

        model.optimize()

        service_sets = []
        assignment: dict[int, list[int]] = {}
        if model.SolCount > 0:
            for i in parking_nodes:
                if p_open[i].X > 0.5:
                    assignment[i] = [k for k in customers if a[i, k].X > 0.5]
                    service_sets.append(ServiceSetSelection(i, tuple(assignment[i]), 0.0))

        return SolverResult(
            name="PA_R",
            status=model.StatusName if hasattr(model, "StatusName") else str(model.Status),
            objective=model.ObjVal if model.SolCount > 0 else None,
            runtime=model.Runtime,
            variables=model.NumVars,
            constraints=model.NumConstrs,
            open_parking=sorted(assignment),
            service_sets=service_sets,
        )

    def solve_tsp_over_nodes(self, nodes: list[int], name: str = "TSP") -> SolverResult:
        inst = self.instance
        nodes = list(dict.fromkeys(nodes))
        if inst.depot not in nodes:
            nodes = [inst.depot] + nodes

        if len(nodes) <= 1:
            return SolverResult(name=name, status="TRIVIAL", objective=0.0, runtime=0.0, variables=0, constraints=0, route=nodes)

        model = gp.Model(name)
        model.Params.OutputFlag = 0
        arcs = [(i, j) for i in nodes for j in nodes if i != j]

        x = model.addVars(arcs, vtype=GRB.BINARY, name="x")
        u = model.addVars(nodes, lb=0, ub=len(nodes) - 1, vtype=GRB.CONTINUOUS, name="u")

        model.setObjective(gp.quicksum(inst.driving[i][j] * x[i, j] for i, j in arcs), GRB.MINIMIZE)

        for i in nodes:
            model.addConstr(gp.quicksum(x[i, j] for j in nodes if j != i) == 1, name=f"out_{i}")
            model.addConstr(gp.quicksum(x[j, i] for j in nodes if j != i) == 1, name=f"in_{i}")

        root = inst.depot
        model.addConstr(u[root] == 0, name="root")
        for i in nodes:
            if i != root:
                model.addConstr(u[i] >= 1, name=f"order_lb_{i}")
        for i in nodes:
            for j in nodes:
                if i != j and i != root and j != root:
                    model.addConstr(u[i] - u[j] + len(nodes) * x[i, j] <= len(nodes) - 1, name=f"mtz_{i}_{j}")

        model.optimize()
        route = self._extract_route(x, nodes, start=root) if model.SolCount > 0 else []

        return SolverResult(
            name=name,
            status=model.StatusName if hasattr(model, "StatusName") else str(model.Status),
            objective=model.ObjVal if model.SolCount > 0 else None,
            runtime=model.Runtime,
            variables=model.NumVars,
            constraints=model.NumConstrs,
            route=route,
            driving_time=self._route_driving_time(route),
        )

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
            model = gp.Model(f"SSA_{parking}")
            model.Params.OutputFlag = 0
            y = model.addVars(len(candidates), vtype=GRB.BINARY, name="y")
            model.setObjective(gp.quicksum(candidates[j].walking_cost * y[j] for j in range(len(candidates))), GRB.MINIMIZE)
            for c in customers:
                model.addConstr(
                    gp.quicksum(y[j] for j, ss in enumerate(candidates) if c in ss.customers) == 1,
                    name=f"customer_{c}_once",
                )
            model.optimize()

            total_runtime += model.Runtime
            total_vars += model.NumVars
            total_constraints += model.NumConstrs
            if model.SolCount > 0:
                total_obj += model.ObjVal
                selected.extend(candidates[j] for j in range(len(candidates)) if y[j].X > 0.5)

        return SolverResult(
            name="SSA",
            status="OK",
            objective=total_obj,
            runtime=total_runtime,
            variables=total_vars,
            constraints=total_constraints,
            open_parking=sorted(groups),
            service_sets=selected,
            walking_time=sum(ss.walking_cost for ss in selected),
        )

    def solve_two_echelon_heuristic(
        self,
        q: int = 3,
        parking_time: float = 5.0,
        loading_time_per_package: float = 2.1,
    ) -> SolverResult:
        pa = self.solve_pa_r(parking_time=parking_time)
        groups = {ss.parking: list(ss.customers) for ss in pa.service_sets}
        tsp = self.solve_tsp_over_nodes(pa.open_parking, name="TSP_over_opened_parking")
        ssa = self.solve_ssa_for_groups(groups, q=q)

        objective = (
            (tsp.objective or 0.0)
            + parking_time * len(pa.open_parking)
            + (ssa.objective or 0.0)
            + loading_time_per_package * self.instance.customer_count
        )
        return SolverResult(
            name="TwoEchelon_PA_R_TSP_SSA",
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
    # 3. Modified TSP benchmark
    # -------------------------------------------------------------------------

    def solve_modified_tsp(
        self,
        q: int = 3,
        parking_time: float = 5.0,
        loading_time_per_package: float = 2.1,
        time_limit: float | None = None,
    ) -> SolverResult:
        tsp_all = self.solve_tsp_over_nodes(self.instance.customers, name="TSP_all_customers")
        order = [node for node in tsp_all.route if node != self.instance.depot]
        if not order:
            order = self.instance.customers

        restricted_sets = self.generate_service_sets(q=q, contiguous_order=order)
        return self.solve_cdpp_mip(
            q=q,
            parking_time=parking_time,
            loading_time_per_package=loading_time_per_package,
            time_limit=time_limit,
            candidate_sets=restricted_sets,
            name="Modified_TSP_restricted_CDPP",
        )

    # -------------------------------------------------------------------------
    # 4. Relaxed M-S benchmark
    # -------------------------------------------------------------------------

    def solve_relaxed_ms(
        self,
        alpha: float = 0.6,
        q: int = 3,
        parking_time: float = 5.0,
        loading_time_per_package: float = 2.1,
        time_limit: float | None = None,
    ) -> SolverResult:
        inst = self.instance
        service_sets = self.generate_service_sets(q=q)
        customers = inst.customers
        parking_nodes = inst.parking_nodes
        all_nodes = [inst.depot] + parking_nodes

        model = gp.Model(f"Relaxed_MS_alpha_{alpha}")
        model.Params.OutputFlag = 0
        if time_limit is not None:
            model.Params.TimeLimit = time_limit

        arcs = [(i, k) for i in all_nodes for k in all_nodes if i != k]
        flow_arcs = [(i, k) for i in all_nodes for k in parking_nodes if i != k]
        n_customers = len(customers)

        x = model.addVars(arcs, vtype=GRB.BINARY, name="x_drive")
        z = model.addVars(len(service_sets), vtype=GRB.BINARY, name="z_service")
        v = model.addVars(flow_arcs, vtype=GRB.INTEGER, lb=0, ub=n_customers, name="v_flow")

        driving_expr = gp.quicksum(inst.driving[i][k] * x[i, k] for i, k in arcs)
        walking_expr = gp.quicksum(service_sets[j].walking_cost * z[j] for j in range(len(service_sets)))
        loading_expr = loading_time_per_package * n_customers
        model.setObjective(alpha * driving_expr + (1 - alpha) * walking_expr + loading_expr, GRB.MINIMIZE)

        model.addConstr(gp.quicksum(x[inst.depot, i] for i in parking_nodes) == 1, name="leave_depot_once")
        model.addConstr(gp.quicksum(x[i, inst.depot] for i in parking_nodes) == 1, name="return_depot_once")
        for c in customers:
            model.addConstr(gp.quicksum(z[j] for j, ss in enumerate(service_sets) if c in ss.customers) == 1)
        for i in parking_nodes:
            model.addConstr(
                gp.quicksum(x[k, i] for k in all_nodes if k != i)
                == gp.quicksum(x[i, k] for k in all_nodes if k != i)
            )
        for j, ss in enumerate(service_sets):
            model.addConstr(z[j] <= gp.quicksum(x[k, ss.parking] for k in all_nodes if k != ss.parking))
        model.addConstr(gp.quicksum(v[inst.depot, i] for i in parking_nodes) == n_customers)
        for i, k in flow_arcs:
            model.addConstr(v[i, k] <= n_customers * x[i, k])
        for i in parking_nodes:
            delivered = gp.quicksum(len(ss.customers) * z[j] for j, ss in enumerate(service_sets) if ss.parking == i)
            inbound = gp.quicksum(v[k, i] for k in all_nodes if k != i)
            outbound = gp.quicksum(v[i, k] for k in parking_nodes if k != i)
            model.addConstr(inbound - outbound == delivered)

        model.optimize()

        selected_sets = [ss for j, ss in enumerate(service_sets) if model.SolCount > 0 and z[j].X > 0.5]
        open_parking = sorted({ss.parking for ss in selected_sets})
        route = self._extract_route(x, all_nodes, start=inst.depot) if model.SolCount > 0 else []
        driving_total = self._route_driving_time(route)
        walking_total = sum(ss.walking_cost for ss in selected_sets)
        parking_total = parking_time * len(open_parking)
        loading_total = loading_time_per_package * n_customers

        # Paper comparison: solve weighted model, then evaluate realized completion time by adding parking.
        weighted_value = model.ObjVal if model.SolCount > 0 else None
        completion_time = (
            alpha * driving_total + (1 - alpha) * walking_total + loading_total + parking_total
            if model.SolCount > 0
            else None
        )

        return SolverResult(
            name=f"Relaxed_MS_alpha_{alpha}",
            status=model.StatusName if hasattr(model, "StatusName") else str(model.Status),
            objective=completion_time,
            runtime=model.Runtime,
            variables=model.NumVars,
            constraints=model.NumConstrs,
            route=route,
            open_parking=open_parking,
            service_sets=selected_sets,
            driving_time=driving_total,
            parking_time=parking_total,
            walking_time=walking_total,
            loading_time=loading_total,
            weighted_value=weighted_value,
        )


# =============================================================================
# Experiment runner
# =============================================================================


@dataclass(frozen=True)
class ExperimentConfig:
    county_prefix: str = "Adams"
    instance_id: int = 1
    num_customers: int = 8
    seed: int = 42
    q: int = 3
    parking_time: float = 5.0
    loading_time: float = 2.1
    alpha_values: tuple[float, ...] = (0.5, 0.6, 0.8)
    time_limit: float | None = None
    depot_policy: Literal["first_sampled", "first_file"] = "first_sampled"


class ExperimentRunner:
    BASE_PARKING_TIME = {
        "Cook": 9.0,
        "Adams": 5.0,
        "Cumberland": 1.0,
    }

    PARKING_TIME_GRID = {
        "Cook": (0.0, 3.0, 6.0, 9.0),
        "Adams": (0.0, 3.0, 5.0),
        "Cumberland": (0.0, 1.0),
    }

    def __init__(self, base_dir: str | Path | None = None) -> None:
        self.loader = IllinoisDataLoader(base_dir=base_dir)
        self.logger = SRVLogger()

    def load(self, config: ExperimentConfig) -> CDPPInstance:
        return self.loader.load_county_sample(
            county_prefix=config.county_prefix,
            instance_id=config.instance_id,
            num_customers=config.num_customers,
            seed=config.seed,
            depot_policy=config.depot_policy,
        )

    def run_single_sample(self, config: ExperimentConfig) -> list[SolverResult]:
        instance = self.load(config)
        solver = CDPPSolver(instance)
        results: list[SolverResult] = []

        results.append(
            solver.solve_cdpp_mip(
                q=config.q,
                parking_time=config.parking_time,
                loading_time_per_package=config.loading_time,
                time_limit=config.time_limit,
            )
        )
        results.append(
            solver.solve_modified_tsp(
                q=config.q,
                parking_time=config.parking_time,
                loading_time_per_package=config.loading_time,
                time_limit=config.time_limit,
            )
        )
        for alpha in config.alpha_values:
            results.append(
                solver.solve_relaxed_ms(
                    alpha=alpha,
                    q=config.q,
                    parking_time=config.parking_time,
                    loading_time_per_package=config.loading_time,
                    time_limit=config.time_limit,
                )
            )
        results.append(
            solver.solve_two_echelon_heuristic(
                q=config.q,
                parking_time=config.parking_time,
                loading_time_per_package=config.loading_time,
            )
        )
        return results

    def write_results_csv(self, rows: list[dict[str, Any]], output_path: str | Path) -> None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if not rows:
            output_path.write_text("", encoding="utf-8")
            return
        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def result_to_row(config: ExperimentConfig, result: SolverResult) -> dict[str, Any]:
        return {
            "county": config.county_prefix,
            "instance_id": config.instance_id,
            "num_customers": config.num_customers,
            "seed": config.seed,
            "q": config.q,
            "parking_time_config": config.parking_time,
            "solver": result.name,
            "status": result.status,
            "objective": result.objective,
            "weighted_value": result.weighted_value,
            "runtime": result.runtime,
            "variables": result.variables,
            "constraints": result.constraints,
            "num_open_parking": len(result.open_parking),
            "open_parking": result.open_parking,
            "route": result.route,
            "driving_time": result.driving_time,
            "parking_time": result.parking_time,
            "walking_time": result.walking_time,
            "loading_time": result.loading_time,
            "num_service_sets": len(result.service_sets),
            "service_sets": [(ss.parking, ss.customers) for ss in result.service_sets],
        }

    def run_base_comparison_sample(
        self,
        counties: tuple[str, ...] = ("Cook", "Adams", "Cumberland"),
        instance_ids: tuple[int, ...] = (1,),
        num_customers: int = 8,
        seed: int = 42,
        output_csv: str | Path | None = None,
    ) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for county in counties:
            for instance_id in instance_ids:
                config = ExperimentConfig(
                    county_prefix=county,
                    instance_id=instance_id,
                    num_customers=num_customers,
                    seed=seed,
                    parking_time=self.BASE_PARKING_TIME[county],
                )
                for result in self.run_single_sample(config):
                    rows.append(self.result_to_row(config, result))
        if output_csv is not None:
            self.write_results_csv(rows, output_csv)
        return rows

    def run_parking_time_impact_sample(
        self,
        county: str = "Cook",
        instance_id: int = 1,
        num_customers: int = 8,
        seed: int = 42,
        output_csv: str | Path | None = None,
    ) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for parking_time in self.PARKING_TIME_GRID[county]:
            config = ExperimentConfig(
                county_prefix=county,
                instance_id=instance_id,
                num_customers=num_customers,
                seed=seed,
                parking_time=parking_time,
            )
            instance = self.load(config)
            solver = CDPPSolver(instance)
            result = solver.solve_cdpp_mip(q=config.q, parking_time=parking_time, loading_time_per_package=config.loading_time)
            rows.append(self.result_to_row(config, result))
        if output_csv is not None:
            self.write_results_csv(rows, output_csv)
        return rows

    def run_capacity_impact_sample(
        self,
        county: str = "Adams",
        instance_id: int = 1,
        num_customers: int = 8,
        seed: int = 42,
        capacities: tuple[int, ...] = (1, 2, 3, 4, 5, 6),
        output_csv: str | Path | None = None,
    ) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for q in capacities:
            config = ExperimentConfig(
                county_prefix=county,
                instance_id=instance_id,
                num_customers=num_customers,
                seed=seed,
                q=q,
                parking_time=self.BASE_PARKING_TIME[county],
            )
            instance = self.load(config)
            solver = CDPPSolver(instance)
            # Use exact CDPP for small samples; for bigger q/n switch to heuristic as needed.
            result = solver.solve_cdpp_mip(q=q, parking_time=config.parking_time, loading_time_per_package=config.loading_time)
            rows.append(self.result_to_row(config, result))
        if output_csv is not None:
            self.write_results_csv(rows, output_csv)
        return rows


# =============================================================================
# CLI-lite main
# =============================================================================


def main() -> None:
    logger = SRVLogger(SRVLogger.Args(level=logging.INFO, memory=False))

    # Small default sample. Increase num_customers only after verifying runtime/license limits.
    config = ExperimentConfig(
        county_prefix="Adams",
        instance_id=1,
        num_customers=10,
        seed=42,
        q=3,
        parking_time=5.0,
        loading_time=2.1,
        alpha_values=(0.5, 0.6, 0.8),
        time_limit=None,
        depot_policy="first_sampled",
    )

    runner = ExperimentRunner()
    results = runner.run_single_sample(config)
    rows = [runner.result_to_row(config, r) for r in results]
    output_path = Path("srv_reimplement_final_sample_results.csv")
    runner.write_results_csv(rows, output_path)

    logger.print(f"Wrote sample results to: {output_path.resolve()}")
    for result in results:
        logger.print(result.summary())


if __name__ == "__main__":
    main()
