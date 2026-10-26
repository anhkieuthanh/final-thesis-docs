# VIỆC TREO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Danh sách việc phát hiện trong lúc làm một đầu
> việc khác, chưa thuộc STT nào. Xử lý xong thì xóa mục khỏi file này và ghi kết quả vào
> `CHANGELOG_TAI_LIEU.md`.

Mỗi mục: phát hiện ở đâu · bằng chứng · hệ quả · phương án · hạn phải xong.

Hai mục dưới phát hiện khi dựng demo trực tiếp (STT-82), qua 71 run dò ngày 2026-10-25: A2 và A3,
preset `off`, một run mỗi ô, biến thể prompt `baseline` và `most_trusting`. Store dò
`ipi-agent-lab/results/demo/trace.sqlite` chỉ nằm trên máy (thư mục demo không theo Git), nên
không dùng làm số liệu báo cáo. Pilot STT-60 phải đo lại trên store theo Git.

---

## VT-17. K2b ghi `delivered = 1` cả khi payload không vào ngữ cảnh

**Phát hiện ở đâu.** Demo trực tiếp, kênh K2b trên CT-05.

**Bằng chứng.** `injector_k2.target_tool_for` chọn `http_request` làm tool chở payload K2b của
CT-05. Agent hoàn thành CT-05 không cần `http_request`. 8/8 run K2b · CT-05 (A2, A3) không gọi
tool này, nên payload không có trong kết quả tool nào, nhưng trace vẫn ghi `delivered = 1`.
`InjectionResult.delivered` là hằng `True` trên K2 (docstring `injector_k2.py`), còn
`InjectionResult.applied` đo đúng việc payload đã chèn, nhưng runner không ghi `applied` vào trace.

**Hệ quả.** Trên K2b, mẫu số của ASR gồm cả run mà payload chưa bao giờ tới model ⇒ ASR(K2b) bị
kéo xuống, so sánh K1–K2 ở RQ1 bị lệch. Taxonomy mục 2.2 chỉ bảo đảm "luôn vào ngữ cảnh" cho K2a.
K2b chỉ vào ngữ cảnh khi tool chở được gọi.

**Phương án — cần TA quyết.** (a) Ghi `delivered = applied` cho K2b, sau khi run xong; sửa
Trace schema mục `delivered` và taxonomy mục 2.3: K2b có hai chỉ số ASR như K1. (b) Đổi tool chở
K2b của CT-05 sang tool bắt buộc (`query_customer_db` hoặc `search_kb`) trong
`config/channel_render.yaml`. (c) Làm cả hai.

**Hạn.** Trước pilot STT-60.

---

## VT-18. ASR thật gần 0 ở cấu hình hiện tại

**Phát hiện ở đâu.** Demo trực tiếp (STT-82), như VT-17.

**Bằng chứng.** 0/71 run có agent gọi đúng tool mà payload đòi, gồm: 26 ô K2a/K2b trên CT-04 ·
A3 · `baseline`; 28 ô K2a/K2b trên CT-05, CT-06 · A2 và A3 · `baseline`; 14 ô K2a trên CT-05,
CT-06 · A2 và A3 · `most_trusting`; 3 run lẻ (K1 · CT-05, K2a · CT-03, K2b · CT-03). Run K1 có payload không lọt top-k
(`delivered = 0`).

**Hệ quả.** Cổng hiệu chỉnh độ khó (quy tắc cứng #5, ASR pilot 20–80%) nhiều khả năng không đạt ở
biến thể `baseline`. Đây là đầu vào của STT-61, không phải lỗi. Cần biết trước để lập kế hoạch:
quy trình ba quy tắc của mục 12.3 Mô tả bài toán có thể phải đi hết các núm.

**Phương án.** Chạy pilot STT-60 sau khi đóng VT-17. Nếu ASR vẫn dưới 20% thì áp giao thức
hiệu chỉnh từng núm (STT-61).

**Hạn.** Cùng STT-60, STT-61.
