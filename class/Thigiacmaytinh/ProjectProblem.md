# Đề cương nghiên cứu

## Phân lớp ảnh X-quang xương y khoa bằng Foundation Models: khảo sát, tái lập inference và đánh giá trên dữ liệu BTXRD

---

# 1. Giới thiệu đề tài

Đề tài nghiên cứu bài toán **phân lớp ảnh X-quang xương** bằng các mô hình nền tảng đa phương thức, gồm **Medical Vision-Language Models (Med-VLM)** và **Medical Multimodal Large Language Models (Med-MLLM)**.

Trọng tâm của đề tài không chỉ là huấn luyện một mô hình phân loại truyền thống, mà là khảo sát khả năng áp dụng các mô hình đã được tiền huấn luyện trên dữ liệu ảnh-văn bản y khoa vào bài toán phân loại ảnh xương.

Các hướng chính:

- Phân biệt ảnh xương **bình thường** và **bất thường**.
- Phân loại ảnh có dấu hiệu **tổn thương hoặc khối u xương**.
- Đánh giá khả năng **zero-shot**, **few-shot** và **fine-tuning nhẹ**.
- So sánh workflow truyền thống với workflow dùng Foundation Model.

Dataset chính được sử dụng là **Bone Tumor X-ray Radiograph Dataset (BTXRD)**. Dataset này phù hợp với hướng nghiên cứu vì có ảnh X-quang xương, nhãn phân loại và có thể mở rộng sang các bài toán localization/segmentation nếu cần.

---

# 2. Ý nghĩa của đề tài

## 2.1. Ý nghĩa khoa học

Đề tài có ba ý nghĩa khoa học chính.

Thứ nhất, đề tài giúp đánh giá khả năng **chuyển giao tri thức** của Foundation Model sang miền ảnh y khoa chuyên biệt. Thay vì học trực tiếp từ nhãn cố định như CNN truyền thống, Med-VLM học quan hệ giữa ảnh y khoa và mô tả văn bản.

Thứ hai, đề tài khảo sát các hướng học hiện đại như **zero-shot**, **few-shot** và **parameter-efficient fine-tuning**. Đây là các hướng phù hợp với y khoa vì dữ liệu thường ít, khó thu thập và khó gán nhãn.

Thứ ba, đề tài tạo ra một workflow nghiên cứu có thể tái lập: khảo sát mô hình, chạy inference, đánh giá kết quả và phân tích lỗi trên ảnh X-quang xương.

## 2.2. Ý nghĩa ứng dụng

Về ứng dụng, đề tài có thể hỗ trợ xây dựng hệ thống AI giúp **sàng lọc sơ bộ ảnh X-quang xương**, phát hiện ảnh có dấu hiệu bất thường và hỗ trợ bác sĩ trong quá trình đọc ảnh.

Tuy nhiên, kết quả của đề tài nên được trình bày theo hướng **hỗ trợ nghiên cứu và hỗ trợ quyết định**, không khẳng định thay thế chẩn đoán lâm sàng.

---

# 3. Workflow tổng quát của bài toán Classification

## 3.1. Mục tiêu của bài toán Classification

Bài toán classification nhận một mẫu đầu vào `x` và dự đoán nhãn `y` thuộc một tập lớp đã định nghĩa trước.

Input không chỉ là ảnh. Tùy bài toán, input có thể là:

```txt
Image Classification      : ảnh -> nhãn lớp
Text Classification       : văn bản -> nhãn chủ đề/cảm xúc
Tabular Classification    : bảng dữ liệu -> nhãn dự đoán
Medical Classification    : ảnh + metadata -> nhãn bệnh lý
Multimodal Classification : ảnh + text + metadata -> nhãn phân loại
```

Phát biểu tổng quát:

```txt
Input  : x = một mẫu dữ liệu đơn phương thức hoặc đa phương thức
Model  : f(x)
Output : y = nhãn dự đoán thuộc tập lớp đã định nghĩa
```

---

## 3.2. Workflow cho bài toán Classification

Workflow classification có thể mô tả theo dạng **chữ U**. Nhánh trái là quá trình định nghĩa và chuẩn bị dữ liệu; đáy là huấn luyện mô hình; nhánh phải là suy luận, kiểm định và diễn giải output.

```txt
                 [1] Problem Definition
                /                       \
               v                         v
 [2] Input Space                    [8] Output Space
     - image                            - predicted label
     - text                             - probability score
     - tabular data                     - confidence score
     - metadata                         - top-k classes
     - multimodal input                 - explanation/heatmap
               |                         ^
               v                         |
 [3] Label Space                    [7] Validation & Evaluation
     - binary class                     - validation loss
     - multi-class                      - accuracy
     - multi-label                      - precision / recall
     - class hierarchy                  - F1-score / AUROC
               |                         ^
               v                         |
 [4] Data Preparation              [6] Inference / Prediction
     - cleaning                         - forward pass
     - preprocessing                    - logits
     - augmentation                     - softmax/sigmoid
     - train/val/test split             - threshold decision
                \                       /
                 v                     v
                  [5] Model Training
                  - feature learning
                  - loss minimization
                  - optimization
                  - parameter update
```

---

## 3.3. Giải thích các thành phần trong workflow

| Thành phần | Vai trò chính | Ví dụ trong bài toán ảnh xương |
|---|---|---|
| Problem Definition | Xác định bài toán cần giải | Phân loại Normal/Tumor |
| Input Space | Xác định dữ liệu đầu vào | Ảnh X-quang, metadata, prompt |
| Label Space | Xác định tập nhãn | Normal, Benign, Malignant |
| Data Preparation | Làm sạch và chuẩn hóa dữ liệu | Resize ảnh, chia train/val/test |
| Model Training | Huấn luyện hoặc thích nghi mô hình | CNN, ViT, MedCLIP, LoRA |
| Inference | Dự đoán trên mẫu mới | Tính xác suất từng lớp |
| Validation | Kiểm tra độ tin cậy mô hình | Accuracy, Recall, F1, AUROC |
| Output Space | Trả về kết quả cuối cùng | Nhãn, confidence, giải thích |

---

## 3.4. Validation cần đánh giá những gì?

Validation không chỉ trả về một con số accuracy. Trong classification, validation cần đánh giá cả **giá trị output**, **độ tin cậy** và **kiểu lỗi** của mô hình.

Input của validation gồm:

```txt
Validation set
Ground-truth labels
Model predictions
Probability scores
Decision threshold
Evaluation metrics
```

Output của validation nên gồm:

| Output validation | Ý nghĩa |
|---|---|
| Validation loss | Mức sai số của mô hình trên tập validation |
| Accuracy | Tỷ lệ dự đoán đúng tổng thể |
| Precision | Trong các mẫu dự đoán dương tính, có bao nhiêu mẫu đúng |
| Recall/Sensitivity | Trong các mẫu thật sự dương tính, mô hình phát hiện được bao nhiêu |
| F1-score | Cân bằng giữa precision và recall |
| AUROC | Khả năng phân biệt giữa các lớp ở nhiều threshold |
| Confusion matrix | Mô hình nhầm lớp nào sang lớp nào |
| Error cases | Các mẫu sai cần phân tích thủ công |

Với ảnh y khoa, **Recall/Sensitivity** đặc biệt quan trọng vì bỏ sót bệnh thường nguy hiểm hơn báo động sai.

---

# 4. Workflow Classification trong ảnh y khoa

## 4.1. Đặc điểm riêng của dữ liệu y khoa

Ảnh y khoa có nhiều đặc điểm khác ảnh tự nhiên:

- Dữ liệu ít và khó công khai.
- Nhãn cần chuyên gia y tế.
- Có thể lệch lớp nghiêm trọng.
- Một ảnh có thể cần metadata đi kèm.
- Lỗi false negative có rủi ro cao.
- Mô hình cần được đánh giá bằng nhiều metric, không chỉ accuracy.

Trong bài toán này, input không nên hiểu là “chỉ ảnh”. Khi dùng Med-VLM/Med-MLLM, input có thể gồm:

```txt
Ảnh X-quang xương
+ prompt văn bản mô tả lớp cần phân loại
+ metadata nếu có
+ vài mẫu labeled examples nếu dùng few-shot
```

---

## 4.2. Workflow 1: Supervised CNN/ViT truyền thống

Workflow này phù hợp khi có dữ liệu gán nhãn đủ lớn.

```txt
X-ray Images
    |
    v
Expert Labels
    |
    v
Train / Validation / Test Split
    |
    v
Preprocessing + Augmentation
    |
    v
CNN / ViT
    |
    v
Supervised Training
    |
    v
Prediction
    |
    v
Evaluation
```

Ưu điểm:

- Dễ triển khai.
- Dễ đánh giá.
- Phù hợp làm baseline.

Hạn chế:

- Cần nhiều dữ liệu gán nhãn.
- Khả năng tổng quát sang dataset mới có thể thấp.
- Ít tận dụng tri thức ngôn ngữ y khoa.

---

## 4.3. Workflow 2: Zero-shot Classification bằng Med-VLM

Workflow này dùng mô hình ảnh-văn bản đã tiền huấn luyện. Mô hình so sánh ảnh với các prompt mô tả lớp.

```txt
X-ray Image -----------------> Image Encoder ----                                                   > Similarity Score -> Predicted Class
Text Prompts -> Text Encoder --------------------/
```

Ví dụ prompt:

```txt
"a normal bone X-ray"
"an X-ray showing bone tumor"
"an X-ray showing benign bone lesion"
"an X-ray showing malignant bone tumor"
```

Ưu điểm:

- Không cần huấn luyện lại.
- Phù hợp để kiểm tra nhanh khả năng của Foundation Model.
- Có thể dùng khi dữ liệu gán nhãn ít.

Hạn chế:

- Phụ thuộc mạnh vào chất lượng prompt.
- Có thể kém ổn định nếu domain khác dữ liệu tiền huấn luyện.
- Cần đánh giá kỹ confidence và lỗi phân loại.

---

## 4.4. Workflow 3: Few-shot Adaptation bằng LoRA

Workflow này dùng một lượng nhỏ dữ liệu có nhãn để thích nghi mô hình.

```txt
Pretrained Med-VLM
    |
    v
Freeze Main Parameters
    |
    v
Insert LoRA Modules
    |
    v
Train on Few-shot Samples
    |
    v
Evaluate on Test Set
```

Ưu điểm:

- Ít tốn tài nguyên hơn fine-tuning toàn bộ mô hình.
- Phù hợp với dữ liệu y khoa ít nhãn.
- Có thể cải thiện so với zero-shot.

Hạn chế:

- Vẫn cần dữ liệu gán nhãn sạch.
- Cần chọn số shot và hyperparameter hợp lý.
- Cần kiểm tra overfitting.

---

# 5. Tổng quan về Foundation Models

Foundation Model là mô hình được tiền huấn luyện trên lượng dữ liệu lớn, sau đó có thể thích nghi cho nhiều tác vụ hạ nguồn.

Trong đề tài này, có ba nhóm mô hình chính:

| Nhóm mô hình | Đặc điểm | Vai trò trong đề tài |
|---|---|---|
| Vision Models | Chỉ xử lý ảnh | Làm baseline: CNN, ViT, ResNet |
| Med-VLM | Xử lý ảnh + văn bản | Zero-shot, prompt-based classification |
| Med-MLLM | Ảnh + ngôn ngữ + hội thoại | Sinh giải thích, hỗ trợ phân tích kết quả |

Quan hệ tổng quát:

```txt
Foundation Model
    |
    +-- Vision Model
    |      -> image classification
    |
    +-- Medical Vision-Language Model
    |      -> image-text matching, zero-shot classification
    |
    +-- Medical Multimodal LLM
           -> visual question answering, explanation, reasoning
```

---

# 6. Phát biểu lại bài toán nghiên cứu

## 6.1. Bài toán tổng quát

Cho một ảnh X-quang xương và các thông tin hỗ trợ nếu có, hệ thống cần dự đoán ảnh thuộc lớp nào trong tập nhãn y khoa đã định nghĩa trước.

Trong ngữ cảnh Vision-Language Model, input có thể gồm ảnh và các prompt văn bản mô tả giả thuyết bệnh. Prompt không nhất thiết là mô tả riêng của đúng bệnh nhân, mà có thể là mô tả đại diện cho từng class.

Phát biểu ngắn gọn:

```txt
Input:
    Ảnh X-quang xương
    + prompt văn bản nếu dùng VLM
    + metadata nếu có

Output:
    Nhãn phân loại
    + xác suất/confidence
    + top-k prediction
    + giải thích nếu mô hình hỗ trợ
```

---

## 6.2. Các mức độ bài toán

| Mức | Bài toán | Input | Output |
|---|---|---|---|
| Cơ bản | Binary classification | Ảnh X-quang | Normal / Tumor |
| Trung bình | Multi-class classification | Ảnh X-quang | Normal / Benign / Malignant |
| Mở rộng | Multimodal classification | Ảnh + prompt + metadata | Nhãn + confidence + giải thích |
| Nâng cao | Few-shot adaptation | Ảnh + vài mẫu có nhãn | Mô hình thích nghi tốt hơn |

---

## 6.3. Mục tiêu theo cấp bậc

| Cấp | Mục tiêu | Nội dung cần thực hiện | Kết quả đầu ra |
|---|---|---|---|
| Cấp 1 | Hiểu mô hình và kỹ thuật | Khảo sát classification, Med-VLM, Med-MLLM, MedCLIP, LoRA | Survey + workflow + bảng so sánh |
| Cấp 2 | Chạy inference xác nhận kết quả | Chạy baseline CNN/ViT và zero-shot Med-VLM | Metric ban đầu + nhận xét |
| Cấp 3 | Nhận định trên kết quả/dataset mới | Phân tích lỗi, so sánh workflow, đánh giá few-shot nếu khả thi | Kết luận nghiên cứu + hướng phát triển |

---

# 7. Đánh giá tiềm năng đề tài

Đề tài có tiềm năng nếu được định vị là một nghiên cứu **khảo sát và tái lập thực nghiệm** trên bài toán phân lớp ảnh X-quang xương.

Mức đóng góp chính:

- Xây dựng workflow rõ ràng cho bài toán bone X-ray classification.
- So sánh baseline truyền thống với Foundation Model.
- Kiểm tra khả năng zero-shot/few-shot trên dataset BTXRD.
- Phân tích lỗi và giới hạn của mô hình.
- Đề xuất hướng mở rộng sang localization/segmentation hoặc explanation.

Rủi ro chính:

- Mô hình zero-shot có thể cho kết quả thấp.
- Dataset có thể lệch lớp hoặc nhãn chưa đủ chi tiết.
- Tài nguyên tính toán có thể hạn chế khi fine-tuning.
- Kết quả không được diễn giải như chẩn đoán y khoa chính thức.

---

# 8. Timeline thực hiện

Thời gian dự kiến: **2.5 tháng**.

## 8.1. Các task chính của project

| Giai đoạn | Công việc | Kết quả cần có |
|---|---|---|
| Tuần 1 | Khảo sát đề tài và tài liệu liên quan | Tổng quan MedCLIP, LoRA, BTXRD |
| Tuần 2 | Viết survey workflow | Workflow classification và medical classification |
| Tuần 3 | Chuẩn bị dữ liệu | Thống kê dataset, split train/val/test |
| Tuần 4 | Chạy baseline truyền thống | Kết quả CNN/ViT hoặc ResNet |
| Tuần 5 | Chạy zero-shot Med-VLM | Kết quả MedCLIP/BioMedCLIP nếu khả thi |
| Tuần 6 | Phân tích few-shot adaptation | Đánh giá tính khả thi LoRA/few-shot |
| Tuần 7 | Tổng hợp và phân tích kết quả | Bảng metric, confusion matrix, error cases |
| Tuần 8-10 | Viết báo cáo và hoàn thiện | Report, slide, source code, kết luận |

---

## 8.2. Phân công thành viên

| Thành viên | Vai trò chính | Nhiệm vụ |
|---|---|---|
| 25C11042 — Nguyễn Trọng Hiếu | Kỹ thuật và thực nghiệm | Khảo sát MedCLIP/CLIP-LoRA; chuẩn bị code inference; chạy baseline; chạy zero-shot/few-shot; tổng hợp metric |
| 25C11071 — Trương Lê Bảo Trân | Dữ liệu và báo cáo | Khảo sát BTXRD, MURA, MedMNIST; viết survey workflow; viết phần Foundation Model; hỗ trợ phân tích kết quả; hoàn thiện báo cáo và slide |

---

# 9. Kết quả kỳ vọng

Kết quả cuối cùng của đề tài gồm:

- Một bản survey ngắn gọn về workflow classification và Foundation Model trong ảnh y khoa.
- Một pipeline thực nghiệm cho bài toán phân lớp ảnh X-quang xương.
- Kết quả baseline truyền thống.
- Kết quả zero-shot hoặc few-shot nếu triển khai được.
- Bảng đánh giá metric và phân tích lỗi.
- Báo cáo hoàn chỉnh có thể dùng làm nền tảng cho nghiên cứu tiếp theo.

Tóm tắt pipeline kỳ vọng:

```txt
BTXRD Dataset
    |
    v
Data Preparation
    |
    +--> CNN/ViT Baseline
    |
    +--> Zero-shot Med-VLM
    |
    +--> Few-shot LoRA if feasible
    |
    v
Evaluation
    |
    v
Result Analysis + Report
```

---

# 10. Tài liệu tham khảo

- [Bone Tumor X-ray Radiograph Dataset — BTXRD](https://www.kaggle.com/datasets/thanhngan123/btxrd-data?resource=download)
- [2022 MedCLIP: Contrastive Learning from Unpaired Medical Images and Text](https://arxiv.org/abs/2210.10163)
- [2024 Low-Rank Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2405.18541)
