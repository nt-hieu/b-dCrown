# THỰC HÀNH 01 - OPENCV CƠ BẢN

## Thông tin chung

Bài thực hành thuộc môn Thị Giác Máy Tính Nâng Cao (Advanced Computer Vision), K35 - HCMUS
- Thành viên nhóm
   - Nguyễn Trọng Hiếu – 25C11042 (Nhóm trưởng)
   - Trương Lê Bảo Trân – 25C11071
- Giảng viên hướng dẫn:
   - ThS. Nguyễn Mạnh Hùng

## Nội dung thực hiện

Bài thực hành bao gồm các nội dung:

1. Đọc và hiển thị hình ảnh (Open, Show)
2. Thay đổi kích thước ảnh (Resize)
3. Xoay ảnh (Rotate)
4. Biến đổi màu sắc
   * RGB → Gray
   * RGB → HSV
   * HSV → RGB
5. Điều chỉnh độ sáng (Brightness)
6. Điều chỉnh độ tương phản (Contrast)

Mỗi nội dung đều được thực hiện theo hai cách:
* Cài đặt thủ công (Manual Implementation)
* Sử dụng thư viện OpenCV

Đồng thời tiến hành so sánh kết quả và thời gian thực thi giữa hai phương pháp.

---

## Cấu trúc thư mục

```ps
source/
├── TH01.ipynb
├── requirements.txt
├── README.md
├── images/
│ └── Lenna.jpg
└── output/
```
---

## Môi trường thực hiện

* Python 3.11
* Virtual Environment (venv)

### Thư viện sử dụng

* NumPy
* OpenCV-Python
* Matplotlib
* Pillow

---

## Cài đặt môi trường

Tạo môi trường ảo:

```bash
python -m venv venv
```
Kích hoạt môi trường:

Windows:
```bash
venv\Scripts\activate
```
Cài đặt các thư viện:

```bash
pip install -r requirements.txt

```
Restar kernel --> Chọn kernel .venv
---

*Note: 
1. Cài đặt extension Jupyter Notebook trong Vs Code
2. Trường hợp chạy lệnh activate bị lỗi: 
```bash
"cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170. At line:1 char:1 + venv\Scripts\activate + ~~~~~~~~~~~~~~~~~~~~~ + CategoryInfo : SecurityError: (:) [], PSSecurityException + FullyQualifiedErrorId : UnauthorizedAccess"
```
Lỗi này  do PowerShell đang chặn việc chạy script (.ps1) 
theo chính sách bảo mật của Windows (Execution Policy).

Cách khắc phục:
1. Mở PowerShell với quyền bình thường và chạy lệnh:
   
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
2. Sau đó chọn Y
3. Rồi kích hoạt lại môi trường bằng lệnh: venv\Scripts\Activate.ps1


## Chạy chương trình

Mở file: TH01.ipynb và thực thi toàn bộ notebook theo thứ tự từ trên xuống dưới.

Notebook sẽ:

* Tự tạo thư mục images nếu chưa tồn tại.
* Tự tạo thư mục output nếu chưa tồn tại.
* Tự tải ảnh Lenna nếu chưa có trong thư mục images.

---

## Kết quả

Các ảnh kết quả được lưu trong thư mục:

```
source/output/
```

bao gồm:

* Kết quả Resize
* Kết quả Rotate
* Kết quả chuyển đổi màu sắc
* Kết quả điều chỉnh Brightness
* Kết quả điều chỉnh Contrast

