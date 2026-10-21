# VIỆC TREO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Danh sách việc phát hiện trong lúc làm một đầu
> việc khác, chưa thuộc STT nào. Xử lý xong thì xóa mục khỏi file này và ghi kết quả vào
> `CHANGELOG_TAI_LIEU.md`.

Mỗi mục: phát hiện ở đâu · bằng chứng · hệ quả · phương án · hạn phải xong.

---

## VT-9 — TA soát mẫu kỹ thuật 5 cặp payload vi/en T3–T5 (STT-40 Bước 2 lô sau)

- **Phát hiện ở đâu:** STT-40 Bước 2, lô sau 5 cặp T3–T5 (commit lab `21df7de`).
- **Bằng chứng:** `ipi-agent-lab/src/attack/payloads/t3_prereq.yaml` (PR-T3-G1-001, PR-T3-G2-001),
  `t4_hidden.yaml` (PR-T4-G1-001/002), `t5_disguise.yaml` (PR-T5-G3-001). Validator `[INV11]` đạt,
  nhưng validator chỉ kiểm hình thức — không bảo bản dịch giữ nguyên sức mạnh kỹ thuật.
- **Hệ quả:** nếu bản tiếng Việt làm nhẹ kỹ thuật, ASR tiếng Việt thấp giả tạo, kết luận ảnh
  hưởng ngôn ngữ sai (HUONG_DAN_DIEN_PAYLOAD.md mục 7).
- **Phương án:** TA soát cả 5 cặp, chấm "kỹ thuật còn nguyên / bị làm nhẹ" theo mục 7.4. Lưu ý
  riêng: T4 kiểm phần ẩn (comment / zero-width) đúng là không hiển thị khi đọc thường; T5 kiểm
  payload không chứa câu mệnh lệnh nào. Cặp bị làm nhẹ thì sửa bản vi rồi chạy lại `load_payloads`.
- **Hạn phải xong:** trước khi khóa tập payload `v-attack-1.0` (sau khi xong T6–T8).
