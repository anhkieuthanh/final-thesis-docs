# PHỤ LỤC M1b — BỘ MÔ HÌNH ĐÍCH VÀ NGÂN SÁCH API, TRÌNH GVHD KÝ

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Số liệu chi phí tính từ dữ liệu chạy thật đã lưu trong repo
> `ipi-agent-lab`; giả định ghi rõ ở từng dòng. Sinh viên rà lại trước khi trình.

**Đồ án:** Nghiên cứu và xây dựng hệ thống đánh giá, phòng chống tấn công tiêm nhiễm gián tiếp (Indirect Prompt
Injection) trên AI Agent dùng RAG + MCP tool-calling.

Mốc **M1b** (ND2 · Tuần 5): bộ model chốt + `v-models-1.0` · cost_budget hết TODO · hạn mức đã đặt · phụ lục GVHD ký.
Tài liệu này gom bằng chứng ba điều kiện đầu và là bản trình ký cho điều kiện thứ tư.

## 1. Tình trạng bốn điều kiện

| # | Điều kiện | Tình trạng | Bằng chứng |
|---|---|---|---|
| 1 | Bộ model chốt, khóa `v-models-1.0` | Đạt | Tag `v-models-1.0` tại commit `d84c9c4` (repo `ipi-agent-lab`). Từ tag tới nay ba `model_id` không đổi; chỉ đổi đường gọi A1 sang API trực tiếp (mục 2, điểm d) |
| 2 | Bảng giá hết TODO | Đạt phần đơn giá · **thiếu phần dự toán và trần** | Đơn giá ở `config/models.yaml`, không còn `null`. Bảng dự toán theo khối (checklist mục 5) còn trống — điền ở mục 3 dưới đây |
| 3 | Hạn mức đã đặt | Sinh viên tự xác nhận | `COST_BUDGET_USD_TOTAL` trong `.env` và hạn mức trên dashboard nhà cung cấp, đặt theo trần GVHD chốt ở mục 4. `src/obs/cost.py` từ chối mở lô khi biến này trống |
| 4 | Phụ lục GVHD ký | Chờ ký | Mục 5 |

## 2. Nội dung phụ lục điều chỉnh phạm vi

So với checklist W1 đã ký (5 kỹ thuật, bộ model cũ). Chi tiết ở `Chốt phạm vi và checklist ký GVHD.md`.

| # | Điều chỉnh | Nguồn |
|---|---|---|
| a | Tập kỹ thuật payload mở từ 5 lên **8** (thêm T6 chia mảnh, T7 kích hoạt trễ, T8 che giấu tiếng Việt), khóa `v-attack-1.0` | Checklist hạng mục 5 |
| b | Bộ mô hình đích: A1 `claude-opus-5` · A2 `glm-5.2` · A3 `glm-5.3-flash`, khóa `v-models-1.0` | Checklist hạng mục 6 |
| c | Thêm RQ6 với 2 harness × 3 model (HN-CC, HN-OW) | Checklist hạng mục 14 |
| d | A1 gọi thẳng Messages API của Anthropic, không qua gateway | `Xin ý kiến GVHD — họp kế tiếp.md` mục 1 |
| e | Thêm preset `d3_no_confirm` vào B2, B3, báo cáo dạng khám phá | Như trên, mục 2 |
| f | B2 có preset `off` đo lại cùng lô; RQ3 chọn cơ chế đơn lẻ tốt nhất trên toàn B2 | Như trên, mục 3 |
| g | Model sinh payload thích ứng (B5) và paraphrase: `claude-opus-5` | Checklist hạng mục 13 |
| h | Trần ngân sách API | Mục 4 dưới đây — **cần GVHD chốt** |

Các điểm d–f đã được GVHD duyệt miệng ngày 2026-10-21, chưa có bản ký; ký ở mục 5 thay cho bản ký đó.

## 3. Dự toán chi phí theo khối

### 3.1 Đơn giá mỗi run, đo thật

Nguồn: lô USR nền STT-37 `results/usr_baseline/usr-baseline-20261021T080837Z/` — 60 câu lành tính × 3 lặp × 3 model
= 540 run. Token trung bình mỗi run lấy từ bảng `runs` của `trace.sqlite`; đơn giá từ `config/models.yaml`.

| Model | Token vào / run | Token ra / run | USD / run |
|---|---:|---:|---:|
| A1 `claude-opus-5` | 9.293 | 783 | 0,0660 |
| A2 `glm-5.2` | 5.767 | 796 | 0,0174 |
| A3 `glm-5.3-flash` | 6.555 | 324 | 0,0045 |
| Judge `claude-sonnet-5-5` (mỗi run được chấm) | — | — | 0,0082 |

Chi phí judge suy từ `spent_usd` = 20,25 USD trong `manifest.json` trừ phần ba model đích.

### 3.2 Dự toán

Số run lấy từ checklist mục 5, giả định lập kế hoạch N = 30.

| Khối | Số run | Cách tính | Dự toán (USD) |
|---|---:|---|---:|
| B1 — nền tấn công | 3.780 | Chia đều A2, A3 | 41 |
| B2 — phòng thủ, tấn công | 5.040 | Chia đều A2, A3 | 55 |
| B3 — phòng thủ, lành tính | 4.200 | Chia đều A2, A3 + judge mọi run | 80 |
| B4 — xác nhận A1 | 500 | A1 | 33 |
| B5 — thích ứng | 900 | A2 + attacker opus-5 mỗi vòng (giả định 4.000 token vào, 512 token ra) | 45 |
| B6 — harness | 450 | 50 mẫu × 3 model × 3 nhánh + overhead system prompt harness (giả định 12.000 token × 4 bước cho mỗi run qua harness) | 50 |
| **Cộng** | **≈ 14.870** | | **≈ 305** |
| **Dự toán có hệ số an toàn 1,3** | | | **≈ 400** |

Giới hạn của dự toán:

- Đơn giá đo trên câu lành tính. Run tấn công dùng tác vụ chở và tài liệu chứa payload nên token vào có thể cao hơn;
  hệ số 1,3 dành cho phần này. Token/run thật của từng khối đo ở pilot (STT-60–62) và điền lại bảng trên.
- N = 30 là giả định; N thật quyết sau pilot ở M4. Chi phí B1–B3 tỉ lệ thuận với N.
- Overhead gateway của A2, A3 không ổn định theo thời gian (`Y_TUONG_DU_AN.md` mục 10.1); dự toán không cộng thêm.

## 4. Trần ngân sách — cần GVHD chọn

Checklist hạng mục 11 ghi trần **100 USD**. Dự toán ở mục 3 cho thấy trần này chỉ đủ khoảng một phần ba kế hoạch.
Ngay cả khi giảm N còn 10 cho B1, B2, giảm lặp B3 còn 2, bỏ B4, giảm một nửa B5 và B6, dự toán vẫn khoảng 145 USD
có hệ số an toàn.

| Phương án | Nội dung | Hệ quả |
|---|---|---|
| **PA1** | Nâng trần lên **400 USD**, giữ thiết kế phân khối | Đủ toàn bộ B1–B6 với N = 30 |
| **PA2** | Trần phân tầng: **tầng 1 = 60 USD** cho pilot + B1; sau pilot sinh viên trình lại dự toán B2–B6 bằng token/run thật | GVHD kiểm soát chi theo từng bước; thêm một lần duyệt sau M4 |
| **PA3** | Giữ **100 USD** | Phải cắt khối: bỏ B4 và B6 (mất RQ6 và tập xác nhận A1), N ≈ 10, CI rộng — RQ1, RQ2 nhiều khả năng chỉ báo cáo được xu hướng |

Đề xuất của sinh viên: **PA2**. Mọi phương án đều giữ quy tắc vận hành: kiểm chi phí mỗi 2 giờ trong 4 giờ đầu mỗi
lô, vượt 120% dự toán thì dừng.

## 5. Ký duyệt

| # | Hạng mục | Đồng ý | Sửa / ghi chú của GVHD |
|---|---|:---:|---|
| 1 | Bộ mô hình đích và `v-models-1.0` (mục 2 b, d) | ☐ | |
| 2 | Các điều chỉnh phạm vi mục 2 a, c, e, f, g | ☐ | |
| 3 | Dự toán chi phí mục 3 | ☐ | |
| 4 | Trần ngân sách: ☐ PA1 · ☐ PA2 · ☐ PA3 · ☐ khác: ______ USD | ☐ | |

|  | Sinh viên | Giáo viên hướng dẫn |
|---|---|---|
| Họ tên | Kiều Thành Anh | |
| Chữ ký | | |
| Ngày | | |
