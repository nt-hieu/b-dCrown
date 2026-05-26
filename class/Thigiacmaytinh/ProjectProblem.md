# Đề cương nghiên cứu
**Phân lớp ảnh X-quang xương y khoa bằng Foundation Models: khảo sát, tái lập inference và đánh giá trên dữ liệu BTXRD**

# 1. Giới thiệu đề tài

Đề tài tập trung nghiên cứu bài toán phân lớp ảnh y khoa về xương, đặc biệt là ảnh X-quang xương, bằng các mô hình nền tảng đa phương thức như Medical Vision-Language Models — Med-VLM và Medical Multimodal Large Language Models — Med-MLLM.

Trọng tâm nghiên cứu không chỉ là huấn luyện một mô hình phân loại truyền thống, mà là khảo sát khả năng áp dụng các mô hình đã được tiền huấn luyện trên dữ liệu ảnh-văn bản y khoa vào các tác vụ như:

phân biệt ảnh xương bình thường và bất thường;
phân loại tổn thương hoặc khối u xương;
đánh giá khả năng zero-shot, few-shot và fine-tuning nhẹ;
so sánh workflow truyền thống với workflow dùng Foundation Model.

Dataset chính Bone Tumor X-ray Radiograph Dataset — BTXRD. Theo mô tả công bố, BTXRD gồm 3.746 ảnh X-quang xương, trong đó có 1.879 ảnh bình thường và 1.867 ảnh có khối u; dataset cũng có nhãn toàn cục, thông tin lâm sàng, mask và bounding box cho vùng tổn thương.

# 2. Các Ý nghĩa của đề tài
## 2.1. Ý nghĩa khoa học
Đề tài có ý nghĩa khoa học ở ba điểm chính.

Thứ nhất, nó giúp làm rõ khả năng chuyển giao tri thức của Foundation Model sang miền ảnh y khoa chuyên biệt. Các mô hình như MedCLIP được thiết kế để học liên kết giữa ảnh y khoa và văn bản y khoa, thay vì chỉ học nhãn phân loại cố định như CNN truyền thống. MedCLIP đề xuất cách học contrastive từ ảnh và văn bản không ghép cặp trực tiếp, đồng thời dùng semantic matching loss để giảm lỗi “false negative” trong dữ liệu y khoa.

Thứ hai, đề tài giúp đánh giá mức độ hiệu quả của các hướng zero-shot, few-shot và parameter-efficient fine-tuning. Paper CLIP-LoRA cho thấy LoRA có thể được dùng để thích nghi Vision-Language Model trong bối cảnh few-shot, giảm chi phí huấn luyện so với fine-tuning toàn bộ mô hình.

Thứ ba, đề tài tạo ra một workflow nghiên cứu có thể tái lập: từ khảo sát mô hình, chạy inference, đánh giá kết quả, đến phân tích lỗi trên dữ liệu ảnh xương. Đây là bước quan trọng nếu muốn phát triển tiếp thành một bài báo hoặc một benchmark nhỏ cho phân lớp ảnh X-quang xương.

## 2.2. Ý nghĩa ứng dụng
Về ứng dụng, đề tài có thể hỗ trợ xây dựng các hệ thống AI giúp sàng lọc sơ bộ ảnh X-quang xương, phát hiện ảnh có dấu hiệu bất thường và hỗ trợ bác sĩ trong quá trình đọc ảnh.

Trong bối cảnh dữ liệu y khoa thường ít, đắt và khó gán nhãn, các mô hình Foundation Model có tiềm năng vì có thể hoạt động ở chế độ zero-shot hoặc few-shot. Điều này phù hợp với các bài toán y khoa hẹp, nơi nhóm nghiên cứu không có đủ tài nguyên để huấn luyện một mô hình lớn từ đầu.

Tuy nhiên, kết quả của đề tài nên được trình bày theo hướng hỗ trợ nghiên cứu và hỗ trợ quyết định, không khẳng định thay thế chẩn đoán lâm sàng.

# 4. Survey: Workflow của bài toán image classification nói chung
## 4.1. Mục tiêu của bài toán classification

Bài toán classification không chỉ nhận ảnh làm đầu vào. Tùy loại dữ liệu, input có thể là ảnh, văn bản, âm thanh, bảng dữ liệu, tín hiệu y sinh, hoặc dữ liệu đa phương thức. Mục tiêu chung là ánh xạ input về một hoặc nhiều nhãn đầu ra đã được định nghĩa trước.

Ví dụ:
```txt
Image Classification      : ảnh -> nhãn lớp
Text Classification       : văn bản -> nhãn chủ đề/cảm xúc
Tabular Classification    : bảng dữ liệu -> nhãn dự đoán
Medical Classification    : ảnh + metadata -> nhãn bệnh lý
Multimodal Classification : ảnh + text + metadata -> nhãn phân loại
```

Workflow tổng quát có thể mô tả theo dạng chữ U, trong đó nhánh trái là quá trình chuẩn bị và học biểu diễn, đáy chữ U là mô hình học từ dữ liệu, còn nhánh phải là quá trình suy luận, kiểm định và diễn giải kết quả.

```txt
                [1] Problem Definition <-
               /                        |
              v                         |
 [2] Input Space                    [8] Output Space
     - image                            - predicted label
     - text                             - probability / confidence
     - tabular data                     - top-k classes
     - metadata                         - explanation if needed
              |                         ^
              v                         |
 [3] Label Space                    [7] Validation & Evaluation
     - binary class                     - accuracy
     - multi-class                      - precision / recall
     - multi-label                      - F1-score / AUROC
     - class hierarchy                  - confusion matrix
              |                         ^
              v                         |
 [4] Data Preparation              [6] Inference / Prediction
     - cleaning                         - forward pass
     - preprocessing                    - logits
     - augmentation                     - softmax / sigmoid score
     - train/val/test split             - decision threshold
              \                        ^
               v                      / 
                 [5] Model Training
                 - feature learning
                 - optimization
                 - loss minimization
                 - parameter update
```

## 4.2. Supervised CNN/ViT truyền thống

## 4.3. Zero-shot/Few-shot classification

# 7. Phát biểu lại bài toán nghiên cứu
## 7.1. Bài toán tổng quát

Cho một ảnh X-quang xương và các nhận đinh về bệnh có thể nhận định và ảnh ko phải nói về cùng 1 đối tượng, hệ thống cần dự đoán ảnh thuộc lớp nào trong tập nhãn y khoa đã định nghĩa trước.

## 7.2. Mục tiêu theo các cấp bậc
Input, output

<TODO: kẻ bảng nôi dung sau cho tôi>
Cấp 1: Hiểu mô hình và kỹ thuật

Nhóm cần hiểu các kỹ thuật chính:

Cấp 2: Chạy inference để xác nhận kết quả

Cấp 3: Nhận định trên kết quả hoặc dataset mới
# Timeline thực hiện
## Các tasks của project
- Khảo sát đề tài và tài liệu (Related work)
- Viết survey workflow
- Chuẩn bị dữ liệu
- Chạy 1 số baseline truyền thống (CNN/ViT hoặc pretrained ResNet) & Ghi nhận và đánh giá kết quả
- Zero-shot Med-VLM applied (inference với MedCLIP/BioMedCLIP) & Ghi nhận và đánh giá kết quả
- Few-shot adaptation applied (phân tích tính khả thi với tài nguyên hiện có)
- Đưa ra định hướng rõ hơn về nghiên cứu & Report

## Phân công thành viên
<TODO: kẻ bảng nội dung sau cho tôi>
25C11042-Nguyễn Trọng Hiếu 

phụ trách chính phần kỹ thuật:

- khảo sát MedCLIP, CLIP-LoRA;
- chuẩn bị code inference;
- chạy baseline;
- chạy zero-shot/few-shot;
- tổng hợp metric và bảng kết quả.

25C11071 — Trương Lê Bảo Trân

Phụ trách chính phần dữ liệu và báo cáo:

- khảo sát dataset BTXRD, MURA, MedMNIST;
- viết survey workflow;
- viết phần Foundation Model;
- hỗ trợ phân tích kết quả;
- hoàn thiện báo cáo và slide.

# Tài liệu tham khảo
- [Bone Tumor X-ray Radiograph Dataset — BTXRD](https://www.kaggle.com/datasets/thanhngan123/btxrd-data?resource=download)
- [2022 MedCLIP: Contrastive Learning from Unpaired Medical Images and Text](https://arxiv.org/abs/2210.10163)
- [2024 Low-Rank Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2405.18541)

