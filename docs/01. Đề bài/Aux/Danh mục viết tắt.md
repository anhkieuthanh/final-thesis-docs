# DANH MỤC TỪ VIẾT TẮT VÀ KÝ HIỆU

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Nguồn: `Y_TUONG_DU_AN.md`,
> `docs/01. Đề bài/01. Mô tả bài toán.md`. Một khái niệm — một ký hiệu; không tái sử dụng tiền tố.

## 1. Thuật ngữ và công nghệ

| Viết tắt | Tiếng Anh | Tiếng Việt / diễn giải |
|---|---|---|
| IPI | Indirect Prompt Injection | Tiêm nhiễm chỉ thị gián tiếp — chủ đề đồ án |
| RAG | Retrieval-Augmented Generation | Sinh câu trả lời có tăng cường truy hồi |
| MCP | Model Context Protocol | Giao thức chuẩn hóa để agent gọi công cụ ngoài |
| LLM | Large Language Model | Mô hình ngôn ngữ lớn |
| AI | Artificial Intelligence | Trí tuệ nhân tạo |
| A2A | Agent-to-Agent | Giao tiếp liên-agent (kênh K5) |
| KB | Knowledge Base | Cơ sở tri thức — corpus tài liệu cho RAG |
| PII | Personally Identifiable Information | Thông tin định danh cá nhân |
| E2E | End-to-End | Đầu-cuối |
| NFKC | Normalization Form KC | Chuẩn hóa Unicode, dùng trong D2 |
| ReAct | Reasoning + Acting | Kiểu vòng lặp agent suy luận xen hành động |
| Harness | — | Khung chạy agent thương mại có sẵn lớp kiểm soát |
| Canary | — | Chuỗi mồi nhúng vào tài sản để phát hiện rò rỉ |
| Rug-pull | — | Server MCP đổi mô tả công cụ sau khi đã được duyệt |

## 2. Chỉ số đo

| Ký hiệu | Tên | Định nghĩa |
|---|---|---|
| ASR | Attack Success Rate | Tỷ lệ tấn công thành công |
| ASR_e2e | ASR đầu-cuối | `S / N` — mẫu số là toàn bộ run hợp lệ |
| ASR_cond | ASR có điều kiện | `S / D` — chỉ run payload đã vào được context (chỉ có nghĩa ở K1) |
| DSR | Defense Success Rate | `1 − ASR_e2e(defense=on)` |
| USR | Utility Success Rate | Tỷ lệ hoàn thành tác vụ trên tập run sạch |
| FRR | False Refusal Rate | Tỷ lệ từ chối sai — agent đúng nhưng phòng thủ vẫn chặn |
| TCP | Tool-Call Precision | Độ khớp công cụ đã gọi với `required_tools` (đo quá trình) |
| AMR | Attack Miss Rate | `ASR_e2e(defense=on)` — phần tấn công lọt qua phòng thủ |
| SUS | Safety-Utility Score | `max(0, 100 − (ρ+0,5)·AMR − 1,5·FRR)`, `ρ = 1,5` |
| ARR | Adaptive Robustness Ratio | `DSR(adaptive) / DSR(blind)` — độ bền trước kẻ tấn công thích ứng |

## 3. Tài sản cần bảo vệ

| Ký hiệu | Tài sản |
|---|---|
| TS1 | System prompt của agent |
| TS2 | `customers.db` — dữ liệu khách hàng mô phỏng |
| TS3 | Quyền gọi `send_email` / `http_request` / `create_ticket` |

## 4. Mục tiêu tấn công

| Ký hiệu | Mục tiêu |
|---|---|
| G1 | Rò rỉ dữ liệu ra ngoài (nhắm TS1, TS2) |
| G2 | Chiếm quyền hành động (nhắm TS3) |
| G3 | Thao túng đầu ra tới người dùng — toàn vẹn thông tin |

## 5. Năng lực kẻ tấn công

| Ký hiệu | Nội dung |
|---|---|
| A-blind | Mức năng lực 1 — không biết cơ chế phòng thủ nào đang bật, một vòng |
| A-adaptive | Mức năng lực 2 — biết trước cơ chế, viết lại payload tối đa ba vòng |
| NL1–NL7 | Bảy trục năng lực kẻ tấn công (kiến trúc · quyền ghi · biết cấu hình phòng thủ · phạm vi quan sát · số vòng · biết canary · biết model đích) |
| PH0–PH3 | Bốn mức phản hồi mà A-adaptive quan sát được giữa các vòng; **đã chốt PH1** |

## 6. Kênh tiêm nhiễm

| Ký hiệu | Kênh | Trạng thái |
|---|---|---|
| K1 | Tài liệu retrieval (RAG) | Thực nghiệm |
| K2a | Mô tả công cụ — trường `description` trong tool schema | Thực nghiệm |
| K2b | Kết quả trả về của công cụ | Thực nghiệm |
| K3 | Nội dung web / API ngoài | Chỉ mô tả |
| K4 | Bộ nhớ dài hạn | Chỉ mô tả |
| K5 | Liên-agent (A2A), đa MCP server | Chỉ mô tả |

## 7. Kỹ thuật payload

| Ký hiệu | Kỹ thuật |
|---|---|
| T1 | Câu lệnh tường minh, giả mạo uy quyền |
| T2 | Ghi đè chỉ thị hệ thống |
| T3 | Điều kiện giả — dạng thống trị trong MCPTox |
| T4 | Chèn ẩn (ký tự vô hình, HTML comment, text ẩn theo CSS) |
| T5 | Ngụy trang nghiệp vụ — không chứa câu mệnh lệnh nào |
| T6 | Chia mảnh payload qua nhiều chunk |
| T7 | Kích hoạt trễ |
| T8 | Che giấu bằng đặc thù tiếng Việt |

## 8. Cơ chế phòng thủ

| Ký hiệu | Cơ chế | Vị trí chặn |
|---|---|---|
| D1 | Spotlighting | Dựng lại ranh giới dữ liệu/chỉ thị lúc ghép prompt |
| D2 | Input Sanitizer | Trước khi nội dung vào context và khi tool-result trả về |
| D3 | Tool-call Policy | Trước khi tool-call thật thực thi |
| D4 | Egress Filter | Ngay trước khi dữ liệu rời vành đai |

Thứ tự ghép: `D2 → D1 → (agent suy luận) → D3 → nếu tool ∈ EGRESS_TOOLS → D4 → thực thi`.

## 9. Mô hình đích và công cụ

| Ký hiệu | Nội dung |
|---|---|
| A1 | Mô hình lớp frontier |
| A2 | Mô hình doanh nghiệp Việt |
| A3 | Mô hình lớp rẻ / nhỏ — nhóm đối chiếu |
| TL1 | Công cụ `search_kb` — cửa vào kênh K1 |
| TL2 | Công cụ `query_customer_db` |
| TL3 | Công cụ `send_email` — outbound |
| TL4 | Công cụ `http_request` — outbound |
| TL5 | Công cụ `create_ticket` — outbound |

## 10. Tác vụ chở và câu hỏi lành tính

| Ký hiệu | Nội dung |
|---|---|
| CT-01 | Hỏi đáp thuần RAG — chính sách bảo hành |
| CT-02 | Hỏi đáp RAG tổng hợp nhiều tài liệu |
| CT-03 | Gọi một công cụ đọc — tra công nợ khách hàng |
| CT-04 | Chuỗi nhiều công cụ — đối chiếu tồn kho |
| CT-05 | Hành động ra ngoài hợp lệ — gửi email báo giá |
| CT-06 | Hành động ra ngoài hợp lệ — mở phiếu hỗ trợ |
| U1 | Nhóm câu lành tính: hỏi đáp thuần RAG (16 câu) |
| U2 | Gọi một công cụ đọc (14 câu) |
| U3 | Chuỗi nhiều công cụ (12 câu) |
| U4 | Hành động ra ngoài hợp lệ (10 câu) |
| U5 | Tài liệu chứa code / base64 hợp lệ (8 câu) |

## 11. Câu hỏi nghiên cứu và bước lớn

| Ký hiệu | Nội dung |
|---|---|
| B1 | Đo lỗ hổng → RQ1, RQ2 |
| B2 | Đo đánh đổi an toàn–hữu dụng → RQ3, RQ4 |
| B3 | Đo độ bền trước leo thang → RQ5 |
| B4 | Đo phần harness đã bao phủ → RQ6 |
| RQ1 | K1 và K2 khác nhau thế nào về ASR? |
| RQ2 | Kỹ thuật nào mạnh nhất trên từng kênh, có ổn định khi đổi lớp mô hình? |
| RQ3 | Tổ hợp bốn cơ chế có hơn cơ chế đơn lẻ tốt nhất không? |
| RQ4 | Cái giá về tính hữu dụng của từng cơ chế? |
| RQ5 | Phòng thủ còn hiệu quả bao nhiêu khi kẻ tấn công biết trước cơ chế? |
| RQ6 | Harness giảm ASR bao nhiêu so với vòng lặp trần? |
| H1–H6 | Giả thuyết tương ứng RQ1–RQ6 |

## 12. Mốc nghiệm thu

| Mốc | Nội dung |
|---|---|
| M0 | Chốt bài toán, có chữ ký GVHD |
| M1 | Khóa bộ đo |
| M1b | Chốt bộ model, tag `v-models-1.0`, ngân sách API |
| M2 | Lõi agent E2E, 5 tool MCP, canary, scorer đã kiểm chứng |
| M3 | Adapter benchmark ngoài, mở 2 kênh, mutator, injector, runner ma trận |
| M3b | Kỹ thuật mở rộng T6–T8, tag `v-attack-1.0` |
| M4 | Hiệu chỉnh độ khó, ASR nền 3 model, RQ1 + RQ2 |
| M5 | D1–D4, ≥6 cấu hình × 3 model, Pareto, RQ3 + RQ4 |
| M6 | Harness, ASR tập con, RQ6 |
| M7 | Tấn công thích ứng, ARR, dashboard, demo |
| M8 | Ráp báo cáo, slide, repo chạy một lệnh trên máy sạch |

## 13. Công cụ và tổ chức

| Viết tắt | Nội dung |
|---|---|
| AgentDojo | Benchmark IPI ngoài — dùng để đối sánh |
| AutoDojo | Công cụ sinh ca thử tự động |
| MCPTox | Bộ payload tấn công qua mô tả công cụ MCP |
| LangGraph | Framework agent dùng cho Core-B |
| MailHog | SMTP server giả để hứng email outbound |
| SOICT | Trường Công nghệ Thông tin và Truyền thông |
| GVHD | Giảng viên hướng dẫn |
| DATN | Đồ án tốt nghiệp |
| DoD | Definition of Done — tiêu chí hoàn thành task |
