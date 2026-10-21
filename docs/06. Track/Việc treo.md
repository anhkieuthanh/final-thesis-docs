# VIỆC TREO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Danh sách việc phát hiện trong lúc làm một đầu
> việc khác, chưa thuộc STT nào. Xử lý xong thì xóa mục khỏi file này và ghi kết quả vào
> `CHANGELOG_TAI_LIEU.md`.

Mỗi mục: phát hiện ở đâu · bằng chứng · hệ quả · phương án · hạn phải xong.

---

## VT-8 — TA soát mẫu kỹ thuật 5 cặp payload vi/en (STT-40 Bước 2 lô đầu)

- **Phát hiện ở đâu:** STT-40 Bước 2, lô đầu 5 cặp T1–T2 (commit lab `dfd0f59`).
- **Bằng chứng:** `ipi-agent-lab/src/attack/payloads/t1_explicit.yaml` (PR-T1-G2-001/002/003),
  `t2_override.yaml` (PR-T2-G1-001/002). Validator `[INV11]` đạt, nhưng validator chỉ kiểm hình
  thức — không bảo bản dịch giữ nguyên sức mạnh kỹ thuật.
- **Hệ quả:** nếu bản tiếng Việt làm nhẹ kỹ thuật, ASR tiếng Việt thấp giả tạo, kết luận ảnh
  hưởng ngôn ngữ sai (HUONG_DAN_DIEN_PAYLOAD.md mục 7).
- **Phương án:** TA soát cả 5 cặp (lô nhỏ, soát hết thay vì lấy mẫu 10%), chấm từng cặp "kỹ
  thuật còn nguyên / bị làm nhẹ" theo mục 7.4. Cặp bị làm nhẹ thì sửa bản vi rồi chạy lại
  `load_payloads`.
- **Hạn phải xong:** trước khi làm T3/T4/T5 (lô sau của STT-40, Tuần 11).
