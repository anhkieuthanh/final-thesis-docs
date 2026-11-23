# Nháp RQ6 — harness thương mại bao phủ phòng thủ tới đâu (B6)

> Nháp làm việc cho báo cáo (Chương 5), do AI hỗ trợ soạn. Số liệu truy nguồn:
> `ipi-agent-lab/results/tables/harness-B6-20261123T082444Z_runs.csv` (lô `harness-B6-20261123T082444Z`,
> một harness_version `core-a@e8fe7b2`). Runner: `scripts/run_harness.py`; harness HN-OW:
> `src/attack/harness_ow.py`. Còn treo tới khi TA duyệt đưa vào Overleaf.

## Câu hỏi và giả thuyết

**RQ6:** (6a) Harness thương mại giảm ASR bao nhiêu so với vòng lặp LLM trần trên cùng model?
(6c) Lớp kiểm soát của harness ứng với những lớp nào của D1–D4? **H6:** Harness bao phủ phần lớn
D3 nhưng không bao phủ D1/D2/D4.

(6b — so hai harness — bỏ: chỉ đo một harness HN-OW, HN-CC đã cắt khỏi phạm vi.)

## Thiết lập

- HN-OW = OpenWork (lõi `opencode` 1.19.6) lái model A2 (glm-5.2) qua gateway, gọi năm tool
  testbed qua MCP; `none` = vòng lặp core-a trần cùng model. Cùng lô, cùng mẫu.
- 20 mẫu bốc seeded từ kế hoạch run B2 (off/A2), mỗi mẫu chạy một lần dưới mỗi harness = 40 run,
  attacker blind, **chỉ preset off** (không bật D1–D4), 0 parse_error.
- opencode chạy **tự động** (không người xác nhận tool-call); builtin tool (bash/edit/read…) tắt,
  chỉ còn năm tool testbed.

## Kết quả (6a)

| harness | ASR_e2e | G1 | G2 | G3 | blocked_by |
|---|---|---|---|---|---|
| none (core-a) | 13/20 = 0,650 | 6/6 | 5/5 | 2/9 | — |
| HN-OW (opencode) | 13/20 = 0,650 | 6/6 | 4/5 | 3/9 | — |

Theo kênh: K2a 13/18 cả hai; K2b 0/2 cả hai. **ΔASR = 0** — harness thương mại **không giảm**
tỉ lệ tấn công thành công; `blocked_by` rỗng ở cả hai (không lớp nào chặn tool-call độc).

## Đối chiếu D1–D4 ↔ lớp kiểm soát HN-OW (6c)

| Lớp D | Chức năng | Lớp tương ứng trong OpenWork | Bao phủ? |
|---|---|---|---|
| D1 spotlighting | đánh dấu/cách ly dữ liệu không tin | — (không có đánh dấu nguồn) | Không |
| D2 input sanitizer | lọc/chuẩn hóa payload trong dữ liệu | — | Không |
| D3 tool policy / xác nhận | allowlist tool, hỏi trước khi gọi | permission `ask`/allowlist agent (có cơ chế) | Có cơ chế, **tắt khi chạy tự động** |
| D4 egress filter | chặn rò ra ngoài (email/HTTP) | — (không lọc nội dung outbound) | Không |

OpenWork **có** lớp allowlist/permission tool (gần D3) nhưng ở chế độ agent tự động nó cho phép
mọi tool trong allowlist, nên không chặn được G1/G3 — tương đương D3 bị vô hiệu.

## Nhận định so với H6

- H6 ("harness bao phủ phần lớn D3"): **không được chứng thực** trong cấu hình này. HN-OW chạy tự
  động không chặn tool-call độc nào (blocked_by rỗng), ASR bằng hệt core-a. Lớp giống-D3 của nó
  (permission/allowlist) chỉ có tác dụng khi có người xác nhận — không phải mặc định.
- Câu phản biện *"những gì anh xây, harness thương mại đã có sẵn"* **không đúng** với OpenWork chạy
  tự động: harness không có D1/D2/D4, và lớp giống-D3 không tự chặn. Giá trị của D1–D4 (đo ở B2/B5)
  không bị harness thương mại thay thế.

## Hạn chế (bắt buộc khai — rủi ro 9)

- RQ6 là **chỉ dấu trên một harness** (HN-OW/opencode), không phải kết luận tổng quát cho mọi
  harness thương mại. HN-CC không đo.
- Harness có phòng thủ riêng **không tắt hoàn toàn được**; chạy tự động là một lựa chọn cấu hình,
  harness khác hoặc chế độ có người xác nhận có thể chặn nhiều hơn.
- 20 mẫu, một target (A2), chỉ preset off — quy mô chỉ dấu. CI rộng.
