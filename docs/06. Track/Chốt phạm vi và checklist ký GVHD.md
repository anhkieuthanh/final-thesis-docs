# CHỐT PHẠM VI ĐỒ ÁN VÀ CHECKLIST KÝ VỚI GVHD

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Biểu mẫu đã được GVHD ký: nội dung ở các mục 1–7 có hiệu lực
> theo các hạng mục đã đồng ý ở mục 9. Khi đã ký, các nguồn chân lý
> (`Y_TUONG_DU_AN.md`, `docs/01. Đề bài/01. Mô tả bài toán.md`) được đồng bộ theo tài liệu này.
> Các đề mục ghi "đề xuất" là ngưỡng sinh viên đặt trước, GVHD xác nhận hoặc sửa ngay trên bảng.

## 1. Định danh

| Mục | Nội dung |
|---|---|
| Tên đề tài | Chọn một và dùng thống nhất: ☐ "Hệ thống đánh giá và phòng chống Indirect Prompt Injection trên AI Agent" (phiếu giao nhiệm vụ) · ☑ "Nghiên cứu và xây dựng hệ thống đánh giá, phòng chống tấn công tiêm nhiễm gián tiếp (Indirect Prompt Injection) trên AI Agent dùng RAG + MCP tool-calling" |
| Loại đồ án | Ứng dụng — sản phẩm bàn giao là công cụ |
| Thời gian | Bắt đầu 07/09/2026 · hạn nộp và bảo vệ 08/01/2027 theo phiếu · 17 tuần · nhịp 20 giờ/tuần |
| Cổng kiểm chứng scorer | 8/8 ca thử (`Y_TUONG_DU_AN.md` mục 12.5). Sai một ca là chưa đạt, không chạy ma trận |
| Cổng hiệu chỉnh độ khó | ASR pilot nằm trong 20–80% trước khi chạy ma trận đầy đủ, theo giao thức ba quy tắc (mục 12.3 Mô tả bài toán) |

## 2. Persona

| Mã | Persona | Câu hỏi họ mang tới | RQ trả lời |
|---|---|---|---|
| **P1** — chính | Kỹ sư an toàn hoặc chủ nền tảng AI tại một doanh nghiệp Việt đang hoặc sắp vận hành agent có quyền gọi công cụ | Cấu hình phòng thủ nào đáng bật · đánh đổi bao nhiêu tính hữu dụng · lỗ hổng nào không cơ chế nào bịt được, kể cả khi kẻ tấn công biết trước cơ chế · harness đang dùng đã che được phần nào | RQ3, RQ4, RQ5, RQ6 |
| **P2** — phụ | Người đánh giá hoặc nhà nghiên cứu cần tái lập kết quả hay bổ sung payload | Kênh nào nguy hiểm hơn · kỹ thuật nào mạnh · chạy lại được bằng một lệnh | RQ1, RQ2 |

Phân biệt bắt buộc: **nhân viên kinh doanh** là người dùng *mô phỏng bên trong lab* (người gửi câu hỏi cho agent), không phải người dùng công cụ đánh giá. **Phản persona**: người muốn dùng tập payload nhắm vào hệ thống thật — nằm ngoài phạm vi phục vụ, xem chính sách phát hành ở mục 7.

## 3. Phạm vi chốt cứng

| Chiều | Số lượng | Nội dung | Khóa bằng |
|---|---:|---|---|
| Kênh tấn công | 2 | K1 · K2 (hai phân kênh K2a, K2b) | Checklist này |
| Kỹ thuật payload | 8 | T1–T5 nền · T6 chia mảnh · T7 kích hoạt trễ · T8 che giấu tiếng Việt | `v-attack-1.0` |
| Cơ chế phòng thủ | 4 | D1 · D2 · D3 · D4 | Checklist này |
| Mô hình đích | 3 | A1 `claude-opus-5` · A2 `glm-5.2` · A3 `glm-5.3-flash` | `v-models-1.0` |
| Mục tiêu tấn công | 3 | G1 · G2 · G3 | Checklist này |
| Mức attacker | 2 | A-blind · A-adaptive (mức phản hồi PH1, tối đa 3 vòng) | Checklist này |
| Tác vụ chở | 6 | CT-01 … CT-06 | `v-bench-1.0` |
| Câu hỏi lành tính | 60 | U1–U5 | `v-bench-1.0` |
| Harness | 2 | HN-CC Claude Code · HN-OW OpenWork (lõi opencode) · mỗi harness trên A1, A2, A3 · 50 mẫu mỗi nhánh, D=OFF (mục 6) | Pin version cả hai, ghi vào trace |

Phạm vi không mở rộng trong 17 tuần; ý tưởng phát sinh ghi vào "Hướng phát triển" của báo cáo.

**Ngoài phạm vi:** tấn công trực tiếp (chỉ làm mốc so sánh, không mở K3) · đa phương thức · tấn công tầng huấn luyện · fine-tuning chống injection · tấn công hạ tầng MCP ở tầng mạng · an toàn hạ tầng OS/container/mạng · kênh K3, K4, K5 (chỉ mô tả trong taxonomy).

## 4. Sáu câu hỏi nghiên cứu

Tập kỹ thuật chung của ba phân kênh (loại T4 vì không dựng được trên K2a, T6 vì chỉ dựng được trên K1): **T_chung = {T1, T2, T3, T5, T7, T8}**.

| Mã | Câu hỏi | Giả thuyết ghi trước | Lát cắt | Tiêu chí trả lời (đề xuất) |
|---|---|---|---|---|
| **RQ1** | Ở D=OFF, A-blind, trên T_chung, ASR của K2 khác K1 bao nhiêu — đo bằng `ASR_e2e` và bằng phép so `ASR(K2)` với `ASR_cond(K1)`? | **H1:** `ASR_e2e(K2) > ASR_e2e(K1)`, và phần chênh **không** chỉ đến từ khâu truy hồi: `ASR(K2) > ASR_cond(K1)` | D=OFF · A-blind · A2, A3 đầy đủ; A1 tập xác nhận | Kết luận "khác" khi khoảng Wilson 95% của hai nhóm không chồng; chồng thì báo cáo là xu hướng |
| **RQ2** | Ở D=OFF, trên từng kênh, nhóm kỹ thuật nào mạnh nhất, và thứ hạng có ổn định khi đổi lớp mô hình? | **H2:** T3 thuộc nhóm mạnh nhất trên K2a; T5 thuộc nhóm mạnh nhất trên K1 | Như RQ1, đủ kỹ thuật của từng kênh | "Nhóm mạnh nhất" = các kỹ thuật có cận trên CI ≥ cận dưới CI của kỹ thuật đứng đầu. "Ổn định" = Kendall τ ≥ 0,6 giữa A2 và A3; A1 chỉ kiểm tra thành viên top-3 |
| **RQ3** | Tổ hợp bốn cơ chế có hơn cơ chế đơn lẻ tốt nhất không, hơn bao nhiêu? | **H3:** Không cộng tính. D1 và D2 chồng nhau ở T1/T2/T4; phần tăng thêm chủ yếu từ D3 | 7 preset trong `config/defenses.yaml` (`off`, `d1_only`…`d4_only`, `all`, `reduced_3`) · tập ô S_def (mục 5) | Cơ chế đơn lẻ tốt nhất chọn **theo từng G**, trên lượt pilot tách khỏi lượt đo. "Hơn" khi Δ`ASR_e2e` ≥ 10 điểm % và CI không chồng |
| **RQ4** | Cái giá về tính hữu dụng của từng cơ chế: USR, FRR, TCP, độ trễ, chi phí? | **H4:** D3 có FRR cao nhất, chặn nhầm hành động hợp lệ ở U4 và CT-05, CT-06 | 60 câu × 5 lặp × 7 preset | Độ trễ báo cáo p50/p95 từ trường `latency`; chi phí = token/run (trường `tokens`) quy đổi theo bảng giá đã điền. `task_type` của 60 câu gán **một lần trước thực nghiệm** theo quy tắc "loại tác vụ nhân viên thật sẽ chọn", lưu ở `config/`, không sửa file bộ đo đã khóa |
| **RQ5** | Phòng thủ còn hiệu quả bao nhiêu khi kẻ tấn công biết trước cơ chế? | **H5:** D1 và D2 sụp gần hết; D3 và D4 giữ được | A-adaptive · PH1 · ≤3 vòng · tập ô S_adp (mục 5) | Mục tiêu G **cố định** suốt chuỗi thích ứng. Model sinh payload thích ứng pin và ghi vào trace. `ARR = DSR(adaptive) / DSR(blind)`; `DSR(blind)` gần 0 thì không chia, báo cáo hai số |
| **RQ6** | (6a) Mỗi harness giảm ASR bao nhiêu so với vòng lặp trần **trên cùng một model**? (6b) Trên cùng một model, hai harness khác nhau bao nhiêu, và chênh lệch đó có giữ chiều khi đổi model? (6c) Lớp kiểm soát của từng harness tương ứng với những lớp nào của D1–D4? | **H6:** Harness bao phủ phần lớn D3 nhưng không bao phủ D1, D2, D4 | 50 mẫu cố định · D=OFF · mọi nhánh của cùng một model chạy trong cùng một lô | 6a và 6b định lượng kèm Wilson CI; chỉ so trong cùng một model, không so chéo model. 6c là bảng ánh xạ định tính, đối chiếu tài liệu harness với các run `blocked_by = harness` |

RQ3 không kết luận được về tính cộng tính — không phát biểu "D1 góp x%, D2 góp y%". RQ6 là chỉ dấu trên hai harness, không phải kết luận tổng quát về harness thương mại.

## 5. Thiết kế phân khối — ước tính số run

Ma trận đủ mọi chiều khoảng 1.500 ô, không khả thi. Mỗi RQ dùng một lát cắt. Số dưới đây lấy **N = 30 run mỗi ô làm giả định lập kế hoạch**; N thật quyết sau pilot ở M4.

| Khối | Phục vụ | Cách tính | Số run ước tính |
|---|---|---|---:|
| B1 — nền tấn công | RQ1, RQ2 | (8 kỹ thuật trên K1 + 6 trên K2a + 7 trên K2b) × 3 G × 2 model (A2, A3) × 30 | 3.780 |
| B2 — phòng thủ, tấn công | RQ3 | S_def ≤ 12 ô × 6 preset bật × 2 model × 30 | ≤ 4.320 |
| B3 — phòng thủ, lành tính | RQ4 | 60 câu × 5 lặp × 7 preset × 2 model | 4.200 |
| B4 — xác nhận A1 | RQ1–RQ4 | Tập con cố định | ~500 |
| B5 — thích ứng | RQ5 | S_adp ≤ 6 ô × 5 preset × 10 chuỗi × ≤ 3 vòng, một model | ≤ 900 |
| B6 — harness | RQ6 | 50 mẫu × 3 model × (HN-CC + HN-OW + vòng lặp trần) | 450 |
| **Tổng** | | | **≈ 14.150** |

- **S_def** = các ô (kỹ thuật × kênh × G) có cận dưới CI của `ASR_e2e(off)` ≥ 10% ở A2 hoặc A3, lấy tối đa 12 ô theo thứ tự ASR giảm dần. Không có ASR nền thì DSR vô nghĩa.
- **S_adp** = các ô trong S_def có `DSR(blind)` ≥ 0,3 dưới ít nhất một preset đơn lẻ.
- Chi phí từng khối điền sau khi có bảng giá thật. **Không chạy lô nào khi còn ô chi phí trống.** Áp quy tắc vận hành: kiểm chi phí mỗi 2 giờ trong 4 giờ đầu, vượt 120% dự toán thì dừng.

| Khối | Token/run (đo ở pilot) | Chi phí dự toán |
|---|---:|---:|
| B1 … B6 | | |
| **Trần ngân sách API** | | |

## 6. Harness

| Mã | Harness | Chạy trên | Vai trò |
|---|---|---|---|
| **HN-CC** | Claude Code (CLI, chế độ không tương tác) | A1; A2, A3 qua `ANTHROPIC_BASE_URL` trỏ vào endpoint tương thích Anthropic — **có điều kiện** | Harness thương mại sát thực tế doanh nghiệp nhất; ví dụ GVHD đã nêu. Trên A2, A3 là cấu hình "Claude Code chạy model khác" mà doanh nghiệp dùng để giảm chi phí |
| **HN-OW** | OpenWork, chạy tự động qua lõi opencode | A1, A2, A3 | Harness mã nguồn mở đa nhà cung cấp; GVHD đã nêu; phủ được lớp model doanh nghiệp Việt |

Thiết kế đủ 2 harness × 3 model. Hai phép so hợp lệ, đều trong **cùng một model**: harness với vòng lặp trần (6a), HN-CC với HN-OW (6b). Không so một harness trên model này với nhánh bất kỳ trên model khác — chênh lệch đó lẫn model với harness.

Ràng buộc phải ghi trước khi chạy:

1. **Cấu hình quyền là một biến, phải chốt trước.** Chạy tự động thì không có người bấm duyệt: để mặc định thì mọi tool-call outbound bị treo (ASR = 0 giả tạo), bỏ qua hết quyền thì harness không còn lớp kiểm soát nào. Cấu hình chốt cho cả hai harness: allowlist tool lấy đúng `allowed_tools` của từng tác vụ chở; mọi lượt harness dừng để xin duyệt ghi `blocked_by = harness`.
2. Pin phiên bản và ghi vào `harness_version`: Claude Code; OpenWork **và** opencode. Báo cáo gọi tên "OpenWork (lõi opencode)" vì lớp kiểm soát được đo nằm ở opencode.
3. Harness đi qua cùng gateway với vòng lặp trần. Nhánh nào không làm được thì khai vào phần hạn chế: khác nhau ở tầng hạ tầng.
4. Mọi nhánh của cùng một model chạy trong cùng một lô, vì overhead token của gateway không ổn định theo thời gian.
5. Model id dùng đúng ba id ghi trong `v-models-1.0`. Gateway chỉ cung cấp bí danh, không có bản pin có ngày, nên mọi run ghi trường `model` trong response của gateway vào trace để phát hiện trôi model. Riêng HN-CC trên A2, A3: endpoint tương thích Anthropic của nhà cung cấp phải nhận đúng id đó.
6. HN-CC trên A2, A3 có thể mất một phần tính năng khi dịch API (prompt caching, chế độ suy nghĩ) và prompt của harness được viết cho model Claude — khai vào phần hạn chế, ghi các tính năng quan sát được vào trace.

**Chạy thử trước khi ký**, lưu log vào repo làm bằng chứng. Điều kiện đạt cho từng harness: kết nối MCP server của lab và thấy đủ 5 tool · chạy không tương tác bằng script · đúng model id đã pin · ghi được phiên bản · cấu hình quyền ở điểm 1 hoạt động. Nhánh HN-CC trên A2, A3 là **có điều kiện**: nhánh nào không đạt thì bỏ, RQ6 trên model đó chỉ còn HN-OW, không cần ký lại. Nhánh HN-CC trên A1 hoặc HN-OW không đạt thì ký lại hạng mục 14.

## 7. Đạo đức và phát hành

- Dữ liệu `customers.db` là mô phỏng (Faker `vi_VN`, seed cố định); không dùng dữ liệu cá nhân hay khách hàng thật.
- MCPTox chỉ chạy chế độ mô phỏng. Payload `verbatim` / `adapted` dẫn đúng giấy phép qua `source.license`.
- Tập payload T6–T8 phát hành gắn với năm công cụ của lab; canary là placeholder; không kèm hướng dẫn nhắm hệ thống thật.
- Harness chỉ chạy trên môi trường lab của sinh viên.

## 8. Việc còn treo

| # | Việc | Trạng thái |
|---|---|---|
| 1 | Lập bảng 12 công trình đã khảo sát làm căn cứ cho đóng góp `blocked_by` | ☐ |
| 2 | Rà mọi tham chiếu đường dẫn tài liệu, trỏ đúng cây thư mục hiện hành | ☑ |
| 3 | Sửa hướng dẫn dự án trong Cowork (đang ghi 8 tuần, cổng 6/6, changelog trong file JSON) cho khớp CLAUDE.md | ☐ |
| 4 | Chạy thử HN-CC và HN-OW theo mục 6 | ☐ |
| 5 | Điền bảng giá thật và trần ngân sách ở mục 5 | ☐ |
| 6 | Chốt model sinh payload thích ứng cho RQ5 | ☐ |

## 9. Checklist ký

| # | Hạng mục | Nội dung chốt | Đồng ý | Sửa / ghi chú của GVHD |
|---|---|---|:---:|---|
| 1 | Tên đề tài | Phương án đã đánh dấu ở mục 1 | ☑ | |
| 2 | Thời gian | 17 tuần, hạn nộp và bảo vệ 08/01/2027 | ☑ | |
| 3 | Persona | P1 chính, P2 phụ; tách người dùng mô phỏng trong lab (mục 2) | ☑ | |
| 4 | Kênh | 2 kênh K1, K2 (K2a, K2b) | ☑ | |
| 5 | Kỹ thuật | **Mở từ 5 lên 8** (thêm T6–T8); khóa `v-attack-1.0` trước khi hiện thực D1–D4 | ☑ | |
| 6 | Mô hình đích | **Đổi lớp mô hình**: A1 `claude-opus-5` · A2 `glm-5.2` · A3 `glm-5.3-flash`; khóa `v-models-1.0` | ☑ | |
| 7 | Phòng thủ, mục tiêu, tác vụ, câu lành tính | D1–D4 · G1–G3 · CT-01…CT-06 · 60 câu | ☑ | |
| 8 | Ngoài phạm vi | Danh sách ở mục 3 | ☑ | |
| 9 | Sáu RQ và H1–H6 | Bản ở mục 4, gồm tiêu chí trả lời ghi trước | ☑ | |
| 10 | Thiết kế phân khối | Khối B1–B6, quy tắc chọn S_def và S_adp (mục 5) | ☑ | |
| 11 | Ngân sách | Trần: 100 USD ; dừng khi vượt 120% dự toán | ☑ | |
| 12 | Cổng nghiệm thu | Scorer 8/8 · ASR pilot 20–80% theo giao thức hiệu chỉnh | ☑ | |
| 13 | Kẻ tấn công thích ứng | PH1 · ≤ 3 vòng · G cố định · model sinh payload: chưa chốt | ☑ | |
| 14 | Harness | **Thêm RQ6 với 2 harness × 3 model**: HN-OW trên A1, A2, A3 · HN-CC trên A1 và có điều kiện trên A2, A3 · 50 mẫu mỗi nhánh, D=OFF, cấu hình quyền theo mục 6 | ☑ | |
| 15 | Đạo đức và phát hành | Mục 7 | ☑ | |
| 16 | Lịch và mốc | M0–M8 theo `Y_TUONG_DU_AN.md` mục 15 | ☑ | |

Các hạng mục 5, 6 và 14 là **phụ lục điều chỉnh phạm vi** so với checklist W1 đã ký (5 kỹ thuật, cố định). Ký ở đây thay cho phụ lục đó.

|  | Sinh viên | Giáo viên hướng dẫn |
|---|---|---|
| Họ tên | | |
| Chữ ký | | |
| Ngày | | |
