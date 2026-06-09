# THỰC HÀNH 02 - OPENCV: LÀM TRƠN ẢNH VÀ PHÁT HIỆN BIÊN

## 1. Thông tin chung

Bài thực hành thuộc môn **Thị Giác Máy Tính Nâng Cao** (*Advanced Computer Vision - K35 - HCMUS*).

- Thành viên nhóm:
  - Nguyễn Trọng Hiếu – 25C11042 (Nhóm trưởng)
  - Trương Lê Bảo Trân – 25C11071
- Giảng viên hướng dẫn: ThS. Nguyễn Mạnh Hùng

---

## 2. Mục tiêu bài thực hành

Bài thực hành sử dụng OpenCV để thực hiện hai nhóm kỹ thuật xử lý ảnh cơ bản:

1. **Làm trơn ảnh (Smoothing)**
   - Averaging Blur
   - Gaussian Blur
   - Median Blur

2. **Phát hiện biên ảnh (Edge Detection)**
   - Sobel
   - Laplacian
   - Laplacian of Gaussian (LoG)
   - Canny

Ảnh đầu vào được sử dụng là `Lenna.jpg` trong thư mục `images/`.

---

## 3. Cấu trúc thư mục

```text
source/
├── TH02.ipynb
├── README.md
├── requirements.txt
├── images/
│   └── Lenna.jpg
└── output/
    ├── 01_averaging_blur.jpg
    ├── 02_gaussian_blur.jpg
    ├── 03_median_blur.jpg
    ├── 04_sobel_edge.jpg
    ├── 05_laplacian_edge.jpg
    ├── 06_log_edge.jpg
    └── 07_canny_edge.jpg
```

---

## 4. Môi trường thực hiện

- Python 3.11+
- Jupyter Notebook
- NumPy
- OpenCV-Python
- Matplotlib
- Pillow

---

## 5. Cài đặt môi trường

Tạo môi trường ảo:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows
```

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

---

## 6. Chạy notebook

Mở Jupyter Notebook:

```bash
jupyter notebook
```

Sau đó mở file:

```text
TH02.ipynb
```

Chạy toàn bộ notebook theo thứ tự từ trên xuống dưới.

---

## 7. Nội dung đã thực hiện

### 7.1. Làm trơn ảnh

| Phương pháp | Ý nghĩa |
|---|---|
| Averaging Blur | Lấy trung bình các pixel lân cận, giúp làm mờ đều toàn ảnh. |
| Gaussian Blur | Làm trơn bằng trọng số Gaussian, giữ chuyển tiếp ảnh tự nhiên hơn Averaging. |
| Median Blur | Lấy trung vị trong vùng lân cận, phù hợp để giảm nhiễu muối tiêu. |

### 7.2. Phát hiện biên ảnh

| Phương pháp | Ý nghĩa |
|---|---|
| Sobel | Tính gradient theo hướng ngang và dọc để phát hiện biên. |
| Laplacian | Dùng đạo hàm bậc hai để tìm vùng thay đổi cường độ mạnh. |
| LoG | Làm trơn bằng Gaussian trước, sau đó dùng Laplacian để giảm nhiễu. |
| Canny | Phương pháp nhiều bước, cho biên mảnh và rõ hơn. |

---

## 8. Kết quả đầu ra

Các ảnh kết quả được lưu tại:

```text
source/output/
```

Danh sách kết quả:

- `01_averaging_blur.jpg`
- `02_gaussian_blur.jpg`
- `03_median_blur.jpg`
- `04_sobel_edge.jpg`
- `05_laplacian_edge.jpg`
- `06_log_edge.jpg`
- `07_canny_edge.jpg`

---

## 9. Nhận xét tổng quát

- Các phương pháp smoothing giúp giảm nhiễu và làm mềm ảnh trước khi xử lý tiếp.
- Gaussian Blur thường phù hợp làm bước tiền xử lý trước phát hiện biên.
- Laplacian nhạy với nhiễu, còn LoG ổn định hơn nhờ có bước Gaussian Blur.
- Canny cho kết quả biên rõ, mảnh và dễ quan sát nhất trong nhóm phương pháp phát hiện biên đã thử nghiệm.
