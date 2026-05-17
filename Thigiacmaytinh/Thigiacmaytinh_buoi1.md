
- why following?
Mục đích: Thông minh hóa qui trình sản xuất và quảng lý xã hội trên thế giới ở diện rộng với nền tảng chuyển đổi số, trong đố TTNT giữ vai trò cốt lõi.

- Ans:
    - Thông minh hóa? 
        - định nghĩa: khả năng thích ứng với sự thay đổi
    - Thông minh hóa qui trình sản xuất?
    - Thông minh hóa qui trình quản lý xã hội?
    -> diện rộng:
        - phải diễn ra ở diện rộng:
            - ảnh hưởng tới cá nhân khi (do bị kéo xuống từ)
            - nguồn tiêu thụ phải có tiền
            - ký hợp tác với các đối tác bé
    -> chuyển đổi số
        - số hóa là 1 phần của chuyển đổi số (số hóa là chuyển đổi số liện từ dạng khác sang dạng số)
        - đi kèm với quy trình hoạt động tốt hơn trên nền tảng công nghệ số
        - VD: VNEID/ETAX/Grab mobile?
            - Grab so sánh hiệu quả truyền thống, quy mô, bài toán kinh tế, linh hoạt cho người dùng, <đưa thêm 3 lý do>?
            - Chuyển đổi số trong giáo dục?
    - Trí tuệ nhân tạo giữ vai trò quan trọng?

- Trong quy trình sản xuất và quản lý xã hội có dùng tới dữ liệu thị giác không?

- Ans:
    - ITS - Inf transportation system: Camera - store video -> hdl -> trace 
    - Nông nghiệp: detect bệnh cho cây trồng.

- Phân biệt 
    - Computer graphics - đồ họa máy tính:
        - Goal: mô phỏng thế giới thực - chưa có thật?
        - Input: 2d,3d 
        - Output: 2D filtering, 3D math rendering
        - lưu trữ: vector (dễ scale)
    - Image processing - xử lý ảnh
        - Goal: tăng cường chất lượng ảnh
        - Input: ảnh, video
        - Output: ảnh video được tăng cường
        - lưu trữ: pixel (các giá trị nguyên)
    - Computervision - thị giác máy tính
        - Goal: image/video understanding
        - Input: image/video/3d point cloud
        - Output: tạo image/video mới, hoặc trả về semantic
        - lưu trữ: metadata (dạng data) bất kỳ.

-> kẻ bảng 3 cái trên theo row, thêm 3 col Goal|Input|Ouput

Hiện thực ảo (Augmented reality) và hiện thực tăng cường (virtual reality)

tìm 1 ứng dụng xem xem có thực hiện các task nào dưới dây (dựa vào gold/input/output/task)
- object, scene, event
    - Detection
        - gold: Xác định vị trí của đối tượng trong ảnh
        - input: ảnh/video
        - output: bouding box
        - task: phát hiện sinh viên
    - Recognition
        - gold: Nhận biết được id của đối tượng
        - input: same
        - output: id của object
        - task: Điểm danh
    - Classification
        - gold: xác định lớp của object
        - input: same
        - output: class id
        - task: ???
    - Tracking
        - gold: Theo vết đối tượng trên nhiều camera <chọn ứng viên trong framet+1 gần vị trí với frame t> 
        - input: video
        - output: bounding bõ của đối tượng cần theo vết ở các frame
        - task: ???
    - Retrieval
        - gold: thu được tập các ảnh có độ tương đồng cao với ảnh query + ranking output
        - input: image/video
        - output: tập các ảnh có độ tương đồng cao với query.
        - task: ???
    - Counting
        - gold: đếm số người
        - input: ảnh/video
        - output: số người
        - task: ???
    - Generating
        - gold: tạo sinh nội dung mới
        - input: ảnh/video
        - output: ảnh/video mới
        - task: ???
