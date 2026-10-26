# XIN Ý KIẾN GVHD — BUỔI HỌP KẾ TIẾP

> Tài liệu soạn với sự hỗ trợ của AI (Claude), sinh viên đã rà nội dung. GVHD đã duyệt mục 1–3 đúng đề xuất ngày
> 2026-10-21 (sinh viên báo lại; không lưu bản ký). Các nguồn chân lý và `Chốt phạm vi và checklist ký GVHD.md` đã đồng bộ
> theo mục 1–3. Mục 4 chờ ý kiến.

**Đồ án:** Nghiên cứu và xây dựng hệ thống đánh giá, phòng chống tấn công tiêm nhiễm gián tiếp (Indirect Prompt
Injection) trên AI Agent dùng RAG + MCP tool-calling.

---

## Mục 1. A1 gọi thẳng API của Anthropic, không qua gateway chung (VT-2)

**Bối cảnh.** Checklist đã ký (`Chốt phạm vi và checklist ký GVHD.md`, điều kiện harness, điểm 3 và 5) giả định cả ba
mô hình đích đi qua một gateway chung. Lần dò ngày 2026-10-13 cho thấy gateway chèn system prompt dài khoảng 5–12 nghìn
token của Claude Code vào **mọi** request tới A1. Mô hình tự nhận là "Claude Code" và nhắc tới các công cụ file, terminal,
web mà testbed không cấp. Như vậy số đo trên A1 qua gateway là hành vi của "Claude Opus 5 trong khung Claude Code", không
phải mô hình frontier trong cấu hình doanh nghiệp mà đề tài mô tả.

**Bằng chứng** (`ipi-agent-lab/results/smoke/`): `probe_gateway_identity_20261013T024118Z.json` (qua gateway, có bọc) và
`probe_gateway_identity_20261013T030241Z.json` (gọi thẳng: `prompt_tokens` khớp request, không có chỉ dẫn nào ngoài thứ
testbed gửi).

**Đề xuất.** A1 gọi thẳng Messages API của Anthropic; A2, A3 giữ gateway. Mã mô hình không đổi, nên `v-models-1.0` giữ
nguyên. Hạn chế #2 đã sửa lại: A2, A3 dùng chung hạ tầng, còn chênh lệch giữa A1 và A2/A3 có cả phần khác biệt hạ tầng.

**Nếu GVHD không đồng ý.** A1 quay lại gateway, và mọi số đo A1 phải khai là "đo trong khung Claude Code". Khi đó RQ về
lớp mô hình frontier mất ý nghĩa đại diện.

| Ý kiến GVHD | |
|---|---|
| ☑ Đồng ý · ☐ Không đồng ý · ☐ Ý kiến khác | |
| Ghi chú | |

---

## Mục 2. Thêm preset `d3_no_confirm` vào khối B2, B3 (VT-4)

**Bối cảnh.** D3 có luật R4 "yêu cầu xác nhận" cho mọi tool ghi hoặc gửi ra ngoài. Lab chạy tự động, không có người
bấm duyệt, nên yêu cầu xác nhận được quy về chặn (`automated_resolution: block`). Hệ quả: ở preset `d3_only`, D3 chặn
**mọi** `send_email`, `http_request`, `create_ticket`, kể cả hành động hợp lệ. ASR của D3 trên các bồn này gần 0 **theo
thiết kế**, FRR trên CT-05, CT-06 và nhóm U4 bằng 100%. Vì vậy không tách được hiệu lực của ba luật R1–R3, và đường
Pareto an toàn/hữu dụng của D3 suy biến.

**Đề xuất.** Thêm preset `d3_no_confirm` (D3 với R4 tắt; đã khai và kiểm trong `config/defenses.yaml`) vào B2 và B3:
6 → 7 preset. Kết quả của preset này báo cáo dạng **khám phá**, vì ma trận dự đoán `v-pred-1.0` đã ghi trước không có
dự đoán cho nó.

**Chi phí.** B2 tăng từ 4.320 lên 5.040 run, B3 từ 3.600 lên 4.200 run: tổng thêm 1.320 run, khoảng +17% số run của
hai khối (số theo `planned_runs` của `config/experiment.yaml`).

**Nếu GVHD không đồng ý.** Xóa preset, ghi thành hạn chế: "D3 chỉ đo với R4 chặn tự động; không tách được đóng góp của
R1–R3".

| Ý kiến GVHD | |
|---|---|
| ☑ Đồng ý · ☐ Không đồng ý · ☐ Ý kiến khác | |
| Ghi chú | |

---

## Mục 3. Hai điểm giao thức thực nghiệm lệch câu chữ checklist đã ký (VT-5)

**3a. B2 có thêm preset `off`, chạy cùng lô với 5 preset bật.** Checklist mục 5 tính B2 chỉ gồm các preset bật. Nếu
DSR của B2 so với `off` của B1 thì kết quả bị lẫn hai sai lệch: độ trôi của gateway theo thời gian, và độ lệch lên do
tập ô S_def được chọn đúng ở các ô có ASR cao nhất của B1. Kế hoạch STT-71 vốn đã ghi "OFF/D1/D2/D3/D4/ALL". Số run B2
theo `planned_runs` là 4.320, trùng con số của checklist.

**3b. RQ3 chọn cơ chế đơn lẻ tốt nhất trên toàn B2**, không trên "lượt pilot tách khỏi lượt đo" như checklist mục 4.
Không khối nào cung cấp lượt tách đó, và chia đôi dữ liệu thì mỗi nhánh chỉ còn khoảng 60 run cho mỗi mục tiêu G. Chọn
trên cùng dữ liệu làm cơ chế đơn lẻ có lợi thế giả, tức thiên lệch **ngược** giả thuyết H3, nên kết luận nghiêng về
thận trọng. Điểm này được khai trong báo cáo.

**Nếu GVHD không đồng ý.** (3a) bỏ `off` khỏi `blocks.B2.presets` và khai hai hạn chế trên. (3b) đổi
`blocks.B2.best_single.select_on` sang chia đôi theo băm `payload_id`.

| Ý kiến GVHD | 3a | 3b |
|---|---|---|
| ☑ Đồng ý · ☐ Không đồng ý · ☐ Ý kiến khác | ☑ | ☑ |
| Ghi chú | | |

---

## Mục 4. Hiệu chỉnh độ khó và tính tổng quát của tool khi thay model (STT-61)

**Bối cảnh.** Cổng hiệu chỉnh (quy tắc cứng #5) chọn mức "cả tin" của system prompt sao cho ASR pilot của A2, A3 nằm
trong 20–80%. Câu hỏi phản biện dễ gặp: thay model khác thì phải hiệu chỉnh lại, vậy tool còn ý nghĩa gì?

**Lập trường.** Hiệu chỉnh chỉnh môi trường, không chỉnh model. Ba núm (`calibration.allowed_knobs`) là cấu hình triển
khai có thật trong doanh nghiệp. Làm một lần, khóa sau vòng cuối; model khác chạy trên đúng môi trường đã khóa. ASR
dưới 20% trên model mới là kết quả ("kháng tốt trong lab này"), không phải lý do để chỉnh lại. Cổng tồn tại để đo được
delta phòng thủ: ở sàn ASR ≈ 0 thì không phân biệt được phòng thủ tốt với phòng thủ vô dụng.

**Thiên lệch còn lại.** Môi trường được chọn theo A2/A3, nên kết luận nghiêng về hai model này.

**Đề xuất (a), không đổi thiết kế.** Báo cáo ASR của mọi vòng hiệu chỉnh (`baseline`, `trusting`, `most_trusting`)
như một đường cong độ nhạy theo mức cả tin, không chỉ báo cáo cấu hình cuối. Quy tắc 3 của giao thức (`Y_TUONG_DU_AN.md`
mục 10.3) đã yêu cầu việc này. Chi phí: 0 run thêm ngoài các vòng hiệu chỉnh (mỗi vòng 243 run, khoảng 13–15 USD).

**Phương án (b), đổi thiết kế.** Đưa biến thể prompt thành một trục của ma trận B1–B3. Cách này không phụ thuộc model,
nhưng nhân số run của các khối đó lên khoảng 3–4 lần, và cần sửa `config/experiment.yaml`, `Mô tả bài toán` và checklist
đã ký.

**Nếu GVHD không đồng ý cả hai.** Giữ cổng như hiện tại, khai thành hạn chế: "môi trường hiệu chỉnh theo A2/A3; ASR
tuyệt đối trên model khác không so được".

| Ý kiến GVHD | |
|---|---|
| ☐ Đồng ý (a) · ☐ Đồng ý (b) · ☐ Không đồng ý · ☐ Ý kiến khác | |
| Ghi chú | |

---

| | Sinh viên | GVHD |
|---|---|---|
| Ngày | 2026-10-21 | 2026-10-21 |
| Hình thức | | Duyệt, sinh viên báo lại |
