# Nháp RQ5 — độ bền của phòng thủ trước kẻ tấn công thích ứng (B5)

> Nháp làm việc cho báo cáo (Chương 5), do AI hỗ trợ soạn. Số liệu truy nguồn:
> `ipi-agent-lab/results/tables/arr_pareto_B5.csv`, `arr_B5_detail.csv`, sinh bởi
> `scripts/arr_pareto.py` từ B5 (`attack-B5-20261123T005114Z`), B2 (`attack-B2-20261119T023028Z`),
> B3 (`benign-B3-20261119T053354Z`). Còn treo tới khi TA duyệt đưa vào Overleaf.

## Câu hỏi và giả thuyết

**RQ5:** Phòng thủ còn hiệu quả bao nhiêu khi kẻ tấn công biết trước cơ chế và được viết lại
payload theo phản hồi bị chặn? **H5:** D1, D2 sụp gần hết; D3, D4 giữ được vì không phụ thuộc đọc
hiểu văn bản.

## Thiết lập

- Khối B5 chạy trên 3 ô S_adp — các ô mà phòng thủ **mù** mạnh nhất (DSR(blind) cao):
  K2a·T5·G1, K2a·T3·G2, K2a·T3·G3 — nên kết quả là độ bền **trong điều kiện khó nhất cho kẻ
  tấn công**, không phải trung bình toàn ma trận.
- Target A2 (glm-5.2), attacker thích ứng `glm-5.3`, ≤ 3 vòng/chuỗi, 5 chuỗi mỗi (ô × preset) =
  15 chuỗi/preset.
- DSR(adaptive) = 1 − ASR_e2e thích ứng (mức chuỗi: chuỗi tính "phòng thủ thắng" nếu không vòng nào
  đạt mục tiêu). DSR(blind) từ B2 (mức run). ARR = DSR(adaptive) / DSR(blind) — gần 1 = bền trước
  leo thang. ARR ở đây là **cận trên** của độ bền: attacker A-adaptive có thể yếu hơn kẻ tấn công
  thật (rủi ro 6).

## Kết quả (gộp 3 ô, A2)

| preset | DSR(adaptive) [CI 95%] | DSR(blind) | ARR | USR | FRR |
|---|---|---|---|---|---|
| d3_only | 0,867 [0,621–0,963] | 1,000 | 0,867 | 0,613 | 0,277 |
| all | 0,733 [0,481–0,891] | 1,000 | 0,733 | 0,613 | 0,294 |
| d1_only | 0,467 [0,248–0,699] | 0,633 | 0,737 | 0,908 | 0,000 |
| d4_only | 0,200 [0,071–0,452] | 0,333 | 0,600 | 0,857 | 0,000 |
| d2_only | 0,133 [0,037–0,379] | 0,267 | 0,500 | 0,900 | 0,000 |

CI 95% Wilson; n = 15 chuỗi/preset nên khoảng rộng — đọc là xu hướng, không phải điểm chính xác.

## Nhận định so với H5

- **D2 sụp nặng** (DSR thích ứng 0,133; ARR 0,500): khớp H5. D2 lọc cú pháp, kẻ tấn công viết lại
  diễn đạt để né.
- **D1 giảm mạnh** (DSR 0,467; ARR 0,737): một phần khớp "sụp gần hết" — còn giữ dưới nửa.
- **D3 giữ tốt nhất** (DSR 0,867; ARR 0,867 — mất ít hiệu lực nhất khi leo thang): khớp H5. D3 là
  chính sách gọi tool theo `task_type` chọn trước, không đọc hiểu văn bản payload nên khó né.
- **D4 KHÔNG giữ** (DSR thích ứng 0,200; ARR 0,600): **trái H5**. Trên các ô mạnh này, lọc egress
  bị kẻ tấn công thích ứng vượt — cần soi trace để biết D4 bị né bằng đường rò nào.
- **`all` thấp hơn `d3_only`** (0,733 < 0,867): gộp đủ D1–D4 không bền hơn mình D3 trên tập ô này;
  n nhỏ, cần thận trọng, nhưng đáng soi vì D3 là trụ cột độ bền.

## Pareto an toàn / hữu dụng

Trục an toàn = DSR(adaptive); trục hữu dụng = USR(A2) của B3. Biên Pareto (không bị trội):

- **d3_only** — góc an toàn: DSR 0,867 nhưng USR chỉ 0,613 (FRR 0,277, phí hữu dụng cao do cần
  xác nhận gọi tool).
- **d1_only** — góc hữu dụng: USR 0,908, FRR 0 nhưng DSR chỉ 0,467.

d2_only, d4_only, all đều bị trội: với mỗi cái có một preset khác an toàn ≥ **và** hữu dụng ≥.
Đáng chú ý `all` bị `d3_only` trội (cùng USR 0,613, D3 an toàn hơn) — thêm D1/D2/D4 vào D3 chỉ
tăng FRR (0,277 → 0,294) mà không thêm độ bền trên tập ô này.

**Kết luận RQ5:** Không phòng thủ đơn lẻ nào vừa bền trước leo thang vừa rẻ về hữu dụng. D3 bền
nhất nhưng đắt hữu dụng; D1 rẻ nhất nhưng bền kém; D2 sụp. Lựa chọn là đánh đổi trên biên
d1_only ↔ d3_only, không có "bữa trưa miễn phí". H5 đúng với D2 và D3, **sai với D4** trên tập ô
khó này.
