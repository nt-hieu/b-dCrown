# Proposal tổng quát

## Đề tài

**Phân lớp ảnh X-quang u xương bằng Foundation Model trong y khoa**

Đề tài tập trung nghiên cứu và xây dựng một framework tổng quát cho bài toán phân lớp ảnh X-quang xương, trong đó mô hình có nhiệm vụ hỗ trợ nhận diện ảnh bình thường, u xương lành tính và u xương ác tính. Hướng tiếp cận chính là khai thác các mô hình học sâu và Foundation Model trong y khoa, bao gồm CNN/ViT, Med-VLM và các kỹ thuật thích nghi tham số hiệu quả như LoRA/few-shot adaptation.

---

## 1. Bối cảnh và lý do chọn đề tài

Ảnh X-quang là một phương tiện chẩn đoán phổ biến trong y khoa vì chi phí thấp, dễ triển khai và được sử dụng rộng rãi trong đánh giá tổn thương xương. Tuy nhiên, việc phân biệt giữa ảnh bình thường, u xương lành tính và u xương ác tính vẫn là bài toán khó do đặc trưng hình ảnh có thể mờ, tổn thương nhỏ, hình thái bệnh đa dạng và chất lượng ảnh không đồng đều.

Trong kỷ nguyên AI, các mô hình Foundation Model có khả năng học biểu diễn tổng quát từ lượng dữ liệu lớn và có thể được chuyển giao sang nhiều tác vụ chuyên biệt. Với dữ liệu y khoa, hướng tiếp cận này có ý nghĩa vì dữ liệu gán nhãn thường ít, khó thu thập và cần chuyên gia xác nhận. Do đó, đề tài hướng đến việc xây dựng một quy trình tổng quát để áp dụng Foundation Model vào bài toán phân lớp ảnh X-quang u xương.

---

## 2. Mục tiêu nghiên cứu

### 2.1. Mục tiêu tổng quát

Xây dựng một framework tổng quát cho bài toán phân lớp ảnh X-quang u xương bằng các mô hình học sâu và Foundation Model, có khả năng vận hành qua hai giai đoạn chính: **offline phase** để huấn luyện, đánh giá và chọn mô hình; **online phase** để tiếp nhận ảnh mới, tiền xử lý, suy luận và trả kết quả phân lớp.

### 2.2. Mục tiêu cụ thể

1. Khảo sát workflow tổng quát của bài toán classification.
2. Phân tích đặc thù khi áp dụng classification vào ảnh y khoa.
3. Mô tả và đánh giá tập dữ liệu thử nghiệm BTXRD.
4. Xây dựng framework offline cho quá trình chuẩn bị dữ liệu, huấn luyện, đánh giá và chọn mô hình.
5. Xây dựng framework online cho quá trình nhận ảnh mới, tiền xử lý, inference và xuất kết quả.
6. So sánh các hướng tiếp cận: supervised CNN/ViT, zero-shot Med-VLM và few-shot LoRA.
7. Đánh giá thách thức, rủi ro và hướng phát triển của hệ thống.

---

## 3. Phát biểu bài toán

### 3.1. Bài toán tổng quát

Cho một ảnh X-quang xương đầu vào, hệ thống cần dự đoán ảnh đó thuộc một hoặc nhiều nhóm bệnh lý đã xác định. Trong phạm vi đề tài, bài toán ưu tiên được xem như bài toán **classification** trên ảnh X-quang u xương.

Tùy theo cách định nghĩa nhãn sau khi phân tích dữ liệu, bài toán có thể triển khai theo một trong ba dạng:

| Dạng bài toán | Ý nghĩa | Ví dụ trong X-quang u xương |
|---|---|---|
| Binary classification | Phân lớp 2 nhóm | Normal / Tumor |
| Multi-class classification | Mỗi ảnh thuộc đúng 1 lớp trong nhiều lớp | Normal / Benign / Malignant |
| Multi-label classification | Một ảnh có thể có nhiều nhãn cùng lúc | Có u, vị trí xương, loại tổn thương, mức độ nghi ngờ |

Trong đề tài này, hướng chính là **multi-class classification** với ba lớp: **Normal**, **Benign** và **Malignant**.

### 3.2. Input

Cần phân biệt hai khái niệm input: **input cho người dùng** và **input cho máy**.

#### Input cho người dùng

Input ở tầng người dùng có thể linh hoạt hơn:

- Ảnh X-quang mới.
- Metadata nếu có, ví dụ: tuổi, giới tính, vị trí giải phẫu, góc chụp.
- Ảnh có thể khác kích thước, định dạng, độ sáng, độ rõ hoặc chất lượng chụp.
- Metadata có thể thiếu hoặc không đồng nhất.
- Ảnh có thể đến từ nguồn ngoài miền dữ liệu huấn luyện.

#### Input cho máy

Input ở tầng mô hình phải cố định vì mô hình học sâu cần tensor đầu vào có cấu trúc xác định:

- Ảnh được resize về kích thước chuẩn, ví dụ 224×224 hoặc 384×384.
- Ảnh được chuẩn hóa theo mean/std phù hợp với backbone.
- Ảnh được chuyển về số kênh cố định, ví dụ grayscale 1 kênh hoặc RGB 3 kênh.
- Metadata nếu dùng phải được mã hóa thành vector số.
- Tensor đầu vào phải khớp với kiến trúc model đã chọn.

### 3.3. Output

Output của hệ thống online không chỉ là một nhãn đơn lẻ mà nên bao gồm:

| Thành phần output | Ý nghĩa |
|---|---|
| Predicted label | Nhãn dự đoán: Normal / Benign / Malignant |
| Confidence score | Độ tin cậy của dự đoán |
| Class probability | Xác suất cho từng lớp |
| Warning flag | Cảnh báo nếu độ tin cậy thấp hoặc ảnh ngoài miền dữ liệu |
| Optional explanation | Heatmap, Grad-CAM hoặc vùng ảnh mô hình chú ý nếu có triển khai |

Đối với hệ thống y khoa, output nên được hiểu là **công cụ hỗ trợ quyết định**, không thay thế kết luận của bác sĩ.

---

## 4. Mô tả tập dữ liệu thử nghiệm — BTXRD Dataset

Tập dữ liệu chính được sử dụng trong đề tài là **Bone Tumor X-ray Radiograph Dataset (BTXRD)**. Đây là bộ dữ liệu ảnh X-quang được xây dựng nhằm phục vụ các bài toán **classification**, **localization** và **segmentation** đối với u xương nguyên phát trên ảnh X-quang.

BTXRD được thu thập từ nhiều nguồn khác nhau, bao gồm:

- Ba bệnh viện tại Trung Quốc.
- Nền tảng Radiopaedia.
- Cơ sở dữ liệu MedPix.

Quy trình xây dựng dataset bao gồm: thu thập ảnh X-quang, chuyển đổi dữ liệu DICOM sang JPEG, loại bỏ thông tin định danh bệnh nhân, làm sạch dữ liệu và gán nhãn với sự hỗ trợ của chuyên gia chẩn đoán hình ảnh.

Sau quá trình làm sạch, BTXRD giữ lại **3.746 ảnh X-quang**, gồm:

| Lớp dữ liệu | Số lượng ảnh | Tỷ lệ xấp xỉ |
|---|---:|---:|
| Normal | 1.879 | 50,16% |
| Benign | 1.525 | 40,71% |
| Malignant | 342 | 9,13% |
| **Tổng** | **3.746** | **100%** |

Ngoài nhãn phân loại, mỗi ảnh có thể đi kèm metadata như tuổi, giới tính, vị trí giải phẫu và góc chụp. Với ảnh có u xương, dataset còn có thể có nhãn benign/malignant, subtype, vị trí tổn thương, bounding box và mask annotation.

BTXRD có tính đa dạng tương đối cao vì dữ liệu đến từ nhiều nguồn, nhiều vị trí xương, nhiều góc chụp và nhiều nhóm tuổi. Tuy nhiên, dataset cũng có thách thức rõ ràng là mất cân bằng lớp, đặc biệt số lượng ảnh **Malignant** thấp hơn đáng kể so với **Normal** và **Benign**.

Trong đề tài, dữ liệu cần được chia thành **train/validation/test** trước khi augmentation hoặc training để hạn chế **data leakage**. Nếu cùng một bệnh nhân, cùng một tổn thương hoặc các ảnh gần giống nhau xuất hiện ở cả train và test, kết quả đánh giá có thể bị ảo và không phản ánh đúng khả năng tổng quát hóa của mô hình.

---

## 5. Framework chung của hệ thống

Framework tổng quát cần bắt đầu từ việc **xác định bài toán trước dữ liệu**, sau đó mới đi vào phân tích dữ liệu, thiết kế mô hình, huấn luyện, đánh giá và triển khai.

```text
                    ┌──────────────────────────────┐
                    │  Xác định bài toán y khoa      │
                    │  - Input                       │
                    │  - Output                      │
                    │  - Dạng classification         │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────▼───────────────┐
                    │  Hiểu và kiểm tra dữ liệu      │
                    │  - Label                       │
                    │  - Metadata                    │
                    │  - Phân bố lớp                 │
                    │  - Bias / leakage              │
                    └──────────────┬───────────────┘
                                   │
        ┌──────────────────────────▼──────────────────────────┐
        │                  Offline phase                       │
        │  Split → Clean → Preprocess → Train → Validate/Test  │
        │  → Error analysis → Model selection → Export model   │
        └──────────────────────────┬──────────────────────────┘
                                   │
        ┌──────────────────────────▼──────────────────────────┐
        │                   Online phase                       │
        │  New image → Preprocess → Inference → Confidence     │
        │  → Output → Logging → Human review / feedback         │
        └─────────────────────────────────────────────────────┘
```

---

## 6. Framework giai đoạn offline

### 6.1. Mục tiêu của offline phase

Offline phase là giai đoạn hệ thống học từ dữ liệu đã có. Đầu ra chính của giai đoạn này không phải chỉ là một nhãn phân lớp, mà là một gói mô hình hoàn chỉnh có thể dùng cho inference.

Output của offline phase bao gồm:

- Mô hình đã huấn luyện.
- Trọng số model.
- Pipeline tiền xử lý.
- Ngưỡng quyết định.
- Báo cáo đánh giá.
- Phân tích lỗi.
- Cấu hình huấn luyện.
- Phiên bản dữ liệu và model.

### 6.2. Workflow offline phase

```text
Raw data
  │
  ▼
Problem definition
  │
  ├── Xác định input/output
  ├── Chọn dạng classification
  └── Xác định tiêu chí đánh giá
  │
  ▼
Data split
  │
  ├── Train
  ├── Validation
  └── Test
  │
  ▼
Data understanding & cleaning
  │
  ├── Kiểm tra ảnh lỗi
  ├── Kiểm tra ảnh trùng/gần trùng
  ├── Kiểm tra nhãn sai
  ├── Kiểm tra mất cân bằng lớp
  ├── Phân tích metadata
  └── Đánh giá bias theo nguồn dữ liệu
  │
  ▼
Preprocessing & feature representation
  │
  ├── Resize
  ├── Normalize
  ├── Crop/ROI nếu cần
  ├── Augmentation trên train set
  └── Embedding bằng CNN/ViT/Foundation Model
  │
  ▼
Training
  │
  ├── Supervised CNN/ViT
  ├── Zero-shot Med-VLM
  └── Few-shot LoRA/Adapter
  │
  ▼
Validation & model selection
  │
  ├── Accuracy
  ├── Precision
  ├── Recall
  ├── F1-score
  ├── AUC
  └── Confusion matrix
  │
  ▼
Error analysis
  │
  ├── Lỗi giữa benign/malignant
  ├── Lỗi do ảnh mờ
  ├── Lỗi do lệch miền dữ liệu
  └── Lỗi do mất cân bằng lớp
  │
  ▼
Export model package
```

### 6.3. Các điểm cần lưu ý trong offline phase

#### Chia dữ liệu trước khi augmentation

Dữ liệu phải được chia thành train/validation/test trước khi augmentation. Nếu augmentation được thực hiện trước khi chia dữ liệu, ảnh gốc và ảnh biến đổi có thể rơi vào các tập khác nhau, gây data leakage.

#### Data clean không chỉ là làm sạch

Data clean không chỉ là loại bỏ dữ liệu lỗi mà còn là quá trình hiểu dữ liệu. Cần phân tích:

- Ảnh lỗi hoặc không đọc được.
- Ảnh trùng hoặc gần trùng.
- Nhãn sai hoặc không nhất quán.
- Mất cân bằng lớp.
- Bias theo nguồn dữ liệu.
- Bias theo thiết bị chụp.
- Bias theo tuổi, giới tính, vị trí cơ thể.
- Sự phụ thuộc vào góc chụp hoặc điều kiện chụp.

#### Data máy hiểu nên gọi là tiền xử lý và biểu diễn đặc trưng

Thay vì gọi chung là “data máy hiểu”, nên dùng thuật ngữ chính xác hơn là **tiền xử lý và biểu diễn đặc trưng**. Với ảnh X-quang, bước này gồm resize, normalize, grayscale/RGB, augmentation, crop vùng quan tâm hoặc trích embedding bằng CNN, Vision Transformer hoặc Foundation Model.

#### Tách huấn luyện khỏi đánh giá lỗi

Huấn luyện là quá trình mô hình giảm loss trên train set. Đánh giá lỗi phải dựa trên validation/test set thông qua các chỉ số như accuracy, precision, recall, F1-score, AUC và confusion matrix. Trong y khoa, recall cho lớp bệnh thường quan trọng hơn accuracy vì bỏ sót bệnh có thể gây hậu quả nghiêm trọng.

#### Bổ sung dữ liệu do model tạo ra cần kiểm soát

Có thể dùng pseudo-labeling, active learning hoặc synthetic data, nhưng không nên đưa trực tiếp vào train set nếu chưa kiểm tra. Dữ liệu do model gợi ý nên được con người hoặc chuyên gia xác nhận, đặc biệt với bài toán y khoa.

---

## 7. Framework giai đoạn online

### 7.1. Mục tiêu của online phase

Online phase là giai đoạn hệ thống nhận dữ liệu mới và đưa ra dự đoán. Mục tiêu không phải là tiếp tục học ngay lập tức, mà là vận hành mô hình đã được chọn từ offline phase theo một pipeline ổn định, có kiểm soát và có khả năng ghi nhận phản hồi.

### 7.2. Workflow online phase

```text
Ảnh X-quang mới + metadata nếu có
  │
  ▼
Input validation
  │
  ├── Kiểm tra định dạng ảnh
  ├── Kiểm tra kích thước
  ├── Kiểm tra ảnh lỗi/ảnh quá mờ
  └── Kiểm tra metadata
  │
  ▼
Preprocessing
  │
  ├── Resize theo input size của model
  ├── Normalize theo cấu hình offline
  ├── Chuyển số kênh ảnh
  └── Mã hóa metadata nếu dùng
  │
  ▼
Inference
  │
  ├── CNN/ViT classifier
  ├── Med-VLM zero-shot classifier
  └── LoRA-adapted model
  │
  ▼
Post-processing
  │
  ├── Softmax/sigmoid probability
  ├── Áp dụng ngưỡng quyết định
  ├── Kiểm tra confidence
  └── Gắn cờ ảnh nghi ngờ/out-of-distribution
  │
  ▼
Output
  │
  ├── Nhãn dự đoán
  ├── Xác suất từng lớp
  ├── Cảnh báo nếu cần
  └── Giải thích tùy chọn
  │
  ▼
Logging & feedback
  │
  ├── Lưu input/output
  ├── Lưu confidence
  ├── Lưu lỗi người dùng/chuyên gia phản hồi
  └── Đưa case khó về offline phase
```

### 7.3. Vai trò của preprocessing trong online phase

Preprocessing trong online phase nhằm đảm bảo đầu vào mới khớp với thiết kế của model đã huấn luyện ở offline phase. Có thể hiểu đây là bước “đưa dữ liệu về đúng hướng dẫn sử dụng của model”. Nếu preprocessing online khác preprocessing offline, mô hình có thể suy luận sai dù bản thân model đã được huấn luyện tốt.

Các bước preprocessing cần nhất quán:

- Kích thước ảnh.
- Cách normalize.
- Số kênh ảnh.
- Cách crop hoặc padding.
- Cách mã hóa metadata.
- Thứ tự transform.
- Cấu hình prompt nếu dùng Med-VLM.

### 7.4. Output và kiểm soát rủi ro online

Với ảnh có confidence thấp, hệ thống không nên ép đưa ra kết luận chắc chắn. Thay vào đó, có thể trả về:

- Nhãn dự đoán chính.
- Confidence thấp.
- Cảnh báo cần chuyên gia xem lại.
- Đề xuất đưa ảnh vào tập phân tích lỗi.
- Ghi nhận để cải thiện offline phase.

---

## 8. Các hướng tiếp cận mô hình

### 8.1. Workflow 1 — Supervised CNN/ViT

Đây là hướng baseline truyền thống. Mô hình được huấn luyện có giám sát trên tập train đã gán nhãn.

```text
Ảnh X-quang → Preprocess → CNN/ViT → Classification head → Label
```

Ưu điểm:

- Dễ triển khai.
- Dễ đánh giá.
- Phù hợp làm baseline.
- Có thể đạt kết quả tốt nếu dữ liệu đủ và nhãn tốt.

Hạn chế:

- Cần nhiều dữ liệu gán nhãn.
- Dễ overfit nếu dữ liệu ít.
- Khả năng tổng quát hóa kém nếu dữ liệu lệch miền.
- Khó tận dụng tri thức ngôn ngữ y khoa nếu chỉ dùng ảnh.

### 8.2. Workflow 2 — Zero-shot classification bằng Med-VLM

Med-VLM sử dụng cả ảnh và mô tả văn bản. Thay vì huấn luyện lại toàn bộ mô hình, ta có thể thiết kế prompt để mô hình so khớp ảnh với các mô tả lớp.

```text
Ảnh X-quang → Image encoder
                         ├── Similarity → Label
Prompt lớp → Text encoder
```

Ví dụ prompt:

- “An X-ray image of normal bone.”
- “An X-ray image of benign bone tumor.”
- “An X-ray image of malignant bone tumor.”

Ưu điểm:

- Có thể thử nghiệm khi dữ liệu gán nhãn ít.
- Khai thác tri thức có sẵn của Foundation Model.
- Phù hợp để tạo baseline nhanh.

Hạn chế:

- Phụ thuộc mạnh vào chất lượng prompt.
- Foundation Model có thể chưa hiểu tốt miền ảnh X-quang u xương.
- Khả năng phân biệt benign và malignant có thể hạn chế.
- Cần kiểm tra kỹ với dữ liệu y khoa thực tế.

### 8.3. Workflow 3 — Few-shot LoRA/Adapter

Few-shot LoRA là hướng thích nghi Foundation Model bằng một lượng nhỏ dữ liệu gán nhãn. Thay vì fine-tune toàn bộ model, LoRA chỉ thêm các ma trận hạng thấp có thể học được vào một số tầng của mô hình.

```text
Pretrained VLM
  │
  ├── Freeze phần lớn trọng số
  ├── Thêm LoRA/Adapter
  ├── Fine-tune trên ít dữ liệu gán nhãn
  └── Xuất model thích nghi cho BTXRD
```

Ưu điểm:

- Ít tốn tài nguyên hơn full fine-tuning.
- Phù hợp khi dữ liệu y khoa hạn chế.
- Có thể cải thiện kết quả so với zero-shot.
- Giữ lại phần lớn tri thức nền của Foundation Model.

Hạn chế:

- Cần chọn vị trí gắn LoRA phù hợp.
- Dễ overfit nếu số mẫu few-shot quá ít.
- Cần kiểm soát learning rate, rank, số epoch.
- Kết quả phụ thuộc vào chất lượng dữ liệu mẫu.

---

## 9. Chiến lược đánh giá

### 9.1. Chỉ số đánh giá

Các chỉ số nên dùng:

| Chỉ số | Ý nghĩa |
|---|---|
| Accuracy | Tỷ lệ dự đoán đúng tổng thể |
| Precision | Trong các mẫu dự đoán là bệnh, có bao nhiêu mẫu đúng |
| Recall/Sensitivity | Trong các mẫu bệnh thật, mô hình phát hiện được bao nhiêu |
| Specificity | Khả năng nhận diện đúng mẫu không bệnh |
| F1-score | Trung hòa giữa precision và recall |
| AUC | Khả năng phân tách giữa các lớp |
| Confusion matrix | Phân tích loại nhầm lẫn giữa các lớp |

Với bài toán y khoa, cần chú trọng **recall của lớp Malignant** vì bỏ sót ác tính có rủi ro cao hơn so với cảnh báo nhầm.

### 9.2. Phân tích lỗi

Sau khi đánh giá, cần phân tích các nhóm lỗi:

- Normal bị dự đoán thành Benign/Malignant.
- Benign bị dự đoán thành Malignant.
- Malignant bị dự đoán thành Benign hoặc Normal.
- Lỗi ở ảnh mờ, nhiễu hoặc có artifact.
- Lỗi ở vị trí xương ít xuất hiện trong train set.
- Lỗi do thiếu metadata.
- Lỗi do lệch nguồn dữ liệu.

### 9.3. So sánh mô hình

Bảng so sánh dự kiến:

| Hướng tiếp cận | Dữ liệu cần dùng | Ưu điểm | Hạn chế | Vai trò trong đề tài |
|---|---|---|---|---|
| CNN/ViT supervised | Nhiều dữ liệu gán nhãn | Baseline rõ ràng | Dễ overfit | Mốc so sánh chính |
| Zero-shot Med-VLM | Không cần train hoặc rất ít train | Tận dụng tri thức nền | Phụ thuộc prompt | Baseline Foundation Model |
| Few-shot LoRA | Ít dữ liệu gán nhãn | Cân bằng hiệu quả và chi phí | Cần tinh chỉnh | Hướng cải thiện chính |

---

## 10. Các task cần thực hiện

| Nhóm task | Nội dung |
|---|---|
| Khảo sát | Tìm hiểu classification, medical image classification, Foundation Model, Med-VLM, LoRA |
| Dữ liệu | Tải BTXRD, kiểm tra cấu trúc, nhãn, metadata, phân bố lớp |
| Làm sạch dữ liệu | Kiểm tra ảnh lỗi, ảnh trùng, nhãn sai, mất cân bằng |
| Chia dữ liệu | Chia train/validation/test, hạn chế data leakage |
| Tiền xử lý | Resize, normalize, augmentation, crop/ROI nếu cần |
| Baseline | Huấn luyện CNN/ViT supervised |
| Zero-shot | Thiết kế prompt và đánh giá Med-VLM |
| Few-shot | Thử nghiệm LoRA/Adapter với số mẫu ít |
| Đánh giá | Accuracy, precision, recall, F1, AUC, confusion matrix |
| Phân tích lỗi | Tìm nhóm lỗi, nguyên nhân lỗi, case khó |
| Báo cáo | Viết proposal, mô tả framework, kết quả kỳ vọng và hướng phát triển |

---

## 11. Thách thức của đề tài

### 11.1. Thách thức của dữ liệu y khoa

- Dữ liệu gán nhãn cần chuyên gia.
- Ảnh có chất lượng không đồng đều.
- Dữ liệu mất cân bằng giữa các lớp.
- Tổn thương nhỏ hoặc khó quan sát.
- Benign và malignant có thể có đặc trưng hình ảnh giống nhau.
- Dữ liệu có thể bị bias theo nguồn chụp, thiết bị, tuổi, giới tính hoặc vị trí xương.

### 11.2. Thách thức của zero-shot Med-VLM

- Prompt ảnh hưởng lớn đến kết quả.
- Model có thể chưa được pretrain đủ tốt trên ảnh X-quang u xương.
- Khả năng suy luận y khoa của model cần kiểm chứng.
- Zero-shot có thể cho kết quả không ổn định khi lớp cần phân biệt quá chuyên biệt.

### 11.3. Thách thức của few-shot LoRA

- Số mẫu few-shot ít dễ gây overfit.
- Cần chọn hyperparameter phù hợp.
- Cần xác định gắn LoRA vào tầng nào của model.
- Cần so sánh công bằng với zero-shot và supervised baseline.

### 11.4. Thách thức tổng quát

- Tránh data leakage.
- Đảm bảo đánh giá phản ánh khả năng tổng quát hóa.
- Giải thích được dự đoán của mô hình.
- Kiểm soát rủi ro khi dùng trong y khoa.
- Không xem output của AI là kết luận thay thế chuyên gia.

---

## 12. Kết quả kỳ vọng

Đề tài kỳ vọng tạo ra:

1. Một framework tổng quát cho bài toán phân lớp ảnh X-quang u xương.
2. Một mô tả rõ ràng về offline phase và online phase.
3. Một pipeline thực nghiệm trên BTXRD.
4. Baseline supervised CNN/ViT.
5. Baseline zero-shot Med-VLM.
6. Hướng cải thiện bằng few-shot LoRA.
7. Báo cáo đánh giá bằng các chỉ số phù hợp với y khoa.
8. Phân tích lỗi và đề xuất hướng cải thiện.

---

## 13. Hướng phát triển

Các hướng phát triển sau proposal:

- Tích hợp metadata vào mô hình ảnh.
- Thử nghiệm multi-modal classification với ảnh và thông tin lâm sàng.
- Dùng Grad-CAM hoặc attention map để tăng khả năng giải thích.
- Thử active learning để chọn case khó cho chuyên gia gán nhãn.
- Thử pseudo-labeling nhưng phải có cơ chế kiểm duyệt.
- Mở rộng từ classification sang localization và segmentation.
- Kiểm tra khả năng tổng quát hóa trên dữ liệu ngoài BTXRD.

---

## 14. Bảng phân công dự kiến

| Thành viên | Nhiệm vụ chính | Sản phẩm đầu ra |
|---|---|---|
| Thành viên 1 | Khảo sát lý thuyết classification, Foundation Model, Med-VLM | Phần survey và cơ sở lý thuyết |
| Thành viên 2 | Phân tích BTXRD, tiền xử lý, chia dữ liệu | Mô tả dataset và pipeline dữ liệu |
| Thành viên 3 | Xây dựng baseline CNN/ViT | Kết quả baseline supervised |
| Thành viên 4 | Thử nghiệm zero-shot Med-VLM và few-shot LoRA | Kết quả Foundation Model |
| Cả nhóm | Đánh giá, phân tích lỗi, viết báo cáo | Proposal và báo cáo tổng hợp |

---

## 15. Timeline dự kiến

| Giai đoạn | Nội dung | Kết quả |
|---|---|---|
| Tuần 1 | Xác định bài toán, khảo sát tài liệu | Khung proposal |
| Tuần 2 | Phân tích BTXRD, chia dữ liệu | Dataset report |
| Tuần 3 | Xây dựng preprocessing và baseline CNN/ViT | Baseline result |
| Tuần 4 | Thử zero-shot Med-VLM | Zero-shot result |
| Tuần 5 | Thử few-shot LoRA/Adapter | Few-shot result |
| Tuần 6 | Đánh giá, phân tích lỗi, hoàn thiện báo cáo | Final report |

---

## 16. Kết luận

Proposal này định nghĩa bài toán phân lớp ảnh X-quang u xương theo hướng tổng quát, trong đó hệ thống được chia thành hai giai đoạn chính: offline phase để học, đánh giá và chọn mô hình; online phase để tiếp nhận ảnh mới, tiền xử lý, suy luận và trả kết quả. Điểm quan trọng của framework là phải xác định bài toán trước dữ liệu, chia train/validation/test trước khi augmentation, hiểu dữ liệu trước khi huấn luyện, đánh giá bằng các chỉ số phù hợp với y khoa và kiểm soát rủi ro khi bổ sung dữ liệu do model tạo ra.

Với tập dữ liệu BTXRD, bài toán có ý nghĩa thực nghiệm rõ ràng vì dataset có đủ nhãn Normal, Benign và Malignant, đồng thời có các đặc thù khó như mất cân bằng lớp, ảnh y khoa không đồng nhất và sự tương đồng hình ảnh giữa các loại tổn thương. Do đó, đề tài phù hợp để khảo sát vai trò của Foundation Model trong bài toán classification y khoa, đặc biệt là so sánh giữa supervised learning, zero-shot Med-VLM và few-shot LoRA.

---

## Tài liệu tham khảo

[1] S. Yao et al., “A Radiograph Dataset for the Classification, Localization, and Segmentation of Primary Bone Tumors,” *Scientific Data*, 2025. https://www.nature.com/articles/s41597-024-04311-y

[2] BTXRD Figshare Dataset. https://figshare.com/articles/dataset/A_Radiograph_Dataset_for_the_Classification_Localization_and_Segmentation_of_Primary_Bone_Tumors/27865398

[3] Z. Wang, Z. Wu, D. Agarwal, J. Sun, “MedCLIP: Contrastive Learning from Unpaired Medical Images and Text,” arXiv:2210.10163, 2022. https://arxiv.org/abs/2210.10163

[4] M. Zanella, I. Ben Ayed, “Low-Rank Few-Shot Adaptation of Vision-Language Models,” arXiv:2405.18541, 2024. https://arxiv.org/abs/2405.18541

[5] E. J. Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models,” arXiv:2106.09685, 2021. https://arxiv.org/abs/2106.09685
