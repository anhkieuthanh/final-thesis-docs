# VIỆC TREO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Danh sách việc phát hiện trong lúc làm một đầu
> việc khác, chưa thuộc STT nào. Xử lý xong thì xóa mục khỏi file này và ghi kết quả vào
> `CHANGELOG_TAI_LIEU.md`.

Mỗi mục: phát hiện ở đâu · bằng chứng · hệ quả · phương án · hạn phải xong.

---

## VT-14 · Judge chỉ thấy kết quả tool bị cắt ở 3.000 ký tự

- **Phát hiện:** STT-37, soát tay lô `usr-baseline-20261021T080837Z` (lab `616679b`).
- **Bằng chứng:** hai ca TA kết luận "judge sai" (A1 BQ-U1-006, BQ-U1-008) đều có lý do judge "chi tiết không có trong
  kết quả công cụ… đã bị cắt". `config/prompts.yaml` khối `judge` đặt `max_tool_result_chars: 3000`; 348/511 run có
  judge (68%) có ít nhất một kết quả tool dài hơn (`search_kb` top-5 thường 3.300–7.900 ký tự). 18 run judge trượt nêu
  lý do kiểu này và có kết quả tool vượt ngưỡng (A1 10, A2 2, A3 6); 15 run trong đó dữ kiện cứng đạt — cận trên số run
  USR có thể đổi (ước bằng từ khóa trong `judge_reason`, chưa đo).
- **Hệ quả:** judge phạt câu trả lời đúng là "bịa"; USR thấp giả tạo, lệch nhiều nhất ở A1.
- **Phương án:** (a) nâng `max_tool_result_chars` đủ chứa top-5 (vd 12.000; `max_answer_chars` giữ), chấm lại `judge_pass`
  cho mọi run lô từ trace đã lưu — chỉ gọi judge, không gọi model đích (~511 lời gọi, ước 4–5 USD) — rồi chấm lại scorer,
  báo cả hai số; (b) chỉ chấm lại 18 run nghi ngờ — rẻ hơn nhưng chọn run theo kết quả đã thấy; (c) giữ, báo cáo hạn chế.
- **Hạn:** trước khi đưa số USR nền vào báo cáo.

## VT-15 · API tồn kho trả ngày cập nhật sau ngày tham chiếu

- **Phát hiện:** STT-37, soát tay dòng 5 (A2 BQ-U2-014).
- **Bằng chứng:** `ipi-agent-lab/config/tools.yaml` `http_request.params.inventory_updated_at = 2026-10-01T08:00:00+07:00`,
  sau `fixed.reference_date = 2026-08-06` mà system prompt đưa agent làm "hôm nay". Judge nêu điểm này làm lý do phụ
  để đánh trượt.
- **Hệ quả:** mọi câu hỏi tồn kho (CT-04, BQ-U2-010…014, BQ-U3-001…) có thể bị judge phạt vì một mâu thuẫn do testbed tạo.
- **Phương án:** đổi `inventory_updated_at` về trước `reference_date` (vd `2026-08-05T08:00:00+07:00`) trước pilot;
  `tools.yaml` vào `env_hash` nên lô sau mang hash mới. Lô USR nền giữ nguyên, ghi hạn chế.
- **Hạn:** trước pilot (STT-60).
