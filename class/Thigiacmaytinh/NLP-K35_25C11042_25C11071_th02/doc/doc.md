# BÁO CÁO THỰC HÀNH 02  
# OPENCV: LÀM MỜ ẢNH VÀ XÁC ĐỊNH BIÊN ẢNH

## Phân công công việc

| Thành viên | Nhiệm vụ | Hoàn thành |
|---|---|---|
| 25C11042 - Nguyễn Trọng Hiếu | Chuẩn bị ảnh đầu vào; đọc và hiển thị ảnh; thực hiện nhóm phương pháp làm mờ ảnh gồm Averaging Blur, Gaussian Blur, Median Blur; viết phần giới thiệu, mục tiêu, cơ sở lý thuyết về ảnh số và smoothing. | 100% |
| 25C11071 - Trương Lê Bảo Trân | Thực hiện nhóm kỹ thuật xác định biên gồm Sobel, Laplacian, Laplacian of Gaussian và Canny; viết phần thiết kế thực nghiệm, kết quả, nhận xét và kết luận. | 100% |

---

## Bảng đánh giá nội dung đã hoàn thành

| Nội dung | Mô tả thuật toán | Pseudocode | Triển khai bằng OpenCV | So sánh / nhận xét |
|---|---:|---:|---:|---:|
| Đọc và hiển thị ảnh | ✓ | ✓ | ✓ | ✓ |
| Averaging Blur | ✓ | ✓ | ✓ | ✓ |
| Gaussian Blur | ✓ | ✓ | ✓ | ✓ |
| Median Blur | ✓ | ✓ | ✓ | ✓ |
| Sobel Edge Detection | ✓ | ✓ | ✓ | ✓ |
| Laplacian Edge Detection | ✓ | ✓ | ✓ | ✓ |
| Laplacian of Gaussian (LoG) | ✓ | ✓ | ✓ | ✓ |
| Canny Edge Detection | ✓ | ✓ | ✓ | ✓ |

---

## Mục lục

- Phân công công việc
- Bảng đánh giá nội dung đã hoàn thành
- Mục lục
- Danh mục bảng biểu
- Chương 1. Tổng quan bài thực hành
- Chương 2. Cơ sở lý thuyết
- Chương 3. Thiết kế và cài đặt chương trình
- Chương 4. Kết quả và nhận xét
- Tài liệu tham khảo

---

## Danh mục bảng biểu

| Ký hiệu | Tên bảng |
|---|---|
| Bảng 1 | Phân công công việc |
| Bảng 2 | Bảng đánh giá nội dung đã hoàn thành |
| Bảng 3 | So sánh các phương pháp làm mờ ảnh |
| Bảng 4 | So sánh các kỹ thuật xác định biên ảnh |

---

# Chương 1. TỔNG QUAN BÀI THỰC HÀNH

## 1.1. Mục tiêu

Bài thực hành tập trung vào hai nhóm kỹ thuật xử lý ảnh cơ bản trong OpenCV: **làm mờ ảnh** và **xác định biên ảnh**. Mục tiêu chính là hiểu ý tưởng của từng giải thuật, cách áp dụng vào ảnh số và đánh giá sự khác nhau giữa các phương pháp thông qua kết quả trực quan.

Cụ thể, notebook thực hiện các nội dung sau:

- Đọc ảnh đầu vào `Lenna.jpg`, chuyển đổi định dạng màu để hiển thị đúng bằng Matplotlib.
- Chuyển ảnh màu sang ảnh xám để phục vụ các kỹ thuật xác định biên.
- Áp dụng ba phương pháp làm mờ ảnh: Averaging Blur, Gaussian Blur và Median Blur.
- Áp dụng bốn kỹ thuật xác định biên: Sobel, Laplacian, Laplacian of Gaussian và Canny.
- Lưu kết quả đầu ra vào thư mục `output/` để phục vụ so sánh và đánh giá.

## 1.2. Công cụ sử dụng

Các công cụ và thư viện chính được sử dụng trong notebook gồm:

- **Python**: ngôn ngữ lập trình chính.
- **Jupyter Notebook**: môi trường thực hiện thí nghiệm và trình bày kết quả.
- **OpenCV**: thư viện xử lý ảnh dùng để đọc ảnh, làm mờ ảnh và xác định biên.
- **NumPy**: hỗ trợ thao tác ma trận ảnh và tính toán số học.
- **Matplotlib**: hiển thị ảnh và so sánh kết quả trực quan.
- **Pillow**: hỗ trợ xử lý ảnh trong môi trường Python.

## 1.3. Nội dung thực hiện

Notebook được tổ chức theo bốn nhóm nội dung chính:

1. Chuẩn bị ảnh đầu vào.
2. Làm mờ ảnh bằng các bộ lọc smoothing.
3. Xác định biên ảnh bằng các toán tử gradient và phương pháp nhiều bước.
4. So sánh kết quả và đưa ra nhận xét.

---

# Chương 2. CƠ SỞ LÝ THUYẾT

## 2.1. Ảnh số

Ảnh số là ảnh được biểu diễn dưới dạng ma trận điểm ảnh. Mỗi điểm ảnh chứa giá trị cường độ sáng hoặc giá trị màu. Với ảnh xám, mỗi pixel thường có một giá trị cường độ trong khoảng từ 0 đến 255. Với ảnh màu, mỗi pixel thường gồm ba kênh màu, ví dụ RGB gồm Red, Green và Blue.

Trong OpenCV, ảnh màu khi đọc từ file thường có thứ tự kênh là BGR. Vì vậy, khi hiển thị bằng Matplotlib, ảnh cần được chuyển từ BGR sang RGB để màu sắc hiển thị đúng.

## 2.2. Làm mờ ảnh

Làm mờ ảnh là nhóm kỹ thuật làm giảm sự thay đổi cường độ cục bộ giữa các pixel lân cận. Mục đích chính là giảm nhiễu, làm mềm ảnh và hỗ trợ các bước xử lý sau như xác định biên hoặc phân đoạn ảnh.

Tuy nhiên, làm mờ ảnh cũng có thể làm mất chi tiết, đặc biệt là các đường biên nhỏ hoặc vùng có độ tương phản cao. Vì vậy, việc chọn bộ lọc phù hợp phụ thuộc vào loại nhiễu và mục tiêu xử lý.

### 2.2.1. Averaging Blur

Averaging Blur thay giá trị của mỗi pixel bằng giá trị trung bình của các pixel nằm trong một vùng lân cận. Đây là phương pháp đơn giản, dễ hiểu và dễ triển khai.

Ý tưởng chính:

- Dùng một cửa sổ lọc có kích thước cố định, ví dụ 5x5.
- Với mỗi pixel, lấy trung bình các pixel xung quanh.
- Gán giá trị trung bình đó cho pixel trung tâm.

Ưu điểm của phương pháp này là đơn giản và xử lý nhanh. Nhược điểm là làm mờ đều toàn ảnh nên dễ làm mất chi tiết biên.

### 2.2.2. Gaussian Blur

Gaussian Blur cũng làm mờ ảnh bằng vùng lân cận, nhưng các pixel gần tâm cửa sổ có trọng số lớn hơn các pixel ở xa tâm. Trọng số được xây dựng dựa trên phân phối Gaussian.

Ý tưởng chính:

- Tạo kernel Gaussian.
- Nhân từng pixel lân cận với trọng số tương ứng.
- Cộng các giá trị có trọng số để tạo ra giá trị mới cho pixel trung tâm.

Phương pháp này thường cho kết quả tự nhiên hơn Averaging Blur vì không xem tất cả pixel lân cận là quan trọng như nhau.

### 2.2.3. Median Blur

Median Blur thay giá trị của pixel trung tâm bằng trung vị của các pixel trong vùng lân cận. Khác với trung bình cộng, trung vị ít bị ảnh hưởng bởi các giá trị quá lớn hoặc quá nhỏ.

Ý tưởng chính:

- Lấy các pixel trong cửa sổ lân cận.
- Sắp xếp các giá trị pixel.
- Chọn giá trị trung vị làm giá trị mới cho pixel trung tâm.

Median Blur đặc biệt phù hợp khi ảnh có nhiễu muối tiêu, vì các điểm nhiễu thường là giá trị cực trị 0 hoặc 255.

## 2.3. Xác định biên ảnh

Biên ảnh là vùng có sự thay đổi cường độ sáng mạnh. Trong ảnh số, biên thường xuất hiện tại ranh giới giữa các vật thể, giữa vật thể và nền, hoặc giữa các vùng có màu sắc và ánh sáng khác nhau.

Các kỹ thuật xác định biên thường dựa trên đạo hàm bậc nhất hoặc đạo hàm bậc hai của ảnh:

- Đạo hàm bậc nhất giúp phát hiện hướng và độ mạnh của sự thay đổi cường độ.
- Đạo hàm bậc hai giúp phát hiện vùng có sự thay đổi đột ngột nhưng nhạy với nhiễu.

### 2.3.1. Sobel

Sobel là toán tử phát hiện biên dựa trên gradient ảnh. Phương pháp này tính sự thay đổi cường độ theo hai hướng ngang và dọc, sau đó kết hợp hai thành phần gradient để tạo bản đồ biên.

Ý tưởng chính:

- Tính gradient theo trục x để phát hiện biên dọc.
- Tính gradient theo trục y để phát hiện biên ngang.
- Kết hợp hai gradient để xác định độ mạnh biên.

Sobel có khả năng phát hiện hướng biên tốt và ít nhạy với nhiễu hơn một số toán tử đạo hàm đơn giản.

### 2.3.2. Laplacian

Laplacian sử dụng đạo hàm bậc hai để phát hiện vùng thay đổi cường độ nhanh. Phương pháp này không tách riêng hướng x và y mà phản ánh sự biến thiên tổng hợp của cường độ ảnh.

Ý tưởng chính:

- Tính đạo hàm bậc hai của ảnh xám.
- Các vùng có biến thiên mạnh sẽ tạo phản hồi lớn.
- Chuyển kết quả về miền giá trị hiển thị để quan sát biên.

Laplacian có ưu điểm là phát hiện biên theo nhiều hướng, nhưng nhược điểm là rất nhạy với nhiễu.

### 2.3.3. Laplacian of Gaussian (LoG)

LoG kết hợp Gaussian Blur và Laplacian. Ảnh được làm trơn bằng Gaussian trước để giảm nhiễu, sau đó mới áp dụng Laplacian để xác định biên.

Ý tưởng chính:

- Làm mờ ảnh xám bằng Gaussian Blur.
- Áp dụng Laplacian lên ảnh đã được làm trơn.
- Thu được bản đồ biên ổn định hơn so với Laplacian trực tiếp.

LoG giúp khắc phục một phần nhược điểm nhạy nhiễu của Laplacian.

### 2.3.4. Canny

Canny là phương pháp xác định biên nhiều bước, thường cho kết quả biên mảnh và rõ. Phương pháp này không chỉ tính gradient mà còn loại bỏ các điểm không phải cực đại và dùng hai ngưỡng để theo dõi biên.

Ý tưởng chính:

- Làm trơn ảnh để giảm nhiễu.
- Tính gradient và hướng biên.
- Loại bỏ các điểm không phải cực đại.
- Dùng hai ngưỡng để phân loại biên mạnh và biên yếu.
- Giữ lại các biên yếu nếu chúng nối với biên mạnh.

Canny thường cho kết quả tốt hơn về mặt trực quan, nhưng phụ thuộc vào việc chọn ngưỡng.

## 2.4. Thư viện OpenCV

OpenCV là thư viện mã nguồn mở phổ biến trong xử lý ảnh và thị giác máy tính. Trong bài thực hành này, OpenCV được dùng để đọc ảnh, chuyển đổi không gian màu, làm mờ ảnh, xác định biên và lưu ảnh kết quả.

OpenCV phù hợp cho bài thực hành vì cung cấp sẵn các hàm xử lý ảnh tối ưu, giúp người học tập trung vào việc hiểu bản chất thuật toán và đánh giá kết quả đầu ra.

---

# Chương 3. THIẾT KẾ VÀ CÀI ĐẶT CHƯƠNG TRÌNH

## 3.1. Môi trường thực hiện

Notebook được thực hiện trong môi trường Python và Jupyter Notebook. Ảnh đầu vào là `Lenna.jpg`, được đặt trong thư mục `images/`. Nếu ảnh chưa tồn tại, notebook tự tải ảnh từ URL đã cấu hình.

Kết quả sau khi xử lý được lưu vào thư mục `output/`, gồm các file:

- `01_averaging_blur.jpg`
- `02_gaussian_blur.jpg`
- `03_median_blur.jpg`
- `04_sobel_edge.jpg`
- `05_laplacian_edge.jpg`
- `06_log_edge.jpg`
- `07_canny_edge.jpg`

## 3.2. Chuẩn bị ảnh đầu vào

Ảnh đầu vào được đọc bằng OpenCV. Do OpenCV đọc ảnh màu theo thứ tự BGR, notebook chuyển ảnh sang RGB để hiển thị đúng bằng Matplotlib. Đồng thời, ảnh cũng được chuyển sang grayscale để sử dụng cho các kỹ thuật xác định biên.

### Pseudocode chuẩn bị ảnh

- Bước 1: Kiểm tra thư mục chứa ảnh đầu vào.
- Bước 2: Nếu ảnh chưa tồn tại, tải ảnh từ đường dẫn được cấu hình sẵn.
- Bước 3: Đọc ảnh bằng OpenCV.
- Bước 4: Nếu ảnh không đọc được, thông báo lỗi.
- Bước 5: Chuyển ảnh màu từ BGR sang RGB để hiển thị.
- Bước 6: Chuyển ảnh màu sang ảnh xám.
- Bước 7: Hiển thị ảnh gốc và ảnh xám để kiểm tra.

## 3.3. Averaging Blur

### 3.3.1. Ý tưởng

Averaging Blur dùng trung bình cộng của các pixel trong một vùng lân cận để thay thế pixel trung tâm. Trong notebook, kernel 5x5 được dùng để tạo hiệu ứng làm mờ vừa đủ và dễ so sánh với các phương pháp khác.

### 3.3.2. Pseudocode

- Input: ảnh màu RGB, kích thước kernel.
- Output: ảnh sau khi làm mờ bằng trung bình.
- Bước 1: Chọn kích thước kernel, ví dụ 5x5.
- Bước 2: Duyệt từng pixel trong ảnh.
- Bước 3: Lấy các pixel nằm trong vùng lân cận của pixel hiện tại.
- Bước 4: Tính trung bình các giá trị pixel trong vùng đó.
- Bước 5: Gán giá trị trung bình cho pixel tương ứng ở ảnh đầu ra.
- Bước 6: Lưu và hiển thị ảnh kết quả.

### 3.3.3. Hướng tiếp cận triển khai

Trong notebook, phương pháp này được triển khai bằng hàm làm mờ trung bình của OpenCV. Cách tiếp cận này giúp đảm bảo kết quả ổn định, ngắn gọn và đúng với ý tưởng thuật toán. Ảnh đầu ra được lưu với tên `01_averaging_blur.jpg`.

## 3.4. Gaussian Blur

### 3.4.1. Ý tưởng

Gaussian Blur làm mờ ảnh bằng cách dùng kernel Gaussian. Các pixel gần tâm có trọng số lớn hơn, còn các pixel ở xa tâm có trọng số nhỏ hơn. Vì vậy, ảnh sau khi làm mờ có cảm giác tự nhiên hơn so với Averaging Blur.

### 3.4.2. Pseudocode

- Input: ảnh màu RGB, kích thước kernel, độ lệch chuẩn Gaussian.
- Output: ảnh sau khi làm mờ bằng Gaussian.
- Bước 1: Chọn kích thước kernel, ví dụ 5x5.
- Bước 2: Xây dựng trọng số Gaussian cho từng vị trí trong kernel.
- Bước 3: Đặt kernel lên từng pixel của ảnh.
- Bước 4: Nhân các pixel lân cận với trọng số Gaussian tương ứng.
- Bước 5: Cộng các giá trị có trọng số để tạo giá trị mới cho pixel trung tâm.
- Bước 6: Lưu và hiển thị ảnh kết quả.

### 3.4.3. Hướng tiếp cận triển khai

Notebook sử dụng Gaussian Blur của OpenCV với kernel 5x5. Tham số độ lệch chuẩn được để OpenCV tự suy luận từ kích thước kernel. Ảnh đầu ra được lưu với tên `02_gaussian_blur.jpg`.

## 3.5. Median Blur

### 3.5.1. Ý tưởng

Median Blur dùng giá trị trung vị của các pixel trong vùng lân cận để thay thế pixel trung tâm. Phương pháp này không tính trung bình nên ít bị ảnh hưởng bởi các giá trị nhiễu cực trị.

### 3.5.2. Pseudocode

- Input: ảnh màu RGB, kích thước kernel.
- Output: ảnh sau khi lọc trung vị.
- Bước 1: Chọn kích thước kernel lẻ, ví dụ 5x5.
- Bước 2: Duyệt từng pixel trong ảnh.
- Bước 3: Lấy toàn bộ giá trị pixel trong vùng lân cận.
- Bước 4: Sắp xếp các giá trị pixel theo thứ tự tăng dần.
- Bước 5: Chọn giá trị nằm ở giữa làm giá trị mới của pixel trung tâm.
- Bước 6: Lưu và hiển thị ảnh kết quả.

### 3.5.3. Hướng tiếp cận triển khai

Notebook sử dụng Median Blur của OpenCV với kích thước kernel bằng 5. Phương pháp này phù hợp để minh họa khả năng làm mờ nhưng vẫn giữ biên tương đối tốt. Ảnh đầu ra được lưu với tên `03_median_blur.jpg`.

## 3.6. So sánh các phương pháp làm mờ ảnh

| Phương pháp | Đặc điểm | Ưu điểm | Hạn chế |
|---|---|---|---|
| Averaging Blur | Lấy trung bình đều các pixel trong kernel. | Đơn giản, dễ hiểu, xử lý nhanh. | Dễ làm mất chi tiết và làm mờ biên mạnh. |
| Gaussian Blur | Làm mờ bằng trọng số Gaussian. | Tự nhiên hơn Averaging, phù hợp tiền xử lý trước phát hiện biên. | Vẫn có thể làm mất chi tiết nhỏ. |
| Median Blur | Lấy trung vị trong vùng lân cận. | Hiệu quả với nhiễu muối tiêu, giữ biên tốt hơn. | Chi phí xử lý cao hơn do cần sắp xếp giá trị. |

## 3.7. Sobel Edge Detection

### 3.7.1. Ý tưởng

Sobel phát hiện biên bằng cách tính gradient theo hai hướng x và y. Gradient càng lớn thì khả năng pixel nằm trên biên càng cao. Trong notebook, hai thành phần gradient được kết hợp để tạo ảnh biên cuối cùng.

### 3.7.2. Pseudocode

- Input: ảnh xám.
- Output: ảnh biên Sobel.
- Bước 1: Nhận ảnh xám từ ảnh màu đầu vào.
- Bước 2: Tính gradient theo hướng x.
- Bước 3: Tính gradient theo hướng y.
- Bước 4: Kết hợp hai gradient để tính độ lớn biên.
- Bước 5: Chuẩn hóa giá trị biên về khoảng hiển thị.
- Bước 6: Lưu và hiển thị ảnh biên.

### 3.7.3. Hướng tiếp cận triển khai

Notebook dùng OpenCV để tính gradient Sobel theo hai hướng, sau đó dùng NumPy để tính độ lớn gradient. Kết quả được chuẩn hóa về miền 0 đến 255 để có thể quan sát như ảnh xám. Ảnh đầu ra được lưu với tên `04_sobel_edge.jpg`.

## 3.8. Laplacian Edge Detection

### 3.8.1. Ý tưởng

Laplacian phát hiện biên bằng đạo hàm bậc hai. Các vùng thay đổi cường độ đột ngột sẽ có phản hồi lớn, từ đó tạo ra bản đồ biên.

### 3.8.2. Pseudocode

- Input: ảnh xám.
- Output: ảnh biên Laplacian.
- Bước 1: Nhận ảnh xám từ ảnh màu đầu vào.
- Bước 2: Áp dụng toán tử Laplacian lên ảnh xám.
- Bước 3: Chuyển kết quả đạo hàm về dạng giá trị tuyệt đối.
- Bước 4: Chuẩn hóa hoặc chuyển kết quả về miền giá trị ảnh hiển thị.
- Bước 5: Lưu và hiển thị ảnh biên.

### 3.8.3. Hướng tiếp cận triển khai

Notebook sử dụng toán tử Laplacian của OpenCV với kernel kích thước 3. Do kết quả đạo hàm có thể chứa giá trị âm hoặc vượt ngoài miền hiển thị ảnh, notebook chuyển kết quả về dạng ảnh xám có thể quan sát được. Ảnh đầu ra được lưu với tên `05_laplacian_edge.jpg`.

## 3.9. Laplacian of Gaussian (LoG)

### 3.9.1. Ý tưởng

LoG là sự kết hợp giữa Gaussian Blur và Laplacian. Trước tiên, ảnh xám được làm trơn để giảm nhiễu. Sau đó, Laplacian được áp dụng lên ảnh đã làm trơn để phát hiện biên.

### 3.9.2. Pseudocode

- Input: ảnh xám, kích thước kernel Gaussian, kích thước kernel Laplacian.
- Output: ảnh biên LoG.
- Bước 1: Nhận ảnh xám từ ảnh màu đầu vào.
- Bước 2: Làm trơn ảnh xám bằng Gaussian Blur.
- Bước 3: Áp dụng Laplacian lên ảnh đã làm trơn.
- Bước 4: Chuyển kết quả về dạng giá trị tuyệt đối.
- Bước 5: Chuẩn hóa hoặc chuyển kết quả về miền hiển thị.
- Bước 6: Lưu và hiển thị ảnh biên.

### 3.9.3. Hướng tiếp cận triển khai

Notebook dùng Gaussian Blur với kernel 5x5 để làm trơn ảnh xám, sau đó áp dụng Laplacian. Cách triển khai này giúp giảm nhiễu trước khi tính đạo hàm bậc hai. Ảnh đầu ra được lưu với tên `06_log_edge.jpg`.

## 3.10. Canny Edge Detection

### 3.10.1. Ý tưởng

Canny là phương pháp xác định biên nhiều giai đoạn. So với Sobel và Laplacian, Canny thường tạo ra biên mảnh hơn, rõ hơn và ít nhiễu hơn nhờ bước loại bỏ điểm không cực đại và dùng hai ngưỡng.

### 3.10.2. Pseudocode

- Input: ảnh xám, ngưỡng thấp, ngưỡng cao.
- Output: ảnh biên Canny.
- Bước 1: Làm trơn ảnh để giảm nhiễu.
- Bước 2: Tính gradient và hướng gradient của ảnh.
- Bước 3: Loại bỏ các điểm không phải cực đại theo hướng gradient.
- Bước 4: Phân loại pixel thành biên mạnh, biên yếu hoặc không phải biên bằng hai ngưỡng.
- Bước 5: Giữ lại biên yếu nếu chúng liên thông với biên mạnh.
- Bước 6: Lưu và hiển thị ảnh biên cuối cùng.

### 3.10.3. Hướng tiếp cận triển khai

Notebook sử dụng phương pháp Canny của OpenCV với hai ngưỡng 100 và 200. Hai ngưỡng này giúp phân biệt vùng biên mạnh và vùng biên yếu. Ảnh đầu ra được lưu với tên `07_canny_edge.jpg`.

## 3.11. So sánh các kỹ thuật xác định biên

| Phương pháp | Cơ sở chính | Ưu điểm | Hạn chế |
|---|---|---|---|
| Sobel | Đạo hàm bậc nhất theo hướng x và y. | Phát hiện hướng biên tốt, kết quả dễ hiểu. | Biên còn dày, có thể giữ nhiều vùng gradient không thật sự sắc nét. |
| Laplacian | Đạo hàm bậc hai. | Phát hiện vùng thay đổi cường độ mạnh theo nhiều hướng. | Nhạy với nhiễu. |
| LoG | Gaussian Blur kết hợp Laplacian. | Ổn định hơn Laplacian nhờ giảm nhiễu trước. | Kết quả phụ thuộc kích thước Gaussian kernel. |
| Canny | Quy trình nhiều bước với hai ngưỡng. | Biên mảnh, rõ, trực quan nhất trong các phương pháp thử nghiệm. | Cần chọn ngưỡng phù hợp với từng ảnh. |

---

# Chương 4. KẾT QUẢ VÀ NHẬN XÉT

## 4.1. Kết quả nhóm làm mờ ảnh

Ba phương pháp làm mờ ảnh đều làm giảm chi tiết cục bộ trong ảnh. Averaging Blur tạo hiệu ứng mờ đều, Gaussian Blur cho kết quả mềm và tự nhiên hơn, còn Median Blur có xu hướng giữ lại đường biên tốt hơn trong khi vẫn làm giảm nhiễu.

Các file kết quả tương ứng:

- `output/01_averaging_blur.jpg`
- `output/02_gaussian_blur.jpg`
- `output/03_median_blur.jpg`

## 4.2. Kết quả nhóm xác định biên ảnh

Các kỹ thuật xác định biên cho kết quả khác nhau rõ rệt. Sobel cho thấy hướng biến thiên cường độ của ảnh. Laplacian làm nổi bật vùng thay đổi mạnh nhưng dễ nhạy với nhiễu. LoG cải thiện Laplacian bằng cách làm trơn trước khi phát hiện biên. Canny cho biên mảnh và rõ nhất, phù hợp khi cần bản đồ biên trực quan.

Các file kết quả tương ứng:

- `output/04_sobel_edge.jpg`
- `output/05_laplacian_edge.jpg`
- `output/06_log_edge.jpg`
- `output/07_canny_edge.jpg`

## 4.3. Nhận xét chung

Kết quả thực nghiệm cho thấy smoothing là bước tiền xử lý quan trọng trước nhiều bài toán thị giác máy tính. Trong đó, Gaussian Blur là lựa chọn cân bằng vì vừa giảm nhiễu vừa giữ được cảm giác tự nhiên của ảnh. Median Blur phù hợp hơn khi ảnh chứa nhiễu dạng điểm rời rạc.

Đối với xác định biên, Sobel và Laplacian giúp minh họa rõ nguyên lý đạo hàm trong ảnh số. Tuy nhiên, Canny cho kết quả thực tế tốt hơn nhờ kết hợp nhiều bước xử lý. LoG nằm giữa Laplacian và Canny, vì nó giảm nhiễu trước khi dùng đạo hàm bậc hai.

## 4.4. Kết luận

Bài thực hành đã hoàn thành hai yêu cầu chính: áp dụng các phương pháp làm mờ ảnh và áp dụng các kỹ thuật xác định biên ảnh. Thông qua notebook, có thể thấy mỗi thuật toán có mục tiêu và đặc điểm riêng. Averaging, Gaussian và Median phù hợp cho tiền xử lý ảnh, trong khi Sobel, Laplacian, LoG và Canny phù hợp để phân tích ranh giới và cấu trúc trong ảnh.

Trong các phương pháp đã thử nghiệm, Gaussian Blur là phương pháp làm mờ có tính cân bằng tốt, còn Canny là phương pháp xác định biên cho kết quả rõ ràng và dễ quan sát nhất.

---

# TÀI LIỆU THAM KHẢO

1. OpenCV Documentation, Image Filtering.
2. OpenCV Documentation, Image Gradients.
3. OpenCV Documentation, Canny Edge Detection.
4. Gonzalez, R. C., & Woods, R. E. Digital Image Processing.
