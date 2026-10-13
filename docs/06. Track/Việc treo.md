# VIỆC TREO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Danh sách việc phát hiện trong lúc làm một đầu
> việc khác, chưa thuộc STT nào. Xử lý xong thì xóa mục khỏi file này và ghi kết quả vào
> `CHANGELOG_TAI_LIEU.md`.

Mỗi mục: phát hiện ở đâu · bằng chứng · hệ quả · phương án · hạn phải xong.

---

## VT-2. Gateway bọc A1 bằng system prompt riêng; A3 bị định tuyến qua nhiều upstream

**Phát hiện ở:** STT-19, lần dò tín hiệu từ chối; xác nhận bằng lần dò danh tính.

**Bằng chứng** (`ipi-agent-lab/results/smoke/`): `probe_refusal_20261013T012512Z.json` (30 lời gọi)
và `probe_gateway_identity_20261013T024118Z.json` (36 lời gọi, hỏi danh tính, nguồn chỉ dẫn, công
cụ; hai điều kiện: không system prompt và system prompt của testbed).

| Target | `prompt_tokens` so với request (~35–160 token) | Câu trả lời | Kết luận |
|---|---|---|---|
| A1 `claude-opus-5` | 5.300–12.900 token ở **mọi** lời gọi, hai mức (~5,4 nghìn và ~12 nghìn) | Tự nhận "Claude Code, CLI chính thức của Anthropic" ở cả hai điều kiện; kể có chỉ dẫn hệ thống chi tiết về đọc/sửa file, chạy lệnh terminal; không system prompt thì liệt kê công cụ file/terminal/web | **Có bọc.** Gateway chèn system prompt Claude Code dài vào mọi request A1 |
| A2 `glm-5.2` | Khớp request (35 → 35, 98 → 98) | Tự nhận GLM của Z.ai; với system prompt testbed thì nhận vai trợ lý nội bộ; nói không có chỉ dẫn nào khác | **Sạch** |
| A3 `glm-5.3-flash` | Thường khớp; có lúc dôi ~500 token cho cùng request (163 → 670, 72 → 566) | Như A2 | **Không ổn định.** `response_model` có 4 dạng (`glm-5.3-flash`, `z-ai/glm-5.3-flash`, `glm-5-3-flash`, rỗng); 1/36 lời gọi lỗi HTTP 400 — gateway phân tải qua nhiều nhà cung cấp, ít nhất một nơi chèn thêm nội dung |

**Hệ quả:**
- A1: mọi số đo trên A1 là hành vi của "Claude Opus 5 trong khung Claude Code + system prompt testbed",
  không phải model frontier trong cấu hình doanh nghiệp mà đề tài mô tả. Khung Claude Code có chỉ
  dẫn an toàn và phong cách riêng, nên ASR và tỉ lệ từ chối của A1 không đại diện cho A1. Nặng hơn hạn
  chế #2 và #13 (overhead token): đây không chỉ là token thừa mà là chỉ dẫn thay đổi hành vi.
- A3: hai run cùng tổ hợp có thể đi qua hai upstream khác nhau, thêm một nguồn phương sai không
  kiểm soát vào ô thí nghiệm.

**Phương án cho A1** (cần TA chọn; mọi phương án đổi phạm vi phải báo GVHD vì đụng `v-models-1.0`
và điều kiện "một gateway chung" đã ký):

| # | Phương án | Đổi gì | Đánh đổi |
|---|---|---|---|
| a | **Gọi A1 thẳng qua API của Anthropic** (đề xuất) | `.env` + `base_url_env`/`api_key_env` riêng cho khối A1 trong `models.yaml`; giữ `model_id: claude-opus-5` | Đo đúng model trần. A1 tách khỏi gateway chung — giảm chứ không tăng hạn chế #2. Cần khóa API riêng và chi phí trực tiếp |
| b | Hỏi nhà cung cấp gateway có endpoint/tham số tắt lớp bọc | Không đổi code nếu có | Phụ thuộc bên ngoài; phải dò lại để xác nhận đã tắt |
| c | Giữ nguyên, khai thành hạn chế | Thêm dòng vào `Y_TUONG_DU_AN.md` mục 16 và `01. Mô tả bài toán.md` | Không tốn công, nhưng A1 mất giá trị so sánh; RQ dùng A1 phải rút phạm vi kết luận |

**Phương án cho A3:**
1. Hỏi gateway có tham số ghim nhà cung cấp upstream không (kiểu định tuyến `provider` của các
   gateway tổng hợp). Có thì ghim một nơi, dò lại.
2. Không ghim được: trace đã ghi `response_model` — chuẩn hóa nhãn upstream, báo cáo tỉ lệ run theo
   upstream ở mỗi ô, và khai thành hạn chế.

**Hạn:** trước pilot (STT-60).
