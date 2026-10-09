# Lộ trình triển khai code — `ipi-agent-lab`

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Ngày, giờ và trạng thái từng việc vẫn lấy ở
> `Kế hoạch thực hiện.xlsx`. File này chỉ quy định **thứ tự dựng code, phụ thuộc và cổng chặn**,
> tham chiếu theo mã `STT-n`. Phần lý thuyết và báo cáo (STT-16, 25, 59, 77, 88, 90) xử lý sau,
> không nằm trong lộ trình này.

## 1. Hiện trạng repo

| Đã có | Ghi chú |
|---|---|
| Khung uv, ruff, pytest, docker-compose (Qdrant, MailHog), Makefile | STT-13 |
| `config/models.yaml` khóa `v-models-1.0`; `defenses.yaml`, `rag.yaml` là khung | STT-14 |
| RAG: `src/rag/ingest.py`, `embedder.py`, `retriever.py` + corpus 40 file | Kèm test |
| Bộ đo: `carrier_tasks.json`, `benign_queries.json` (đã khóa), `src/eval/allowed_actions.py` | STT-18 |
| `data/customers.db` + `scripts/seed_db.py` | Phần code của STT-22 đã có, cần đối chiếu với lược đồ |

Tag `legacy-pre-cleanup` còn `llm_client.py`, `check_targets.py`, `probe_gateway_overhead.py`,
payload `schema.py`, `utility_bench.py`. Các file này bị gỡ vì gắn bộ model cũ và schema thiếu
T6–T8, `blocked_by`. Chỉ dùng để **tham khảo logic** (retry, đếm token, log), viết lại theo hợp
đồng `config/` hiện hành. Không khôi phục nguyên trạng.

## 2. Sáu giai đoạn

Mỗi giai đoạn kết thúc bằng một **điều kiện xong kiểm được bằng máy**. Chưa đạt thì không sang
giai đoạn sau.

### Giai đoạn 0 — Gọi được ba model

| Việc | STT | Điều kiện xong |
|---|---|---|
| `src/agent/llm_client.py`: đọc `models.yaml`, gọi gateway tương thích OpenAI, retry/backoff, đếm token, ghi trường `model` của response | gộp STT-26 | Test với gateway giả (không gọi mạng) |
| `scripts/check_targets.py`: mỗi target một lời gọi tool-calling tối giản | gộp STT-26 | Ba target trả tool_call parse được; log lưu vào repo |
| `scripts/probe_gateway_overhead.py` | hạn chế số 13 | Chạy được, xuất số overhead |
| Bộ đếm chi phí: cộng dồn theo lô, cảnh báo ở `COST_BUDGET_USD_ALERT_PCT`, dừng ở 120% | phần code của STT-15 | Test với đơn giá giả |

### Giai đoạn 1 — Hợp đồng dữ liệu

| Việc | STT | Điều kiện xong |
|---|---|---|
| Interface 5 tầng và hook phòng thủ, viết thành `Protocol`/dataclass trong code | STT-17 | Import được, có docstring nêu hook nào gọi ở giai đoạn nào |
| Trace store: SQLModel `runs` + `steps` đủ trường mục 13.3, `TraceRecorder`, `export_runs()` | STT-32 | Có `blocked_by` và `technique` T1–T8 ngay từ DDL đầu; SQL tính được cả hai ASR trên dữ liệu giả |
| Schema payload T1–T8 × K1/K2a/K2b, trường `source.license` | STT-20 (phần code) | Validate được một payload mẫu mỗi kỹ thuật |
| Khung `config/experiment.yaml` | STT-24 | Runner sau này đọc được, chưa cần đủ giá trị |
| Đối chiếu `customers.db` với lược đồ | STT-22 | Test hiện có xanh |

### Giai đoạn 2 — Agent chạy được tác vụ lành tính

| Việc | STT |
|---|---|
| Tool registry: 5 tool, description tách ra nguồn thay được, nhãn rủi ro | STT-27 |
| `send_email` + MailHog, `clear_mailbox()` | STT-29 |
| `http_request`, `query_customer_db` (≤20 bản ghi), `create_ticket` | STT-30 |
| MCP server stdio + HTTP, agent lấy danh sách tool động | STT-28 |
| System prompt baseline có placeholder canary | STT-31 |
| Lõi agent Core-A: vòng lặp tối đa 8 bước, hook trước/sau mỗi bước, ghi trace | STT-26 |

**Điều kiện xong:** CT-01…CT-06 chạy hết trên một model, phòng thủ TẮT, trace ghi đủ; MailHog và
ticket nhận đúng nội dung.

### Giai đoạn 3 — Đo lường và cổng scorer

| Việc | STT |
|---|---|
| Canary generator, gieo 3 nơi, dọn sau run | STT-33 |
| Canary listener FastAPI + `/hits` (service mới trong docker-compose) | STT-34 |
| Scorer tất định: G1 bốn bồn (kể cả base64/hex), G2 hai điều kiện, G3, `blocked_by` | STT-35 |
| **Cổng 8/8** — `tests/test_scorer.py` với tám ca ở `Y_TUONG_DU_AN.md` mục 12.5 + chấm lại 100 lần cùng kết quả | STT-36 |
| Bộ chỉ số: ASR hai loại, Wilson 95%, DSR, USR, FRR, TCP, loại `parse_error` | STT-67 (kéo lên sớm) |
| Utility bench + chạy USR nền | STT-37 |

**Điều kiện xong:** 8/8 xanh. STT-37 là lô gọi API thật đầu tiên → **phải có dự toán STT-15 trước**.

### Giai đoạn 4 — Attack engine

| Việc | STT |
|---|---|
| Adapter AgentDojo, MCPTox (mô phỏng, có `source.license`) | STT-38, 39 |
| Payload tiếng Việt T1–T5, mở rộng sang K2 | STT-40, 41 |
| T5 tài liệu ẩn payload, kiểm bằng `pdftotext` | STT-42 |
| T6 chia mảnh · T7 kích hoạt trễ · T8 che giấu tiếng Việt · T1 giọng thẩm quyền | STT-48, 50, 47, 49 |
| Mutator + `activation_check`, lọc trùng | STT-43 |
| Injector K1 (`delivered` theo top-k) và K2a/K2b (rug-pull) | STT-44, 45 |
| Runner ma trận: tích Descartes, checkpoint, `--resume`, dọn KB/hộp thư mỗi run | STT-46 |

**Điều kiện xong:** chạy được 40 ca pilot (STT-60) end-to-end. Sau đó **tag `v-attack-1.0`**,
không thêm kỹ thuật nữa (quy tắc cứng #9).

### Giai đoạn 5 — Defense layer

| Việc | STT |
|---|---|
| D1 Spotlighting · D2 Sanitizer · D3 Tool policy (`task_type` là input, không phân loại ý định) · D4 Egress | STT-51…54 |
| Pipeline đọc `defenses.yaml`, mọi tổ hợp bật/tắt, ghi cấu hình vào trace | STT-55 |
| Test mỗi cơ chế ≥5 ca (3 phải chặn, 2 không được chặn) + test tích hợp | STT-56 |
| Tấn công thích ứng ≤3 vòng | STT-57 |

**Điều kiện xong:** mọi tham số D1–D4 ở `defenses.yaml` (quy tắc cứng #4); `grep` trong
`src/defense/` không thấy hằng số hành vi.

### Giai đoạn 6 — Trình bày và tích hợp ngoài

| Việc | STT |
|---|---|
| Notebook bảng, biểu đồ | STT-68 |
| Dashboard 4 trang | STT-58 |
| Tích hợp HN-CC, HN-OW vào MCP server, pin phiên bản | STT-79 |
| Đóng gói một lệnh `docker compose up`, test máy sạch | STT-83 |

## 3. Cổng chặn — không được vượt

| Cổng | Chặn việc gì | Nguồn |
|---|---|---|
| Dự toán chi phí có số thật | Mọi lô gọi API (STT-37 trở đi) | `Y_TUONG_DU_AN.md` mục 18, việc 8 |
| Scorer 8/8 | Pilot và ma trận (STT-60 trở đi) | Quy tắc cứng #5 |
| Ma trận dự đoán ghi trước (STT-21) | Pilot STT-60 | Mục 7.3 |
| `v-attack-1.0` | Hiện thực D1–D4 | Phụ lục ký GVHD, hạng mục 5 |
| ASR pilot trong 20–80% (STT-61) | Full matrix | Quy tắc cứng #5 |

## 4. Thứ tự phụ thuộc

```
G0 llm_client ─┐
G1 trace/schema ├─► G2 agent + tool + MCP ─► G3 canary + scorer ─► [8/8] ─► STT-37 USR nền
               │                                                   │
               └──────────────────────────────► G4 attack engine ──┴─► pilot STT-60 ─► v-attack-1.0
                                                                                        │
                                                                         G5 D1–D4 ◄─────┘
                                                                                        │
                                                                         G6 dashboard, harness
```

G4 có thể dựng song song với G3 vì không gọi model thật cho tới khi chạy pilot.
