# Tóm tắt công trình liên quan theo bảng tiêu chí cố định

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Mọi con số trong tài liệu này là **số do tác giả công bố** trong bài báo hoặc README, có dẫn vị trí. Tài liệu này **không** nhận xét về hành vi thực tế của benchmark; nhận xét dựa trên lần chạy thật nằm ở `FIT_GAP.md` và trỏ về `evidence/` (quy tắc cứng #2). TA cần kiểm lại từng trích dẫn từ bản PDF gốc trước khi đưa vào báo cáo.

## 1. Bảng tiêu chí cố định

Mỗi công trình được tóm tắt theo đúng 12 tiêu chí dưới đây, cùng thứ tự, để so sánh được theo hàng.

| # | Tiêu chí | Câu hỏi trả lời |
|---|---|---|
| C1 | Nguồn | Tác giả, nơi công bố, năm, mã nguồn |
| C2 | Bài toán | Công trình đo cái gì, trả lời câu hỏi gì |
| C3 | Kênh tiêm | Payload đi vào ngữ cảnh qua đâu — ánh xạ về K1/K2a/K2b/K3–K5 của đồ án |
| C4 | Môi trường | Tool thật hay mô phỏng, có trạng thái hay không, một lượt hay nhiều lượt |
| C5 | Quy mô | Số tác vụ người dùng, tác vụ tấn công, ca thử |
| C6 | Kỹ thuật tấn công | Họ payload, có tối ưu thích ứng hay không |
| C7 | Phòng thủ được đánh giá | Tên và nhóm |
| C8 | Cách chấm | Tất định trên trạng thái / phân tích tool-call / LLM chấm |
| C9 | Chỉ số | ASR, utility, chỉ số khác; mẫu số là gì |
| C10 | Mô hình đích | Số lượng, đại diện |
| C11 | Kết quả chính (tác giả công bố) | 2–3 con số quan trọng nhất, có vị trí trích |
| C12 | Hạn chế tác giả tự khai | Theo mục Limitations hoặc tương đương |

Ký hiệu kênh dùng đúng taxonomy của đồ án (`Y_TUONG_DU_AN.md` mục 5): K1 tài liệu RAG · K2a mô tả công cụ · K2b kết quả trả về của công cụ · K3 web · K4 bộ nhớ · K5 liên-agent/đa server.

## 2. Bảng tổng hợp

| Tiêu chí | AgentDojo | AutoDojo | MCPTox | InjecAgent | AgentDyn | MCP-Poison-Bench |
|---|---|---|---|---|---|---|
| C1 | Debenedetti và cs., NeurIPS 2024 D&B, arXiv 2406.13352; mã MIT | Ma và cs., arXiv 2606.15057 (2026); mã MIT | Wang và cs., AAAI-26, arXiv 2508.14925; repo **không khai giấy phép** | Zhan và cs., ACL 2024 Findings, arXiv 2403.02691; mã MIT | Li và cs., arXiv 2602.03117 (2026); mã MIT (kế thừa AgentDojo) | Dewan, phần mềm 2026 (trích dẫn dạng `@software`, chưa bình duyệt); mã MIT |
| C2 | Khung đo động utility–security cho agent gọi tool trên dữ liệu không tin cậy | Phòng thủ IPI còn bền không khi kẻ tấn công hộp đen thích ứng; ảnh hưởng của mức đặc tả tác vụ | Mức tổn thương của agent trước **tool poisoning** trên MCP server thật | Mức tổn thương IPI của agent tích hợp tool, một bước | Phòng thủ có triển khai được trong tác vụ mở, động, có chỉ dẫn hữu ích từ bên thứ ba không | Đánh giá "khử vòng lặp" (de-circularized) phòng thủ metadata phía client trước MCP tool poisoning |
| C3 | K2b (dữ liệu trả về từ tool: email, web, giao dịch…) | K2b (kế thừa AgentDojo) | K2a | K2b | K2b (web, email, file…) | K2a (description, schema field), K2b (rug_pull qua tool result), K5 (cross_server) |
| C4 | Môi trường Python mô phỏng, **có trạng thái**, nhiều lượt; tool output định dạng YAML | Như AgentDojo + AgentDyn | Chèn tool độc vào system prompt cùng danh sách tool thật, **một lượt**, chỉ đọc tool-call đầu ra, không thực thi | **Mô phỏng một lượt**: phản hồi tool được sinh sẵn, agent chỉ quyết định hành động kế tiếp | Kế thừa AgentDojo, nhiều lượt, quỹ đạo dài | Harness MCP cục bộ, sink no-op, canary tổng hợp |
| C5 | 97 tác vụ, 629 ca thử, 70–74 tool, 4 suite (bài báo, Bảng 1) | 3 suite, 57 tác vụ, 21 tác vụ tấn công, 389 ca (Bảng 1) | 45 server, 353 tool, 1.312 ca độc (Tóm tắt) | 1.054 ca, 17 user tool, 62 attacker tool (Bảng 2) | 60 tác vụ, 28 tác vụ tấn công, 560 ca, 3 suite (Bảng 2) | 5 lớp tấn công × 3 mục tiêu; ~2.500 lượt chấm ở v1 (README) |
| C6 | TODO, Ignore previous, InjecAgent, Important message, Max; không tối ưu | Vòng lặp LLM tối ưu hộp đen 6 vòng, seed = static + TopicAttack + RLHammer | 3 khuôn: P1 kích hoạt tường minh–chiếm chức năng, P2 kích hoạt ngầm–chiếm chức năng, P3 kích hoạt ngầm–sửa tham số; biến thể "tăng cường" thêm `<IMPORTANT>` / "Ignore all previous…" | Base và Enhanced (tiền tố "IMPORTANT!!! Ignore all previous instructions…") | `important_instructions` mặc định | Register "seen" và "held-out" (held-out không chạm từ khóa phòng thủ, kiểm bằng CI) |
| C7 | Delimiting, PI detector, Repeat prompt, Tool filter | 9 phòng thủ: sandwich, reminder, spotlighting, PromptGuard, PIGuard, ProtectAI, DataFilter, Progent, DRIFT | Không đánh giá phòng thủ | Không đánh giá phòng thủ | 10 phòng thủ: sandwich, spotlighting, PromptGuard2, PIGuard, ProtectAI, Meta SecAlign, Tool Filter, CaMeL, Progent, DRIFT | Phòng thủ metadata phía client (viết lại tool list) |
| C8 | Hàm `utility`/`security` **tất định** trên trạng thái môi trường trước–sau; tác giả chủ ý tránh LLM chấm | Như AgentDojo | Phân loại tool-call: Success / Failure-Ignored / Failure-Direct Execution / Failure-Refused | Phân tích cú pháp hành động kế tiếp (ReAct); bước 2 của data stealing dùng GPT-4 **mô phỏng** phản hồi tool | Như AgentDojo (hàm tất định) | Sink được gọi = thành công; canary trong tham số sink là tín hiệu mạnh hơn, ghi riêng |
| C9 | Benign utility, utility under attack, targeted ASR (mẫu số: toàn bộ ca) | ASR, clean utility, utility under attack | ASR = thành công / đầu ra **hợp lệ**; refused ratio | ASR-valid (mẫu số: đầu ra hợp lệ) và ASR-all | Benign utility, utility under attack, ASR | ASR kèm Wilson CI 95% |
| C10 | 10 model (GPT-4o, Claude 3/3.5, Gemini 1.5, Llama 3 70B, Command-R+) | 5 model: GPT-4o-mini, GPT-5.4-mini, Gemini-2.5-Flash, DeepSeek-v4-Flash, Claude-Haiku-4.5 | 20 cấu hình model | 30 agent | 12 model | 6 model, 3 hãng |
| C11 | GPT-4o: benign utility 69,0%, targeted ASR 47,69% (Bảng 3); Tool filter đưa ASR về 6,84%, PI detector 7,95% nhưng benign utility còn 41,49% (Bảng 5); chạy 629 ca trên GPT-4o khoảng 35 USD (Phụ lục D) | PIGuard đưa ASR tĩnh về 0% nhưng AutoDojo khôi phục 28% tổng và 64% trên tác vụ action-open (Tóm tắt); ASR tĩnh không phòng thủ của Claude-Haiku-4.5 và GPT-5.4-mini chỉ 0,3% và 6,9% (mục 5.2) | o1-mini ASR 72,8%; ASR trung bình mọi cấu hình 36,5%; tỉ lệ từ chối cao nhất (Claude-3.7-Sonnet) dưới 3%; P3 hiệu quả nhất (46,7%) (mục 4.2, 4.4); payload IPI chuyển sang description cho ASR gần 0% (Bảng 3) | GPT-4 ReAct ASR-valid 23,6% base, 47,0% enhanced; GPT-4 fine-tuned 6,6% (Bảng 3) | GPT-4o không phòng thủ benign utility 53,33% (Bảng 9); CaMeL benign utility 0% trên cả 12 model (Bảng 11); PromptGuard2 ASR 27,15% trên GPT-4o (Bảng 16) | gpt-4o-mini, rug_pull, held-out: 0,61 → 0,53 khi bật phòng thủ; model frontier gần 0 mọi ô (README, "Published v1") |
| C12 | Tấn công/phòng thủ còn đơn giản; tool filter thất bại khi không lập kế hoạch trước được tool (17% ca) | Kẻ tấn công cố ý yếu (hộp đen, ngân sách nhỏ) → ASR là cận dưới | Chỉ một lượt; payload bán thủ công, không thích ứng | Tiền tố hack cố định; giả định agent đã gọi đúng user tool | — (không có mục riêng trong phần đã đọc) | Mọi kết quả chỉ trong harness có kiểm soát, không suy ra client MCP thật (README) |

## 3. Ghi chú đối chiếu nội bộ bài báo

- **MCPTox**: Tóm tắt ghi 1.312 ca độc, nhưng Bảng 1 cùng bài liệt kê 224 + 548 + 725 = 1.497 theo ba khuôn. Tài liệu này không tự hòa giải hai số; chỉ dẫn lại cả hai.
- **AgentDojo**: bài báo mô tả bản v1 (629 ca, 27 injection task). Bản mã hiện hành v1.2.2 lớn hơn — số đo trên bản đã chạy nằm ở `evidence/agentdojo/`.
- **AgentDyn**: bài báo dẫn repo `github.com/leolee99/AgentDyn`; bản đã clone là `SaFo-Lab/AgentDyn` (README cùng tác giả, cùng tiêu đề).

## 4. Nguồn

- AgentDojo — https://arxiv.org/abs/2406.13352 · https://github.com/ethz-spylab/agentdojo
- AutoDojo — https://arxiv.org/abs/2606.15057 · https://github.com/xhOwenMa/AutoDojo
- MCPTox — https://arxiv.org/abs/2508.14925 · https://github.com/zhiqiangwang4/MCPTox-Benchmark
- InjecAgent — https://arxiv.org/abs/2403.02691 · https://github.com/uiuc-kang-lab/InjecAgent
- AgentDyn — https://arxiv.org/abs/2602.03117 · https://github.com/SaFo-Lab/AgentDyn
- MCP-Poison-Bench — https://github.com/chirag-dewan/MCP-Poison-Bench
