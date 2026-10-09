# Khảo sát bốn nhóm kỹ thuật phòng thủ IPI

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Đầu ra của STT-12 (ND2), đầu vào cho đặc tả D1–D4 ở STT-20 và mục 2.4 báo cáo.
> Tài liệu không chứa số liệu benchmark; mọi khẳng định về công trình khác có trích dẫn ở mục 4. TA kiểm lại từng trích dẫn từ bản PDF gốc trước khi đưa vào báo cáo.

Vị trí cắm dùng năm giai đoạn của `Y_TUONG_DU_AN.md` mục 7.1: (1) Gieo · (2) Nạp · (3) Kích hoạt · (4) Nhầm lẫn ranh giới · (5) Thi hành.

## 1. Bảng đối chiếu

| Nhóm | Cơ chế | Vị trí cắm | Điểm mù | Chi phí |
|---|---|---|---|---|
| **Lọc đầu vào** → D2 | Hai họ. (a) Biến đổi cú pháp tất định: chuẩn hóa Unicode, gỡ ký tự điều khiển và text ẩn, phát hiện khối mã hóa, regex mệnh lệnh. (b) Bộ dò học máy phân loại đoạn văn có chứa chỉ thị hay không [PromptGuard; DataSentinel] | Giai đoạn 2–3: trước khi chunk KB vào context và ngay khi tool-result trả về | Payload không có dấu hiệu cú pháp (T3, T5). Bộ dò mức chunk không thấy payload chia mảnh (T6). Bộ dò huấn luyện tiếng Anh yếu với tiếng Việt bỏ dấu, trộn mã (T8). Bộ dò học máy bị tấn công thích ứng vượt qua [zhan2025adaptive] | (a) Không tốn token, độ trễ cỡ ms, tái lập được. (b) Thêm một lượt suy luận mỗi chunk. Cả hai gây dương tính giả trên tài liệu chứa code/base64 hợp lệ (nhóm U5) |
| **Spotlighting** → D1 | Đánh dấu ranh giới dữ liệu/chỉ thị trong prompt: delimiting (bọc khối), datamarking (chèn ký hiệu giữa các từ), encoding (mã hóa base64) kèm chỉ thị "nội dung trong khối là dữ liệu" [hines2024spotlighting] | Giai đoạn 4: lúc ghép prompt, bọc mọi nội dung không tin cậy (chunk KB, mô tả tool, tool-result) | Hiệu lực phụ thuộc mức tuân thủ của model, tức xác suất, không bảo đảm. T5 không có chỉ thị nên không có gì để vô hiệu. Delimiter tĩnh bị giả mạo được, phải sinh ngẫu nhiên mỗi lượt. Yếu với T3 trên kênh mô tả công cụ (K2a) | Thêm token cố định mỗi khối; datamarking tăng token rõ hơn với tiếng Việt. Không thêm lượt gọi LLM. Encoding làm giảm chất lượng trả lời ở model yếu (ảnh hưởng A3) |
| **Kiểm soát chính sách gọi công cụ** → D3 | Kiểm tool-call ngoài LLM trước khi thi hành. Biến thể: allowlist công cụ theo tác vụ (tool filter) [debenedetti2024agentdojo]; tách luồng điều khiển khỏi luồng dữ liệu và gắn capability [CaMeL]; mẫu thiết kế plan-then-execute, action-selector [design-patterns]; so sánh với lần chạy lại đã che yêu cầu người dùng [MELON] | Giai đoạn 5: giữa lúc agent đề xuất tool-call và lúc tool thật thực thi | G3: trả lời sai lệch không cần tool-call nên không có gì để kiểm. Hành động nằm trong allowlist nhưng tham số hoặc nội dung bị thao túng (gửi email cho khách hợp lệ với nội dung sai). Tác vụ mở không biết trước bộ công cụ cần dùng | Máy trạng thái: độ trễ không đáng kể, không token. Chi phí thật là dương tính giả: chặn nhầm hành động ra ngoài hợp lệ (CT-05, CT-06, nhóm U4). CaMeL và MELON tốn thêm lượt LLM và công viết chính sách |
| **Lọc dữ liệu đầu ra** → D4 | Quét luồng ra trước khi rời vành đai: canary (honeytoken) thô và đã mã hóa, nhận diện PII [Presidio], domain ngoài allowlist, URL/ảnh markdown nhúng dữ liệu | Giai đoạn 5: ngay trước tool thuộc nhóm egress (`send_email`, gọi HTTP) và câu trả lời hiển thị cho người dùng | G2 nội bộ và G3: không có dữ liệu rời vành đai. Dữ liệu đã diễn đạt lại hoặc tóm tắt không còn mang canary. Phép mã hóa nằm ngoài danh sách đã biết. Chỉ thấy G1 khi dữ liệu ra mang dấu vết nhận diện được | Regex + NER: độ trễ cỡ ms, không token. Dương tính giả với email báo giá hợp lệ chứa thông tin khách (CT-05). Phải duy trì danh sách mã hóa và allowlist domain |

## 2. Ba nhận xét cho thiết kế D1–D4

1. **Hai nhóm đọc nội dung, hai nhóm đọc hành vi.** D1, D2 xét văn bản trước khi model suy luận; D3, D4 xét hành động sau khi model quyết định. Nhóm đầu thua khi payload không trông như chỉ thị (T5); nhóm sau thua khi tấn công không sinh hành động (G3). Đây là cơ sở của ô `T5 × G3` trong ma trận dự đoán (mục 7.3).
2. **Chỉ D1 phụ thuộc mức tuân thủ của model.** D2 (họ tất định), D3, D4 chạy ngoài LLM nên kẻ tấn công biết cơ chế vẫn phải đổi hành vi thật, không chỉ đổi câu chữ. Đây là cơ sở của giả thuyết H5.
3. **Chi phí chính không phải token mà là dương tính giả.** D3 và D4 rẻ về tính toán nhưng chặn nhầm đúng nhóm tác vụ có giá trị nhất (hành động ra ngoài hợp lệ). Vì vậy mỗi cấu hình phải đo kèm USR/FRR (giả thuyết H4).

## 3. Ánh xạ sang lựa chọn của đồ án

| Nhóm | Đồ án chọn | Không chọn, lý do |
|---|---|---|
| Lọc đầu vào | Họ (a) tất định, không dùng LLM | Họ (b) thêm lượt suy luận, khó tái lập, và đã có công trình đo; giữ làm đối chứng nếu còn giờ |
| Spotlighting | Delimiting với delimiter ngẫu nhiên mỗi lượt; datamarking là tùy chọn | Encoding: làm giảm hữu dụng ở A3 |
| Chính sách tool-call | Allowlist theo `task_type` người dùng chọn + `arg_constraints` | CaMeL, MELON: tốn thêm lượt LLM, vượt phạm vi đã ký; phân loại ý định tự do bị cấm (quy tắc cứng #3) |
| Lọc đầu ra | Canary thô và mã hóa, PII, allowlist domain | Bộ dò rò rỉ dựa trên LLM: không tất định |

## 4. Tài liệu tham khảo

Khóa trong ngoặc vuông trùng khóa BibTeX ở `docs/07. Báo cáo/refs_chuong1.bib` khi đã có; mục đánh dấu (*) cần thêm vào file `.bib`.

- [hines2024spotlighting] Hines và cs., *Defending Against Indirect Prompt Injection Attacks With Spotlighting*, 2024.
- [debenedetti2024agentdojo] Debenedetti và cs., *AgentDojo*, NeurIPS 2024 D&B.
- [zhan2025adaptive] Zhan và cs., *Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents*, 2025.
- [CaMeL] (*) Debenedetti và cs., *Defeating Prompt Injections by Design*, arXiv 2503.18813, 2025.
- [design-patterns] (*) Beurer-Kellner và cs., *Design Patterns for Securing LLM Agents against Prompt Injections*, arXiv 2506.08837, 2025.
- [MELON] (*) Zhu và cs., *MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents*, arXiv 2502.05174, 2025.
- [DataSentinel] (*) Liu và cs., *DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks*, arXiv 2504.11358, 2025.
- [PromptGuard] (*) Meta, Prompt Guard — model card trên Hugging Face (trích dạng `@misc`).
- [Presidio] (*) Microsoft, Presidio — thư viện nhận diện và ẩn danh PII, mã nguồn MIT (trích dạng `@software`).
