# TAXONOMY KÊNH NỘI DUNG KHÔNG TIN CẬY

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Đây là **đặc tả mức thi hành** của taxonomy
> kênh. Mục 6 của `docs/01. Đề bài/01. Mô tả bài toán.md` nêu bản chất và ranh giới; file này
> nêu tiêu chí phân loại, điểm bơm cụ thể, cơ chế kích hoạt, và ánh xạ sang T1–T8 và D1–D4.
> Đặc tả kỹ thuật tấn công ở `payload_taxonomy.md`, đặc tả phòng thủ ở `defense_spec.md`.

---

## 1. TRỤC PHÂN LOẠI

Một kênh được định nghĩa bằng **vị trí trong vòng đời một lượt suy luận của agent** mà tại đó
nội dung ngoài vành đai tin cậy được ghép vào cửa sổ ngữ cảnh. Không phân loại theo định dạng
file, theo nội dung payload, hay theo mục tiêu tấn công — ba trục đó đã có ký hiệu riêng
(`obfuscation`, T1–T8, G1–G3) và trộn vào đây sẽ làm bảng ASR không đọc được.

Năm giai đoạn của một lượt, để định vị điểm bơm của từng kênh:

```
Gieo (ngoài vành đai) → Nạp (KB tự động, tool list lúc chạy) → Kích hoạt (người dùng hỏi)
  → Nhầm lẫn ranh giới (ghép prompt) → Thi hành (tool-call thật)
```

Hai kênh thực nghiệm K1 và K2 bơm ở giai đoạn **Nạp**; chúng khác nhau ở chỗ nội dung có phải
vượt một khâu chọn lọc mới vào được context hay không. Đó chính là trục sinh ra RQ1.

### 1.1 Ba câu hỏi phân định một kênh

| # | Câu hỏi | Vì sao đủ để tách kênh |
|---|---|---|
| Q1 | Nội dung do **thực thể nào** ghi, và ghi vào **kho nào**? | Quyết định kẻ tấn công cần quyền gì (NL2 trong `02. Threat Model.md` mục 2) |
| Q2 | Nội dung vào context **bảo đảm** hay **có điều kiện**? | Quyết định có tồn tại biến `delivered` hay không, tức có hai chỉ số ASR hay một |
| Q3 | Nội dung nằm ở **vùng nào** của prompt so với chỉ thị hệ thống? | Quyết định mức tin cậy ngầm định mà mô hình gán cho nó |

Hai nội dung trả lời giống nhau cả ba câu thì **không** tách thành hai kênh. Đây là lý do K2a và
K2b là hai phân kênh của cùng K2 — giống nhau ở Q2 (đều bảo đảm vào context) — chứ không phải
hai kênh ngang hàng với K1.

---

## 2. NĂM KÊNH

| Mã | Kênh | Thực thể ghi | Vào context | Vùng prompt | Phạm vi |
|---|---|---|---|---|---|
| **K1** | Tài liệu retrieval (RAG) | Người gửi file vào pipeline ingest | Có điều kiện — chỉ khi chunk được truy hồi | Vùng dữ liệu, sau câu hỏi người dùng | **Thực nghiệm** |
| **K2a** | Mô tả công cụ | MCP server bên thứ ba | Bảo đảm — mọi lượt | Cùng vùng với chỉ thị hệ thống | **Thực nghiệm** |
| **K2b** | Kết quả trả về của công cụ | MCP server bên thứ ba | Bảo đảm — khi tool được gọi | Giữa chuỗi suy luận | **Thực nghiệm** |
| K3 | Nội dung web hoặc API ngoài | Chủ sở hữu trang web | Có điều kiện | Vùng dữ liệu | Chỉ mô tả |
| K4 | Bộ nhớ dài hạn của agent | Chính agent ở lượt trước | Bảo đảm | Vùng gần chỉ thị hệ thống | Chỉ mô tả |
| K5 | Liên-agent (A2A), đa MCP server | Agent khác; server B | Bảo đảm | Tùy kiến trúc | Chỉ mô tả |

### 2.1 K1 — Tài liệu retrieval

**Điểm bơm.** Một file hoặc một chunk trong vector store. Trong lab: tài liệu nhiễm độc có ID
riêng, chèn vào collection nền trước run và xóa sau run.

**Cơ chế kích hoạt.** Payload chỉ có tác dụng khi chunk chứa nó lọt vào top-k của retriever cho
câu hỏi của tác vụ chở. Kẻ tấn công phải tối ưu **đồng thời** hai thứ đối nghịch: độ tương đồng
ngữ nghĩa với truy vấn dự kiến, và nội dung độc. Đây là kênh **duy nhất** có `delivered` biến
thiên, nên cũng là kênh duy nhất mà `ASR_cond` có nghĩa.

**Bề mặt ẩn giấu riêng.** Metadata file, footer, chữ trắng trên nền trắng, HTML comment, text
ẩn theo CSS — chênh lệch giữa cái người duyệt tài liệu thấy và cái parser đọc ra.

**Giả định vận hành cho phép kênh này mở:** giả định 1 — KB nạp tự động từ email/upload, không
qua kiểm duyệt nội dung.

### 2.2 K2a — Mô tả công cụ

**Điểm bơm.** Trường `description` trong tool schema mà agent lấy về lúc chạy.

**Cơ chế kích hoạt.** Không cần kích hoạt gì. Nội dung vào context ở **mọi** lượt, kể cả khi
công cụ đó không bao giờ được gọi. `delivered = true` theo định nghĩa, nên `D = N`.

**Đặc thù.** Mô tả công cụ nằm cùng vùng với chỉ thị hệ thống — đây là vùng mô hình gán mức tin
cậy cao nhất, và là lý do kỹ thuật T3 (điều kiện tiên quyết giả) thống trị ở đây. Cho phép
**rug-pull**: tool list đổi giữa hai phiên, bản duyệt lần đầu không còn bảo đảm gì cho lần sau.

**Giả định vận hành cho phép kênh này mở:** giả định 2 — tool list lấy lúc chạy, không pin
phiên bản, không kiểm chữ ký, không so với bản đã duyệt.

**Lưu ý phòng thủ.** K2a **không qua D2 theo mặc định**: mô tả tool là văn bản cấu hình ngắn,
tần suất strip nhầm `{parameter}` hợp lệ cao hơn lợi ích. Đây là quyết định thiết kế, phải đọc
kèm khi diễn giải DSR của D2.

### 2.3 K2b — Kết quả trả về của công cụ

**Điểm bơm.** Payload nằm trong response JSON của một công cụ.

**Cơ chế kích hoạt.** Vào context khi công cụ được gọi — tức **giữa chuỗi suy luận**, ngay
trước bước agent quyết định hành động tiếp theo. Đòn bẩy cao nhất trong ba kênh thực nghiệm:
khoảng cách giữa lúc payload vào context và lúc agent ra quyết định là ngắn nhất.

**Giả định vận hành cho phép kênh này mở:** giả định 3 — tool-result được agent tin ở mức dữ
liệu nghiệp vụ. Đây là giả định **khó bỏ nhất**, vì hầu hết agent thật đều tin tool-result.

### 2.4 K3 — Nội dung web hoặc API bên ngoài

Trang web agent duyệt, hoặc API công khai agent gọi. Bề mặt gần như vô hạn, không kiểm soát
được nguồn. **Ngoài phạm vi thực nghiệm** vì hai lý do: (i) không thêm trục phân biệt mới so với
K1 — cũng là vùng dữ liệu, cũng vào context có điều kiện; (ii) không tái lập được, nội dung một
URL thật đổi giữa hai lần chạy làm mọi con số mất giá trị so sánh.

Tấn công trực tiếp — người dùng tự gõ prompt độc — **không** mở K3: giả định 6 nói người dùng
nội bộ là lành tính. Kẻ tấn công nội bộ là mô hình đe dọa khác.

### 2.5 K4 — Bộ nhớ dài hạn của agent

Bản ghi memory từ lượt trước được nạp lại ở lượt sau. Cho phép tấn công **bền vững qua nhiều
phiên**: payload chỉ cần vào một lần, sau đó tự tái nạp. **Ngoài phạm vi** vì testbed không có
tầng memory — thêm tầng này là thêm một biến kiến trúc mới vào mọi ô của ma trận, và mọi kết
quả trước đó không so được với sau đó.

### 2.6 K5 — Liên-agent và đa MCP server

Thông điệp từ agent khác (A2A), hoặc tool list của server B mang payload nhắm tool của server A.
Đặc thù: **nạn nhân và điểm bơm ở hai thực thể khác nhau**, và rug-pull phá giả định "duyệt một
lần là xong". **Ngoài phạm vi** vì đòi dựng thêm ít nhất một agent và một MCP server thứ hai —
vượt ngân sách 17 tuần, và phần đo được sẽ mỏng hơn phần phải dựng.

---

## 3. TIÊU CHÍ VÀO PHẠM VI THỰC NGHIỆM

Ba tiêu chí, phải thỏa **cả ba**:

| # | Tiêu chí | K1 | K2a | K2b | K3 | K4 | K5 |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| C1 | Có trong kiến trúc RAG + MCP tối thiểu — không đòi dựng thêm thành phần | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| C2 | Tái lập được — nội dung kênh do lab kiểm soát hoàn toàn | ✓ | ✓ | ✓ | ✗ | — | — |
| C3 | Thêm một trục phân biệt mới, không trùng kênh đã có | ✓ | ✓ | ✓ | ✗ | — | — |

K3 trượt C2 và C3; K4 và K5 trượt C1. Ba kênh còn lại vào phạm vi, gộp thành **hai kênh** K1 và
K2 ở mức phát biểu kết quả.

**Vì sao K2 là một kênh chứ không phải hai.** K2a và K2b cùng trả lời như nhau cho Q1 (đều do
MCP server bên thứ ba ghi) và Q2 (đều vào context bảo đảm). Chúng chỉ khác ở Q3 — vị trí trong
prompt. Gộp lại khi so với K1 vì đối tượng của RQ1 là **ảnh hưởng của khâu truy hồi**, và ở
điểm đó K2a với K2b đứng cùng phía. Tách ra khi trả lời RQ2, vì kỹ thuật mạnh nhất trên hai
phân kênh được dự đoán là khác nhau.

**Trace vẫn ghi ba giá trị.** `channel ∈ {K1, K2a, K2b}`. Gộp là thao tác lúc tổng hợp bảng,
không phải lúc ghi. Ghi gộp từ đầu thì mất vĩnh viễn khả năng tách RQ2.

---

## 4. ÁNH XẠ KÊNH × KỸ THUẬT

Bảng này nêu kỹ thuật nào **dựng được** trên kênh nào, không phải kỹ thuật nào mạnh hơn — dự
đoán về độ mạnh nằm ở ma trận kỹ thuật × phòng thủ trong `payload_taxonomy.md`, một chỗ duy nhất.

| Kỹ thuật | K1 | K2a | K2b | Ghi chú |
|---|:--:|:--:|:--:|---|
| T1 Câu lệnh tường minh, giả mạo uy quyền | ✓ | ✓ | ✓ | |
| T2 Ghi đè chỉ thị hệ thống từ trong tài liệu | ✓ | ✓ | ✓ | |
| T3 Điều kiện tiên quyết giả | ✓ | ✓ | ✓ | Dạng tự nhiên nhất ở K2a — mô tả tool vốn là nơi khai điều kiện dùng |
| T4 Chèn ẩn, bất đối xứng hiển thị | ✓ | ✗ | ✓ | K2a là chuỗi JSON ngắn, không có tầng render để tạo bất đối xứng |
| T5 Ngụy trang nghiệp vụ | ✓ | ✓ | ✓ | |
| T6 Payload chia mảnh | ✓ | ✗ | ✗ | Đòi nhiều đơn vị mang payload được truy hồi độc lập — chỉ K1 có |
| T7 Kích hoạt trễ, có điều kiện | ✓ | ✓ | ✓ | Cần tác vụ chở nhiều bước: CT-04, CT-05, CT-06 |
| T8 Che giấu đặc thù tiếng Việt | ✓ | ✓ | ✓ | |

Hai ô `✗` của T4 và ba ô của T6 là **ràng buộc kiến trúc**, không phải lựa chọn. Phải khai ở
bảng kết quả: ô trống trong ma trận kênh × kỹ thuật không đồng nghĩa với ASR bằng 0.

---

## 5. ÁNH XẠ KÊNH × PHÒNG THỦ

| Cơ chế | K1 | K2a | K2b | Lý do |
|---|:--:|:--:|:--:|---|
| **D2** Input Sanitizer | có | **không** | có | K2a không qua D2 theo mặc định — xem mục 2.2 |
| **D1** Spotlighting | có | có | có | Dựng lại ranh giới lúc ghép prompt, áp cho mọi nội dung không tin cậy |
| **D3** Tool-call Policy | có | có | có | Chặn ở tầng thi hành, không phụ thuộc kênh |
| **D4** Egress Filter | có | có | có | Chặn ở luồng ra, không phụ thuộc kênh |

D1 và D2 gắn với kênh; D3 và D4 gắn với hành động. Đây là lý do H5 dự đoán D1 và D2 sụp trước
kẻ tấn công thích ứng còn D3 và D4 giữ được.

---

## 6. NỀN CHO RQ1

K1 đòi payload phải "được tìm thấy" trước, tức phải cạnh tranh trong không gian embedding, nên
ASR phụ thuộc mạnh vào chất lượng retrieval. K2 không có ràng buộc đó: nội dung vào context một
cách bảo đảm, ở vị trí có mức tin cậy ngầm định cao hơn.

Hệ quả đo lường: một chỉ số ASR duy nhất sẽ trộn lẫn hai hiệu ứng khác bản chất — "retriever có
lấy đúng chunk không" và "agent có tin payload không". Vì vậy phải đo cả `ASR_e2e` (so sánh
giữa các kênh) lẫn `ASR_cond` (chỉ có nghĩa ở K1).

> **Giả thuyết H1:** ASR trên K2 cao hơn đáng kể so với K1 với cùng tập kỹ thuật payload.

Kiểm H1 bằng `ASR_e2e`, không bằng `ASR_cond` — `ASR_cond` ở K2 bằng đúng `ASR_e2e` nên so hai
chỉ số khác mẫu số là so sai.
