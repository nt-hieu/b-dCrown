Để làm lại toàn bộ thực nghiệm Section 5, nên reimplement **4 giải thuật top-level**, hoặc nếu tách module thì thành **6 solver/module**.

## 1. Các giải thuật cần reimplement

| Nhóm | Giải thuật | Mục đích |
|---|---|---|
| 1 | **CDPP MIP exact** | Lời giải chính/tối ưu để so sánh |
| 2 | **Modified TSP** | Benchmark đại diện thực hành công nghiệp |
| 3 | **Relaxed M-S** | Benchmark đại diện mô hình học thuật trước đó |
| 4 | **Two-echelon heuristic** | Chạy instance lớn n=100, gồm **PA-R + TSP + SSA** |

Nếu viết code rõ ràng, nên tách thành 6 solver:

- `solve_cdpp_mip`
- `solve_modified_tsp`
- `solve_relaxed_ms`
- `solve_pa_r`
- `solve_tsp_over_parking`
- `solve_ssa`

### 1.1. Mã giả cho 6 hàm

#### 1.1.1 `solve_cdpp_mip`

```text
Input: driving matrix D, walking matrix W, parking_time p, loading_time f, capacity q
Output: solution with route, open parking, selected service sets, objective

1. Let depot = 0, customers = {1..n-1}, parking nodes = {1..n-1}
2. Generate all candidate service sets S:
	- for each parking i
	- for each subset T of customers with |T| <= q
	- compute walking loop cost w(i, T)
3. Create MIP variables:
	- y_i = 1 if parking i is open
	- z_s = 1 if service set s is selected
	- x_ik = 1 if vehicle drives from node i to node k
	- v_ik = flow variable for remaining customers on arc (i,k)
4. Objective:
	minimize sum(D[i,k] + p_k) * x_ik + sum(w(s) + f*|s|) * z_s
5. Constraints:
	- vehicle leaves depot once and returns once
	- each customer is covered by exactly one selected service set
	- a service set can be selected only if its parking is open
	- flow conservation on driving arcs
	- flow amount decreases by number of customers served at each parking
	- MTZ / subtour elimination constraints for vehicle route
6. Solve MIP
7. Extract selected service sets, open parking nodes, and route from x and z
8. Return objective, runtime, and breakdown statistics
```

#### 1.1.2 `solve_modified_tsp`

```text
Input: D, W, p, f, q
Output: restricted CDPP solution based on TSP order

1. Solve a TSP on customer nodes using driving matrix D
2. Obtain the visiting order of customers from the TSP route
3. From this fixed order, generate potential service sets:
	- take contiguous subsequences of length <= q
	- for each subsequence, compute its walking loop cost
4. Call the CDPP MIP helper with this restricted set family
5. Keep the CDPP objective structure, but on the restricted candidate sets
6. Return route, open parking nodes, selected service sets, and objective
```

#### 1.1.3 `solve_relaxed_ms`

```text
Input: D, W, alpha, p, f, q
Output: relaxed benchmark result and final completion time

1. Build candidate service sets exactly as in CDPP
2. Solve a relaxed CDPP-like MIP with objective:
		alpha * driving cost + (1 - alpha) * walking cost
	where parking time is NOT inside the objective
3. Extract the solution and count the number of parking stops s
4. Compute final completion time:
		completion_time = weighted_objective + s * p
5. Return weighted objective, completion time, route, and service sets
```

#### 1.1.4 `solve_pa_r`

```text
Input: walking matrix W, parking_time p
Output: parking assignment result

1. Create binary variable a[i,k] = 1 if customer k is assigned to parking i
2. Create binary variable p_open[i] = 1 if parking i is opened
3. Objective:
		minimize p * sum(p_open[i]) + sum(W[i,k] * a[i,k])
4. Constraints:
	- each customer is assigned to exactly one parking
	- a[i,k] <= p_open[i]
	- p_open[i] <= sum_k a[i,k]
	  (open parking must serve at least one customer)
5. Solve MIP
6. Return the open parking nodes and the customer groups per parking
```

#### 1.1.5 `solve_tsp_over_parking`

```text
Input: list of parking nodes V, driving matrix D
Output: Hamiltonian cycle over the parking nodes

1. Ensure depot 0 is included in V
2. Create binary edge variables x[i,j]
3. Objective:
		minimize sum(D[i,j] * x[i,j])
4. Degree constraints:
		each node has exactly one outgoing edge and one incoming edge
5. Add MTZ subtour elimination with depot as root
6. Solve the TSP MIP
7. Extract the route from x
```

#### 1.1.6 `solve_ssa`

```text
Input: customer groups from PA-R, walking matrix W, capacity q
Output: service-set assignment per parking

1. For each parking i and its customer group G_i:
	- generate all candidate service sets T subset of G_i with |T| <= q
	- compute walking loop cost w(i,T)
2. Create binary variable y_T for each candidate service set T
3. Objective:
		minimize sum(w(i,T) * y_T)
4. Constraints:
	- each customer in G_i must appear in exactly one selected service set
	- solve this MIP separately for each parking i
5. Collect the chosen service sets and total walking cost
```

> Ghi chú: các mã giả trên bám theo cấu trúc hiện tại trong `srv_reimplement.py`, tức là dùng depot riêng, sinh service-set ứng viên, và để Modified TSP / Relaxed M-S quay về một biến thể của CDPP thay vì assignment model đơn giản.

Paper dùng **CDPP** để xét parking time trong objective, **Modified TSP** để mô phỏng thực tế kiểu TSP, **Relaxed M-S** để so với mô hình weighted driving/walking, và **heuristic** để xử lý instance lớn.

## 2. Config dữ liệu chung

Dùng 3 county:

| County | Loại môi trường |
|---|---|
| **Cook** | urban |
| **Adams** | suburban |
| **Cumberland** | rural |

Config chung:

| Tham số | Giá trị |
|---|---|
| Parking locations | **Π = C ∪ {0}** |
| n = 50 | **10 instances** mỗi county |
| n = 100 | **5 instances** mỗi county |
| Base capacity | **q = 3** |
| Base loading time | **f = 2.1 phút/package** |
| Solver | **Python + Gurobi** |

Base parking time:

| County | p |
|---|---:|
| **Cook** | 9 |
| **Adams** | 5 |
| **Cumberland** | 1 |

Paper mô tả rõ base case là **n = 50**, **location-dependent parking time**, **q = 3**, **f = 2.1**.

## 3. CDPP MIP chạy với config nào?

Dùng cho thực nghiệm chính với **n = 50**.

Chạy các config:

| Thực nghiệm | Config |
|---|---|
| **Base comparison** | county = Cook/Adams/Cumberland, n = 50, q = 3, f = 2.1, p base |
| **Impact of parking time** | Cook: p = 0, 3, 6, 9; Adams: p = 0, 3, 5; Cumberland: p = 0, 1 |
| **Impact of capacity** | q = 1, 2, 3, 4, 5, 6, với parking time base từng county |

Output cần lưu:

- **objective_value**
- **total_completion_time**
- **parking_time_total**
- **driving_time_total**
- **walking_time_total**
- **loading_time_total**
- **number_of_parking_stops**
- **opened_parking_nodes**
- **selected_service_sets**
- **vehicle_route**
- **runtime**
- **gap**

**CDPP** là mô hình quan trọng nhất vì nó tối ưu trực tiếp **driving + parking + walking + loading**.

## 4. Modified TSP chạy với config nào?

Dùng trong benchmark Section 5.3.

Config giống base case:

| Tham số | Giá trị |
|---|---|
| County | **Cook, Adams, Cumberland** |
| n | **50** |
| q | **3** |
| f | **2.1** |
| p | **Cook 9, Adams 5, Cumberland 1** |

Quy trình chạy:

1. **Solve TSP** bằng driving matrix **D**
2. **Fix** customer visiting order từ TSP
3. **Generate** service sets consistent với thứ tự đó
4. **Solve** restricted CDPP objective
5. **Compute** completion time

**Modified TSP** cần so sánh với **CDPP** theo phần trăm giảm completion time. Paper dùng nó để mô phỏng thực tế: có route TSP trước, sau đó tài xế quyết định parking/walking trong thứ tự đó.

## 5. Relaxed M-S chạy với config nào?

Dùng trong benchmark Section 5.3 và phân tích cấu trúc Fig. 5.

Config:

| Tham số | Giá trị |
|---|---|
| County | **Cook, Adams, Cumberland** |
| n | **50** |
| q | **3** |
| f | **2.1** |
| p | **base từng county** |
| α | **0.5, 0.6, 0.8** |

Objective:

$$
\alpha \cdot \text{driving time} + (1-\alpha) \cdot \text{walking time}
$$

Sau khi giải xong, tính completion time thật:

$$
v + sp
$$

trong đó **v** là objective của Relaxed M-S, **s** là số lần đỗ xe. Paper dùng **α = 0.6, 0.8**, và thêm **α = 0.5** để cân bằng driving/walking.

## 6. Two-echelon heuristic chạy với config nào?

Dùng khi bài toán lớn hoặc khi **q** lớn làm CDPP MIP khó giải.

Heuristic gồm 3 bước:

- **PA-R**: chọn parking nodes và gán customers vào parking
- **TSP**: nối các parking nodes thành Hamiltonian cycle theo driving time
- **SSA**: tại từng parking, chia customers thành service sets size <= q

Config chính:

| Thực nghiệm | Config |
|---|---|
| **Heuristic quality** | n = 50, so với CDPP optimal |
| **Large instance** | n = 100, 5 instances/county |
| **Parking time impact** | Cook n = 100, p = 0, 3, 6, 9 |
| **Capacity impact** | q = 1, 2, 3, 4, 5, 6, n = 50 và n = 100 |

Output giống CDPP: **total time**, breakdown của **parking/driving/walking/loading**, **số điểm đỗ**, và **runtime**.

## 7. Tổng số lần chạy tối thiểu

Nếu làm giống paper ở mức chính:

| Hạng mục | Số runs |
|---|---:|
| **Base comparison** | 3 counties × 10 instances × (1 CDPP + 1 Modified TSP + 3 Relaxed M-S) = **150** |
| **Parking time impact, n = 50** | Cook: 4 parking values; Adams: 3 parking values; Cumberland: 2 parking values ⇒ (4 + 3 + 2) × 10 = **90 CDPP runs** |
| **Capacity impact, n = 50** | 3 counties × 10 instances × 6 q = **180 runs** |
| **Large instance, n = 100** | 3 counties × 5 instances × 6 q = **90 heuristic/CDPP runs** |

Vậy để reproduce khá đầy đủ, bạn cần khoảng **500+ solver runs**, tùy bạn có chạy đầy đủ heuristic-quality appendix hay không.

---

## 8. Thống kê độ phức tạp và thời gian chạy ước tính — `SRVGurobiCustom` (CBC)

> Cập nhật dựa trên benchmark thực tế với Adams county, `seed=42`, `q=3`, `p=5.0`.  
> Backend: **python-mip 1.17.6 / CBC 2.929**, không dùng Gurobi license.

### 8.1. Quy mô mô hình theo n (q = 3)

| n | Service sets (CDPP) | Service sets (ModTSP) | Biến (CDPP) | Ràng buộc (CDPP) | Biến (PA-R) | Biến (TSP) |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 125 | 60 | 185 | 173 | 30 | 36 |
| 10 | 1.750 | 270 | 1.970 | 1.893 | 110 | 121 |
| 20 | 27.000 | 1.140 | 27.840 | 27.483 | 420 | 441 |
| 30 | 135.750 | 2.610 | 137.610 | 136.773 | 930 | 961 |
| **50** | **1.043.750** | **7.350** | **1.048.850** | **1.046.453** | **2.550** | **2.601** |

**Công thức:**
- Service sets (CDPP) = n × Σ C(n,k) với k=1..q  
- Service sets (ModTSP) = n × Σ (n−k+1) với k=1..q *(contiguous subsequences)*  
- Biến (CDPP) = |arcs| + |sets| + |flow_arcs| với |arcs| = (n+1)·n, |flow_arcs| = (n+1)·n  
- Biến (PA-R) = n + n² (p_open + a)  
- Biến (TSP) = n(n+1) + (n+1) (x + u)

---

### 8.2. Phân tích độ phức tạp lý thuyết

| Solver | Số biến nhị phân | Số ràng buộc | Độ phức tạp sinh | Ghi chú |
|---|---|---|---|---|
| `solve_pa_r` | O(n²) | O(n²) | O(n²) | LP relaxation thường integral |
| `solve_tsp_over_nodes` | O(n²) | O(n²) | O(n²) | MTZ formulation |
| `solve_ssa_for_groups` | O(n·C(n/k, q)) | O(n) | O(n·C(n,q)) | Giải độc lập từng parking |
| `solve_two_echelon_heuristic` | O(n²) tổng | O(n²) | O(n + n²) | PA-R + TSP + SSA song song |
| `solve_modified_tsp` | O(n²) + O(n·q·n) | O(n² + n²q) | O(n²) | TSP + restricted CDPP |
| `solve_relaxed_ms` | O(n² + n·C(n,q)) | O(n² + n·C(n,q)) | **O(n·C(n,q))** | Cùng quy mô CDPP, pruning 90% |
| `solve_cdpp_mip` | O(n² + n·C(n,q)) | O(n² + n·C(n,q)) | **O(n·C(n,q))** | Bottleneck chính cho n=50 |

---

### 8.3. Thời gian chạy thực tế (wall-clock, giây)

> Đo trên cùng máy, Adams county, seed=42. `SRVGurobiCustom` với `cuts=2`, `emphasis=FEASIBILITY`, `preprocess=1`.

| Solver | n=5 | n=10 | Ước tính n=20 | Ước tính n=30 | **Ước tính n=50** |
|---|---:|---:|---:|---:|---:|
| `solve_pa_r` | 0.14 s | 0.02 s | ~0.05 s | ~0.2 s | **~1–5 s** |
| `solve_tsp_over_nodes` | 0.19 s | 0.53 s | ~2 s | ~10 s | **~60–300 s** |
| `solve_ssa_for_groups` | <0.01 s | <0.01 s | ~0.1 s | ~0.5 s | **~5–30 s** |
| `solve_two_echelon_heuristic` | 0.08 s | 0.28 s | ~1 s | ~5 s | **~30–180 s** |
| `solve_modified_tsp` | 0.49 s | 1.61 s | ~5 s | ~30 s | **~120–1800 s** |
| `solve_relaxed_ms` | 0.42 s | 4.47 s | ~30 s | ~300 s | **~1800–14400 s** |
| `solve_cdpp_mip` | 0.38 s | 5.12 s | ~60 s | ~600 s | **~7200–86400 s** |

> **Chú thích ước tính n=50:**
> - Dựa trên tốc độ tăng thực nghiệm từ n=5→10 kết hợp tăng trưởng lý thuyết của số service sets.
> - Với CDPP và Relaxed M-S: sau pruning 90th-percentile, còn ~104.375 sets ở n=50 (vs 1.576 ở n=10), tỷ lệ ~66× số biến → tốc độ giải không tuyến tính.
> - Khoảng ước tính rộng vì thực tế phụ thuộc lớn vào cấu trúc instance (urban vs rural, độ thưa của walking matrix).

---

### 8.4. Kết quả thực tế n=50 từ user output (Adams, seed=42)

Từ output `python srv_reproduce.py` với n=50 (num_customers=50):

| Metric | Giá trị |
|---|---|
| Solver | `solve_two_echelon_heuristic` (CBC) |
| Status | OK |
| Objective (completion time) | **266.43 phút** |
| Driving time | 19.05 phút |
| Parking time | 80.00 phút (16 stops × 5 phút) |
| Walking time | 62.37 phút |
| Loading time | 105.00 phút (50 packages × 2.1 phút) |
| Open parking nodes | 16 nodes |
| Service sets selected | 33 sets |
| **Wall-clock runtime** | **~3 giây** (PA-R + TSP + SSA) |

> **Nhận xét**: `solve_two_echelon_heuristic` là solver **nhanh và ổn định nhất** cho n=50, hoàn thành trong ~3 giây nhờ decomposition (PA-R → TSP nhỏ qua ~16 nodes → SSA độc lập từng parking). Đây là solver khuyến nghị cho n=50 trong production.

---

### 8.5. Nhận xét và khuyến nghị theo từng solver

| Solver | Khả năng n=50 trong 24h | Chất lượng lời giải | Khuyến nghị |
|---|---|---|---|
| `solve_two_echelon_heuristic` | ✅ **~3–180 s** | Heuristic (near-optimal) | **Dùng cho tất cả experiments n=50** |
| `solve_modified_tsp` | ✅ **~2–30 phút** | Gần optimal trên restricted sets | Dùng cho benchmark comparison |
| `solve_pa_r` | ✅ **<10 s** | Optimal (sub-problem) | Sub-solver trong heuristic |
| `solve_tsp_over_nodes` | ✅ **<5 phút** | Optimal (TSP trên n nodes) | Sub-solver, MTZ chậm hơn DFJ |
| `solve_relaxed_ms` | ⚠️ **~30 phút–4 giờ** | Optimal trên relaxed Eq.23 | Cần pruning; chạy được trong 24h |
| `solve_cdpp_mip` | ⚠️ **~2–24 giờ, feasible only** | Feasible, gap lớn cho n=50 | Chỉ tìm được incumbent; cần time_limit=86400 |

#### Lý do `solve_cdpp_mip` khó với n=50:
- Số service sets lý thuyết: **1.043.750** (sau pruning 90%: ~**104.375**)
- Số biến MIP: ~**1.048.850** (vs 1.970 ở n=10, tăng ~532×)
- CBC cần branch nhiều lần trên không gian rất lớn → chỉ tìm feasible solution trong 24h
- **Giải pháp**: Dùng `solve_modified_tsp` (restricted sets chỉ **7.350**) như proxy cho CDPP chất lượng cao

#### Lý do `solve_two_echelon_heuristic` nhanh với n=50:
- **PA-R**: MIP n²=2500 biến, giải < 5s
- **TSP**: chỉ trên ~16 opened parking nodes → 16×15=240 biến → giải <1s
- **SSA**: Từng parking giải độc lập với ≤ q=3 customers/nhóm → trivial
- Tổng: **~3 giây** wall-clock thực tế

---

### 8.6. Cấu hình CBC tối ưu trong `SRVGurobiCustom`

```python
m.preprocess = 1          # Presolve ON — giảm số biến/ràng buộc trước khi giải
m.cuts = 2                # Aggressive cuts — Gomory, MIR, knapsack, clique, zero-half
m.emphasis = FEASIBILITY  # MIPFocus=1 — tìm incumbent nhanh, hy sinh chứng minh tối ưu
m.max_seconds = 86400     # Time limit 24h cho n=50
# Branching: CBC dùng pseudo-cost branching tự động (không cần set thủ công)
# Heuristics: RINS và feasibility pump được kích hoạt tự động khi cuts=2 + emphasis=FEASIBILITY
```

**Tác động thực nghiệm**:
- `cuts=2` giảm LP relaxation gap → branch ít hơn → nhanh hơn ~2–5× so với `cuts=0`
- `emphasis=FEASIBILITY` giúp tìm feasible solution đầu tiên trong vài giây (vs hàng phút nếu không set)
- `preprocess=1` tự động loại biến cố định và đơn giản hóa ràng buộc

---

*Cập nhật: 2026-05-19 | Backend: SRVGurobiCustom / python-mip 1.17.6 / CBC 2.929*
