# Phân tích fit-gap: benchmark có sẵn so với yêu cầu của lab

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Mọi nhận xét về hành vi của một benchmark đều trỏ về một file trong `evidence/`, sinh ra từ lần cài và chạy thật (quy tắc cứng #2). Nhận xét chỉ dựa vào bài báo được đánh dấu **[P]**; nhận xét dựa vào lần chạy thật được đánh dấu **[E]** kèm đường dẫn. Số do tác giả công bố xem `TOM_TAT_CONG_TRINH.md`.

## 1. Mức bằng chứng đã đạt

Mức L3 (chạy có LLM) **chưa** đạt ở benchmark nào vì phiên này không dùng API key (không mở `.env`). Vì vậy tài liệu này **không** đưa ra số ASR hay utility tự đo nào; mọi nhận xét giới hạn ở cấu trúc, định dạng, khả năng tích hợp và độ đúng của bộ chấm khi chạy bằng ground truth.

| Mức | Nghĩa | AgentDojo | AutoDojo | MCPTox | InjecAgent | AgentDyn | MCP-Poison-Bench |
|---|---|---|---|---|---|---|---|
| L1 | Cài được, nạp được dữ liệu | Đạt | Đạt | Đạt | Đạt | Đạt (dùng `uv.lock` của tác giả) | Đạt |
| L2 | Chạy harness không LLM (ground truth, test, kiểm kê) — nguồn: log và `run_manifest*.txt` ở E-1…E-7 | Đạt — 4 suite × 5 attack | Chỉ kiểm kê payload phát hành | Chỉ kiểm kê (repo không có runner) | Chỉ kiểm kê | Một phần — 2/3 suite lỗi khi chạy ground truth | Đạt — 463 test qua |
| L3 | Chạy có LLM, tự đo ASR | Chưa | Chưa | Chưa | Chưa | Chưa | Chưa |

Lệnh để TA tự đưa lên L3 bằng key của mình: `evidence/RUN_WITH_LLM.md`.

## 2. Yêu cầu của lab dùng làm thước đo

Rút từ `Y_TUONG_DU_AN.md` các mục 2, 5, 6, 8, 12, 14.

| Mã | Yêu cầu |
|---|---|
| R1 | Kênh K1 — tài liệu RAG, có cờ `delivered` tách "không truy hồi" với "truy hồi nhưng không sập bẫy" |
| R2 | Kênh K2a — mô tả công cụ qua MCP, lấy tool list động |
| R3 | Kênh K2b — kết quả trả về của công cụ |
| R4 | Kỹ thuật T1–T5 (nền) và T6–T8 (mở rộng: tiếng Việt, chia mảnh, kích hoạt trễ) |
| R5 | Mục tiêu G1 rò canary tại 4 điểm, G2 tool-call ngoài `allowed_actions`, G3 |
| R6 | Chấm tất định, không LLM chấm; bộ chấm kiểm chứng được (cổng 8/8) |
| R7 | Utility đo cùng cấu hình với ASR (USR, FRR, TCP) |
| R8 | Trace có `blocked_by ∈ {defense, model_refusal, harness}` |
| R9 | Kẻ tấn công thích ứng để tính ARR |
| R10 | Payload có `source.license` hợp lệ cho `verbatim`/`adapted` |
| R11 | Bối cảnh doanh nghiệp Việt, tiếng Việt |
| R12 | Tái lập được: pin phiên bản, chạy lại một lệnh |

## 3. Ma trận fit-gap

Ký hiệu: **Có** · **Một phần** · **Không**. Ô chỉ dựa trên bài báo ghi [P]. Ô "Như AgentDojo" nghĩa là benchmark là bản fork dùng lại nguyên lõi AgentDojo (cùng tên gói `agentdojo` trong `pyproject.toml`) nên kế thừa nhận xét của cột AgentDojo; các ô "Có"/"Không" chưa gắn mã ở R8, R9, R12 dựa trên đọc bài báo/README [P].

| | AgentDojo | AutoDojo | MCPTox | InjecAgent | AgentDyn | MCP-Poison-Bench |
|---|---|---|---|---|---|---|
| R1 K1 RAG | Không — không có retriever; payload luôn vào output của tool đã gọi [E-2] | Không [P] | Không [P] | Không [P] | Không [P] | Không [P] |
| R2 K2a | Không [P] | Không [P] | **Có** — 485 payload là tool description [E-4] | Không [P] | Không [P] | **Có** — `tool_description`, `schema_field`, `metadata_drift` [E-6] |
| R3 K2b | **Có** — 949 cặp, 100% payload tới tool output khi chạy ground truth [E-2] | Có (kế thừa) [E-3] | Không [P] | Có, nhưng phản hồi tool **viết sẵn** 100% ca [E-5] | Có [E-7] | Có — `rug_pull` [E-6] |
| R4 T1–T5 | T1/T2 (đã chạy: direct, ignore_previous, system_message, injecagent, important_instructions_no_names) [E-2] | T1/T2 + biến thể tối ưu [E-3] | T3 dạng thống trị — cần TA xác nhận ánh xạ (mục 5) [E-4] | T1/T2 [E-5] | T1 [P] | T3-giống, T4 (zero-width) [E-6] |
| R4 T6–T8 | Không [P] | Không [P] | Không [P] | Không [P] | Không [P] | Không [P] |
| R5 G1/G2 | G2 có (security check trên trạng thái); không có canary [E-1] | Như AgentDojo | Chỉ nhãn tool-call, không thực thi [P] | Chỉ nhãn hành động kế tiếp [P] | Như AgentDojo | Có canary tổng hợp + sink [E-6] |
| R6 Chấm tất định, kiểm chứng được | Một phần — tất định, nhưng 8/35 injection task **không có ground truth** nên không tự kiểm được [E-1b] | Như AgentDojo | Không có mã chấm trong repo [E-4] | Không có harness tái chạy offline [E-5] | Một phần — ground truth utility 0/20 ở shopping, 2 suite lỗi [E-7] | **Có** — 463 test đơn vị qua [E-6] |
| R7 Utility cùng cấu hình | Có [P] | Có [P] | Không [P] | Không [P] | Có, và đo cả over-defense [P] | Không rõ |
| R8 `blocked_by` | Không có trường tương đương [E-2] | Không | Có nhãn `Failure-Refused` riêng [P] | Không | Không | Không |
| R9 Thích ứng | Có "Max" chọn prompt tốt nhất [P] | **Có** — 38.000 biến thể tối ưu phát hành [E-3] | Không [P] | Không [P] | Không [P] | Không |
| R10 Giấy phép | MIT [E-1] | MIT [E-3] | **Không khai giấy phép** [E-4] | MIT [E-5] | MIT [E-7] | MIT [E-6] |
| R11 Tiếng Việt | Không — 0/175 payload [E-8] | Không — 0/38.000 [E-8] | Không — 0/485 [E-8] | Không — 0/1.054 [E-8] | Không [P] | Không — 0/49 [E-8] |
| R12 Tái lập | Có — pin commit, chạy lại được [E-1] | Có | Một phần — dữ liệu phát hành lệch bài báo [E-4] | Có | Một phần — lỗi ngay cả với lockfile [E-7] | Có |

## 4. Phát hiện khi chạy thật

Đây là phần có giá trị nhất của lần chạy: những điều **không đọc được từ bài báo**.

1. **Script kiểm suite của AgentDojo báo sai 100% ca.** `check_suites` gốc báo cả 97/97 user task là "not injectable". Nguyên nhân: hàm `is_task_injectable` lọc `isinstance(content, str)`, trong khi bản mã hiện hành trả content dạng danh sách block, nên mọi tool output bị bỏ qua. Kiểm lại với bộ lọc sửa: 97/97 injectable. [E-1: `agentdojo/check_suites_upstream.log`, `agentdojo/inventory_all.json` cột `injectable_upstream_check` = 0, `injectable_fixed_check` = số user task]. Đây đúng là dạng lỗi ở bài học #4 (lỗi harness hiện ra như lỗi của đối tượng đo).
2. **8/35 injection task của AgentDojo v1.2.2 không có ground truth.** Workspace `InjectionTask6`–`InjectionTask13` có `ground_truth()` trả `[]`, nên hàm `security` của chúng không có ca dương tính để tự kiểm. [E-1b: `agentdojo/workspace_v1_2_empty_ground_truth.txt`, `agentdojo/injection_tasks_gt_all.csv`]. Hệ quả cho adapter: payload từ 8 task này phải gắn cờ "bộ chấm gốc chưa kiểm chứng".
3. **Khớp chuỗi literal để xác nhận payload đã tới ngữ cảnh là sai.** Tool output của AgentDojo được serialize YAML, xuống dòng và dấu nháy bị escape. Khớp literal cho workspace 0/560 ở mọi attack; sau chuẩn hóa hai bước (bỏ escape rồi bỏ ký tự không chữ-số) là 560/560. [E-2: `agentdojo/delivered_gt_all.csv`, cột `delivered_literal` và `delivered_gt`]. Bản đầu của chính script này cũng dính lỗi chuẩn hóa (gộp hai bước vào một regex) và đã được sửa trước lô chạy lưu trong `evidence/`; bản lỗi không được lưu nên không dùng làm số liệu. Bài học trực tiếp cho `delivered` (K1) và bộ dò canary của scorer: phải chuẩn hóa theo đúng định dạng serialize của kênh, và phải có test cho chính hàm chuẩn hóa.
4. **MCPTox phát hành lệch bài báo.** `response_all.json` có 1.348 instance (bài báo: 1.312) và nhãn của **11** model (bài báo: 20); o1-mini — model của con số 72,8% — không có trong dữ liệu phát hành, nên con số này **không tái tính được** từ repo. `label_scopes` khai trong file (`Success, Failure, Work but not Success, Identifiable, None`) không khớp nhãn thực dùng (`Success, Failure-Ignored, Failure-Direct Execution, None`). Chỉ 236/485 docstring trong `def_tool/*.py` khớp `pure_tool.json` sau chuẩn hóa khoảng trắng. Repo không có runner, không có file giấy phép. [E-4: `mcptox/inventory.json`]
5. **InjecAgent là mô phỏng một bước.** 100% trong 2.108 ca (base + enhanced) có sẵn `Thought` và `Tool Response`; agent chỉ quyết định bước kế tiếp. Số attacker tool khác nhau đếm được là 63 (README và bài báo ghi 62). [E-5: `injecagent/inventory.json`]
6. **AgentDyn chưa chạy offline được ổn định.** Với đúng `uv.lock` của tác giả: shopping — ground truth không giải được 20/20 user task; github — ground truth gọi `send_money` không tồn tại trong suite, crash; dailylife — dữ liệu môi trường thiếu trường `end_time`, crash khi nạp. [E-7: `agentdyn/check_suites_upstream_locked.log`, `agentdyn/inventory_shopping.json`]. Repo phát hành 47.723 file log chạy của 76 pipeline — chỉ kiểm kê, không dùng số trong đó.
7. **AutoDojo phát hành payload đã tối ưu, không phát hành log chạy.** 150 file = 3 suite × 5 model đích × 10 cấu hình phòng thủ, tổng 38.000 biến thể, cùng một optimizer (`google/gemini-3.1-pro-preview`). Suite travel không có tác vụ action-open nào (0/20). [E-3: `autodojo/inventory.json`, `autodojo/injection_files.csv`]
8. **MCP-Poison-Bench chạy offline sạch.** 463 test qua, không cần key. Payload rất ít: register "seen" 1 payload mỗi lớp, "held-out" 5–10 mỗi lớp. [E-6: `mcp_poison_bench/pytest.log`, `mcp_poison_bench/inventory.json`]

## 5. Đối chiếu với khẳng định đang có trong `Y_TUONG_DU_AN.md`

- Mục 6.1 ghi "T3 là dạng thống trị trong MCPTox (408/485 payload)". Lần chạy xác nhận **con số**: Template-2 (183) + Template-3 (225) = 408/485 [E-4]. Nhưng theo bài báo [P], Template-2 là "kích hoạt ngầm – chiếm chức năng" (khớp T3 "điều kiện tiên quyết giả"), còn Template-3 là "kích hoạt ngầm – **sửa tham số**" — có thể là một mục tiêu (G2) hơn là một kỹ thuật. **Cần TA chốt** Template-3 xếp vào T3 hay tách, trước khi con số 408/485 vào báo cáo.
- Mục 6.1 dẫn "ASR kênh mô tả công cụ trong y văn cao tới 72,8%". Đây là số tác giả MCPTox công bố [P], **không tái tính được** từ dữ liệu phát hành (phát hiện 4, [E-4]). Khi viết báo cáo phải ghi là số công bố.
- Mục 6.2 ghi T6 "không có trong ba benchmark đã chạy". Sau lần chạy này: không benchmark nào trong sáu có payload chia mảnh qua nhiều tài liệu, vì không benchmark nào có kênh K1 (hàng R1 của ma trận).

## 6. Kết luận fit-gap

Theo ma trận mục 3, không benchmark nào đáp ứng R1 (K1 có `delivered`), R8 (`blocked_by`) hay R11 (tiếng Việt), và không benchmark nào chứa T6–T8. Đây là căn cứ có bằng chứng cho quyết định **tự dựng lab**, đồng thời **mượn có chọn lọc**:

| Mượn gì | Từ đâu | Vì sao | Điều kiện |
|---|---|---|---|
| Payload T1/T2 cho K2b (≥100, adapter W-adapter) | AgentDojo | MIT; 949 cặp đã chạy được; mọi payload tới được tool output [E-2] | Gắn cờ `grader_unverified` cho payload từ 8 injection task thiếu ground truth; gắn cờ coupling ngữ nghĩa (payload nhắc tên người, IBAN, khách sạn… của suite gốc) |
| Mẫu tool poisoning cho K2a | MCPTox | Nguồn K2a lớn nhất (485) [E-4] | Repo **không có giấy phép** → không dùng `verbatim`/`adapted` khi chưa có văn bản cho phép của tác giả; trước mắt chỉ dùng làm tham chiếu cấu trúc để viết payload `original` |
| Lớp `rug_pull`, `cross_server`, `schema_field` | MCP-Poison-Bench | MIT; bộ test chạy sạch [E-6] | Ít payload, dùng làm khuôn chứ không làm nguồn số lượng |
| Phương pháp kẻ tấn công thích ứng cho ARR | AutoDojo | Vòng lặp hộp đen ngân sách nhỏ khớp mức A-adaptive của đồ án [P]; MIT [E-3] | Chi phí gọi optimizer phải vào `cost_budget.md` trước khi chạy |
| Ý tưởng nhãn mức đặc tả tác vụ (action-open / param-open / fully-specified) | AutoDojo | Giải thích được vì sao ASR khác nhau giữa CT-01…CT-06 [E-3] | Chỉ gắn nhãn cho tác vụ chở mới; **không sửa** `data/carrier_tasks.json` đã khóa (quy tắc #1) |
| Ý tưởng "chỉ dẫn hữu ích từ bên thứ ba" để đo FRR | AgentDyn | Đúng điểm mù over-defense của D2/D3 [P] | Không lấy dữ liệu (ground truth lỗi khi chạy offline [E-7]) |

Không mượn InjecAgent làm nguồn payload chính: môi trường một bước với phản hồi tool viết sẵn không khớp vòng lặp agent nhiều lượt của lab [E-5]; chỉ giữ làm mốc đối sánh y văn.

## 7. Việc còn mở

1. TA chốt ánh xạ Template-3 của MCPTox (mục 5).
2. TA quyết có liên hệ tác giả MCPTox xin phép dùng payload hay không (R10).
3. Chạy L3 theo `evidence/RUN_WITH_LLM.md` khi đã có hạn mức trong `cost_budget.md`; chỉ sau đó mới được so bậc độ lớn ASR với số công bố (task 69 trong kế hoạch).
