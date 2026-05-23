"""
test_cdpp_solvers.py — Validate CDPP solver port (HiGHS vs CBC) on synthetic instances.
Since Illinois data may not be available, generates random instances for testing.
"""

from __future__ import annotations
import math
import random
import time
from root_paper.core.cdpp_mip_solver import CDPPMipSolver, CDPPInstance, Location


def generate_random_instance(n_customers: int, seed: int = 42, area: float = 10.0) -> CDPPInstance:
    """Generate a random CDPP instance with n_customers + 1 depot."""
    rng = random.Random(seed)
    n = n_customers + 1  # depot + customers
    points = [(rng.uniform(0, area), rng.uniform(0, area)) for _ in range(n)]
    locations = [Location(original_idx=i, lat=points[i][0], lon=points[i][1]) for i in range(n)]

    # Walking speed ~3 mph = 20 min/mile, driving ~15 mph = 4 min/mile
    walking_speed = 20.0  # min per unit
    driving_speed = 4.0   # min per unit

    dist = [[math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
             for j in range(n)] for i in range(n)]
    walking = [[dist[i][j] * walking_speed for j in range(n)] for i in range(n)]
    driving = [[dist[i][j] * driving_speed for j in range(n)] for i in range(n)]

    return CDPPInstance(name=f"random_n{n_customers}_s{seed}", locations=locations,
                        walking=walking, driving=driving)


def run_comparison(n_customers: int, seed: int = 42, q: int = 3, parking_time: float = 5.0):
    """Run all solvers with both backends and compare."""
    inst = generate_random_instance(n_customers, seed)
    print(f"\n{'='*75}")
    print(f"Instance: {inst.name} | n={n_customers} | q={q} | p={parking_time}")
    print(f"{'='*75}")

    for backend in ["cbc", "highs"]:
    # for backend in ["highs"]:
        solver = CDPPMipSolver(inst, backend=backend)

        # --- Two-echelon heuristic (fastest, always run) ---
        res = solver.solve_two_echelon_heuristic(q=q, parking_time=parking_time)
        print(f"  [{backend.upper():5s}] TwoEchelon : obj={res.objective:>10.2f}  "
              f"time={res.runtime:>7.3f}s  parks={len(res.open_parking):>2d}  "
              f"D={res.driving_time:.1f} P={res.parking_time:.1f} "
              f"W={res.walking_time:.1f} L={res.loading_time:.1f}")

        # --- CDPP exact (only for small instances) ---
        if n_customers <= 15:
            res = solver.solve_cdpp_mip(q=q, parking_time=parking_time, time_limit=120)
            obj_str = f"{res.objective:>10.2f}" if res.objective else "     None"
            print(f"  [{backend.upper():5s}] CDPP exact : obj={obj_str}  "
                  f"time={res.runtime:>7.3f}s  parks={len(res.open_parking):>2d}  "
                  f"status={res.status}")

        # --- Modified TSP (medium) ---
        if n_customers <= 20:
            res = solver.solve_modified_tsp(q=q, parking_time=parking_time, time_limit=120)
            obj_str = f"{res.objective:>10.2f}" if res.objective else "     None"
            print(f"  [{backend.upper():5s}] ModTSP     : obj={obj_str}  "
                  f"time={res.runtime:>7.3f}s  parks={len(res.open_parking):>2d}  "
                  f"status={res.status}")


def main():
    print("CDPP Solver Comparison: HiGHS vs CBC (python-mip)")
    print("=" * 75)

    # Small instances: all solvers
    for n in [5, 8, 10]:
        run_comparison(n, q=3, parking_time=5.0)

    # Medium: heuristic + modified TSP
    for n in [15, 20]:
        run_comparison(n, q=3, parking_time=5.0)

    # # Larger: heuristic only
    # # for n in [30, 50]:
    # for n in [30, 35, 40, 45, 50]:
    #     run_comparison(n, q=3, parking_time=5.0)

    print(f"\n{'='*75}")
    print("All tests completed.")


if __name__ == "__main__":
    main()
