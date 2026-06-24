# THỰC HÀNH 03: PHÁT HIỆN ĐỐI TƯỢNG VỚI YOLO, DETR VÀ FASTER R-CNN

## 1. Thông tin chung

Bài thực hành thuộc môn **Thị Giác Máy Tính Nâng Cao** (*Advanced Computer Vision - K35 - HCMUS*).

- Thành viên nhóm:
  - Nguyễn Trọng Hiếu – 25C11042 (Nhóm trưởng)
  - Trương Lê Bảo Trân – 25C11071
- Giảng viên hướng dẫn: ThS. Nguyễn Mạnh Hùng
- Chủ đề: **Object Detection** với ba mô hình **YOLOv8**, **DETR** và **Faster R-CNN**.

---

## 2. Mục lục

- [1. Thông tin chung](#1-thông-tin-chung)
- [2. Mục lục](#2-mục-lục)
- [3. Mục tiêu bài thực hành](#3-mục-tiêu-bài-thực-hành)
- [4. Tập dữ liệu sử dụng](#4-tập-dữ-liệu-sử-dụng)
- [5. Cấu trúc thư mục](#5-cấu-trúc-thư-mục)
- [6. Môi trường thực hiện](#6-môi-trường-thực-hiện)
- [7. Nội dung đã thực hiện](#7-nội-dung-đã-thực-hiện)
- [8. Hướng dẫn chạy notebook](#8-hướng-dẫn-chạy-notebook)
- [9. Kết quả đầu ra](#9-kết-quả-đầu-ra)
- [10. Kết quả thực nghiệm](#10-kết-quả-thực-nghiệm)
- [11. Nhận xét tổng quát](#11-nhận-xét-tổng-quát)
- [12. Tài liệu tham khảo](#12-tài-liệu-tham-khảo)

---

## 3. Mục tiêu bài thực hành

Bài thực hành tập trung vào bài toán **phát hiện đối tượng (Object Detection)**. Mục tiêu chính là huấn luyện, đánh giá và so sánh ba mô hình phát hiện đối tượng trên cùng một tập dữ liệu.

Các yêu cầu chính:

- Chọn tập dữ liệu phù hợp cho bài toán Object Detection.
- Mô tả chi tiết tập dữ liệu, nhãn, định dạng annotation và liên kết tải dữ liệu.
- Thực nghiệm với **YOLOv8** và **DETR**.
- Chọn thêm một mô hình khác ngoài YOLO và DETR, nhóm chọn **Faster R-CNN**.
- So sánh kết quả thực nghiệm giữa ba mô hình.
- Chuẩn bị notebook inference riêng cho YOLOv8, chạy bằng checkpoint đã huấn luyện và ảnh/zip tải bằng link, không mount Google Drive.

---

## 4. Tập dữ liệu sử dụng

Nhóm sử dụng **Safety Helmet Dataset** từ Roboflow Universe cho bài toán phát hiện mũ bảo hiểm trong ảnh.

### 4.1. Liên kết dữ liệu

- Dataset gốc: https://universe.roboflow.com/dataperson/safety-helmet-dataset-uvh1t
- Link reup Google Drive - định dạng YOLOv8: https://drive.google.com/file/d/1Ihd1CwR9k3XnLtFl7f2w8fNbKMEmZ7_k/view?usp=drive_link
- Link reup Google Drive - định dạng COCO: https://drive.google.com/file/d/1qHouId0FNqHbdBTdrj2kEpQHQT1wpEae/view?usp=drive_link

### 4.2. Thống kê dữ liệu

| Tập dữ liệu | Số lượng ảnh | Tỷ lệ |
|---|---:|---:|
| Train | 761 | 70% |
| Validation | 218 | 20% |
| Test | 109 | 10% |
| Tổng | 1088 | 100% |

### 4.3. Nhãn đối tượng

Dataset gồm ba lớp đối tượng:

| ID | Nhãn | Ý nghĩa |
|---:|---|---|
| 0 | Helmet | Mũ bảo hiểm |
| 1 | Head | Đầu người |
| 2 | Person | Người |

### 4.4. Định dạng dữ liệu

- **YOLOv8 format:** dùng cho notebook YOLOv8, mỗi ảnh đi kèm file `.txt` có dạng `class_id x_center y_center width height`.
- **COCO format:** dùng cho DETR và Faster R-CNN, annotation được lưu trong file `.json` theo chuẩn COCO.

---

## 5. Cấu trúc thư mục

Cấu trúc đề xuất khi nộp bài:

```text
source/
├── README.md
├── doc/
│   ├── NLP-K35_25C11042_25C11071_th03.docx
│   └── NLP-K35_25C11042_25C11071_th03.pdf
├── assets/
│   ├── input/
│   │   ├── helmet-1.jpg
│   │   ├── helmet-3.jpg
│   │   ├── helmet-4.jpg
│   │   ├── helmet-6.jpg
│   │   └── helmet-9.jpg
|   └── outputs/
|   |   └── yolov8_helmet_inference_outputs.zip
│   ├── YOLOv8.ipynb
│   ├── DETR.ipynb
│   ├── FasterRCNN.ipynb
│   └── TH03_YOLOv8_helmet_inference.ipynb
```
---

## 6. Môi trường thực hiện

- Python 3.11+
- Jupyter Notebook hoặc Google Colab
- GPU khuyến nghị cho huấn luyện
- PyTorch
- Torchvision
- Ultralytics YOLOv8
- Transformers
- PyCOCOTools
- TorchMetrics
- NumPy, Pandas, Pillow, Matplotlib, OpenCV

Cài đặt nhanh cho inference YOLOv8:

```bash
pip install ultralytics gdown opencv-python pandas pillow matplotlib
```

---

## 7. Nội dung đã thực hiện

| Nội dung | Mô tả | Trạng thái |
|---|---|---|
| Chuẩn bị dữ liệu | Tải và mô tả Safety Helmet Dataset | Hoàn thành |
| YOLOv8 | Huấn luyện, đánh giá validation/test, lưu checkpoint `best.pt` | Hoàn thành |
| DETR | Huấn luyện và đánh giá trên định dạng COCO | Hoàn thành |
| Faster R-CNN | Huấn luyện và đánh giá mô hình bổ sung ngoài YOLO/DETR | Hoàn thành |
| So sánh mô hình | So sánh kết quả YOLOv8, DETR và Faster R-CNN | Hoàn thành |
| Inference YOLOv8 | Chạy checkpoint đã train trên ảnh/zip đầu vào, không mount Drive | Hoàn thành |
| Báo cáo | Tổng hợp mô tả dữ liệu, lý thuyết, thực nghiệm, nhận xét | Hoàn thành |

---

## 8. Hướng dẫn chạy notebook

### 8.1. Huấn luyện và đánh giá

Chạy lần lượt các notebook sau nếu muốn tái lập quá trình thực nghiệm:

1. `YOLOv8.ipynb`
2. `DETR.ipynb`
3. `FasterRCNN.ipynb`

Các notebook này thực hiện tải dữ liệu, huấn luyện mô hình, đánh giá trên validation/test và lưu checkpoint tốt nhất.

### 8.2. Chạy inference YOLOv8

Notebook inference chính:

```text
src/TH03_YOLOv8_helmet_inference.ipynb
```

Các bước thực hiện:

1. Mở notebook trên Google Colab hoặc Jupyter Notebook.
2. Chỉnh `CHECKPOINT_URL` thành link checkpoint `best.pt` nếu cần.
3. Chỉnh `IMAGE_URLS` nếu muốn chạy một hoặc nhiều ảnh đơn lẻ.
4. Hoặc chỉnh `ZIP_URL` nếu muốn chạy inference trên file `.zip` chứa nhiều ảnh.
5. Run all cells.
6. Tải file kết quả `yolov8_helmet_inference_outputs.zip` ở cuối notebook.

Notebook inference không cần mount Google Drive. Tất cả file được tải bằng link thông qua `gdown` hoặc direct URL.

---

## 9. Kết quả đầu ra

Đầu vào của notebook inference có thể là:

- Một ảnh đơn lẻ từ link.
- Nhiều ảnh từ danh sách `IMAGE_URLS`.
- Một file `.zip` chứa ảnh, bounding box tham chiếu hoặc file `.csv` thông tin.

Đầu ra gồm:

| File/Thư mục | Ý nghĩa |
|---|---|
| `outputs/helmet_inference/` | Ảnh đã vẽ bounding box dự đoán |
| `outputs/helmet_inference/labels/` | File nhãn YOLO do model dự đoán |
| `prediction_boxes.csv` | Bảng kết quả dự đoán gồm tên ảnh, class, confidence và tọa độ bounding box |
| `yolov8_helmet_inference_outputs.zip` | File nén toàn bộ kết quả để tải xuống |

Các cột chính trong `prediction_boxes.csv`:

```text
image_name, object_id, class_id, class_name, confidence, x1, y1, x2, y2, box_width, box_height
```

---

## 10. Kết quả thực nghiệm

### 10.1. YOLOv8 trên tập Validation

| Chỉ số | Giá trị |
|---|---:|
| Precision | 0.859 |
| Recall | 0.835 |
| mAP@0.5 | 0.889 |
| mAP@0.5:0.95 | 0.454 |

### 10.2. YOLOv8 trên tập Test

| Chỉ số | Giá trị |
|---|---:|
| Precision | 0.83622 |
| Recall | 0.846 |
| mAP@0.5 | 0.887 |
| mAP@0.5:0.95 | 0.467 |

### 10.3. So sánh ba mô hình trên tập Test

| Mô hình | Recall | mAR@100 | mAP@50 | mAP@50:95 |
|---|---:|---:|---:|---:|
| YOLOv8 | 0.846 | - | 0.887 | 0.467 |
| Faster R-CNN | - | 0.4938 | 0.8059 | 0.4200 |
| DETR | - | 0.3567 | 0.5317 | 0.2681 |

---

## 11. Nhận xét tổng quát

YOLOv8 đạt kết quả tốt nhất trên bộ dữ liệu Safety Helmet với mAP@50 = 0.887 và mAP@50:95 = 0.467 trên tập Test. Mô hình có ưu điểm là tốc độ nhanh, pipeline đơn giản và phù hợp với bài toán cần inference nhanh.

Faster R-CNN đạt kết quả đứng thứ hai với mAP@50 = 0.8059, thể hiện lợi thế của kiến trúc hai giai đoạn trong việc định vị đối tượng. Tuy nhiên, mô hình thường chậm hơn YOLOv8 khi suy luận.

DETR có kiến trúc hiện đại dựa trên Transformer và cách tiếp cận end-to-end, nhưng trong thí nghiệm này kết quả thấp hơn hai mô hình còn lại. Nguyên nhân có thể đến từ yêu cầu dữ liệu lớn hơn, thời gian huấn luyện dài hơn và độ nhạy với cấu hình huấn luyện.

Tổng thể, YOLOv8 là lựa chọn phù hợp nhất trong phạm vi bài thực hành vì đạt cân bằng tốt giữa độ chính xác, tốc độ và tính dễ triển khai.

---

## 12. Tài liệu tham khảo

- Roboflow Universe - Safety Helmet Dataset: https://universe.roboflow.com/dataperson/safety-helmet-dataset-uvh1t
- Ultralytics YOLOv8 Documentation: https://docs.ultralytics.com/
- DETR: End-to-End Object Detection with Transformers: https://arxiv.org/abs/2005.12872
- Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks: https://arxiv.org/abs/1506.01497
- PyTorch Documentation: https://pytorch.org/docs/stable/index.html
- Torchvision Object Detection: https://pytorch.org/vision/stable/models.html#object-detection
