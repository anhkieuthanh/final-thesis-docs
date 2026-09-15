# CHANGELOG TÀI LIỆU VÀ BỘ ĐO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude).

**Quy ước.** Các file kế hoạch, mô tả bài toán, thiết kế, bộ đo và thực nghiệm chỉ chứa
**bản hiện hành**: không nhãn phiên bản trong thân bài, không bảng đối chiếu "bản cũ → bản
mới", không dòng "Cập nhật ngày…", không ghi chú sửa đổi. Mọi lịch sử thay đổi ghi vào
chính file này, mục mới xếp **trên cùng**, mỗi mục gồm: ngày · file bị đổi · nội dung đổi ·
lý do. File dữ liệu `.json` cũng không chứa khối `changelog` — dữ liệu chỉ chứa dữ liệu.

---

## 15/09/2026 — Viết lại mô tả bài toán

- Tạo `docs/01_de_bai/MO_TA_BAI_TOAN.md` (14 mục, đánh số liên tục) từ `Y_TUONG_DU_AN.md`.
- **Nguyên tắc tách phạm vi:** file này sở hữu bài toán, target lab, mô hình đe dọa, G1–G3, kênh K, bảng tổng quan T1–T9 và D1–D4, `blocked_by`, harness, mô hình đích, sáu RQ, nguyên tắc đo, phạm vi, đóng góp, hạn chế. Nó **không** nhắc lại: đặc tả từng kỹ thuật và ma trận dự đoán (`04_thiet_ke/payload_taxonomy.md`), đặc tả từng cơ chế phòng thủ (`04_thiet_ke/defense_spec.md`), lược đồ trace (`04_thiet_ke/trace_schema.md`), công thức từng chỉ số (`05_bo_do/metrics.md`), lịch và mốc (`02_ke_hoach/`). Mỗi khái niệm nằm đúng một chỗ.
- Ký hiệu dùng `TS1`–`TS3` cho tài sản, `A1`–`A3` cho mô hình đích, ngưỡng scorer 8/8 — thống nhất với `CLAUDE.md`.

**Còn lại của đợt tách:** `02_ke_hoach/KE_HOACH.md` · `02_ke_hoach/TASKS.md` · bốn file `04_thiet_ke/` · `05_bo_do/metrics.md`. Sau khi tách xong, `Y_TUONG_DU_AN.md` co lại thành bản điều hướng hai trang; **chưa làm trước khi các file đích tồn tại**, nếu không nội dung sẽ mất trong lúc chuyển.

---

## 15/09/2026 — Chốt ngưỡng kiểm chứng scorer 8/8

**Lý do.** Ngưỡng này từng tồn tại song song hai giá trị (6/6 và 8/8) ở hai tài liệu khác nhau, trong khi nó là cổng cứng chặn cả giai đoạn ma trận thực nghiệm.

- Chốt **8/8**, sai một ca là chưa đạt.
- `Y_TUONG_DU_AN.md`: thêm mục 12.5 định nghĩa cổng và **tám ca thử cụ thể** — con số không còn tuỳ tiện. Tám ca phủ bốn bồn chứa G1, hai điều kiện G2, ca âm `max_calls`, G3 không tool-call, và phân định `blocked_by`.
- `CLAUDE.md`: quy tắc cứng số 5 ghi rõ 8/8 và trỏ về mục 12.5 làm định nghĩa duy nhất.
- Đóng ba mục treo trong `Y_TUONG_DU_AN.md` mục 18: ngưỡng scorer 8/8 · báo cáo 6 chương · ký hiệu tài sản TS1–TS3.

---

## 15/09/2026 — Dựng lại workspace từ số không

**Lý do.** Cây tài liệu cũ tích tụ bốn lớp vấn đề không sửa lẻ được: ghi chú phiên bản lẫn
trong thân tài liệu, xung đột ký hiệu giữa các tài liệu, ngưỡng nghiệm thu tồn tại song song
hai giá trị, và số liệu trong lập luận không khớp dữ liệu thô. Chọn dựng lại thay vì vá.

- Xoá toàn bộ nội dung cũ của workspace, giữ lại `Y_TUONG_DU_AN.md` làm hạt giống.
- Dựng cây `docs/01_de_bai … 08_tham_khao`, `CLAUDE.md`, `README.md`, `.gitignore` mới.
- `git init` lại repo tài liệu. **Việc còn treo: tạo remote và push** — repo ngoài trước đây
  không có remote, nên toàn bộ tài liệu chỉ tồn tại một bản trên đĩa.
- Quyết định đã ghi vào `CLAUDE.md`: ký hiệu tài sản dùng `TS1`–`TS3`, tách khỏi `A1`–`A3`
  của mô hình đích; quy tắc cứng nâng lên 10 mục, thêm quy tắc tài liệu sạch.
- Mọi số liệu baseline trong `Y_TUONG_DU_AN.md` mục 12.3 đã đối chiếu lại từ CSV thô của
  lượt chạy tham chiếu, không lấy từ tài liệu trung gian.

**Dữ liệu đã mất cùng đợt xoá** (ghi lại để không ai đi tìm): lịch sử Git của repo tài liệu
cũ; `logs/w2_09_utility_api1.csv` và các file bằng chứng thô khác trong `logs/`; `.env`.
Bản sao mã nguồn trên remote GitHub của `ipi-agent-lab` không bị ảnh hưởng.
