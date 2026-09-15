# CHANGELOG TÀI LIỆU VÀ BỘ ĐO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude).

**Quy ước.** Các file kế hoạch, mô tả bài toán, thiết kế, bộ đo và thực nghiệm chỉ chứa
**bản hiện hành**: không nhãn phiên bản trong thân bài, không bảng đối chiếu "bản cũ → bản
mới", không dòng "Cập nhật ngày…", không ghi chú sửa đổi. Mọi lịch sử thay đổi ghi vào
chính file này, mục mới xếp **trên cùng**, mỗi mục gồm: ngày · file bị đổi · nội dung đổi ·
lý do. File dữ liệu `.json` cũng không chứa khối `changelog` — dữ liệu chỉ chứa dữ liệu.

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
