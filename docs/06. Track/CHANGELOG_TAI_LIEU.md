# CHANGELOG TÀI LIỆU

Mục mới nhất ở trên cùng. Mỗi mục: ngày · file · thay đổi · lý do.

## 2026-10-20
- `docs/04. Design/05. Ma trận dự đoán.md` — tạo mới (STT-21): giao thức ghi trước, đại lượng `r = 1 − ASR(d_only)/ASR(off)`,
  thang bốn băng có ngưỡng số, quy tắc phân xử (ô đo được khi `ASR(off) ≥ 0,20` và `N ≥ 30`; CI bootstrap), tách **ô cấu trúc**
  (`≡` luật chặn tất định, `∅` không có hook, `—` không dựng) khỏi ô thực nghiệm; D1/D2 theo kỹ thuật × kênh, D3/D4 theo chín
  lát cắt mục tiêu × bồn S1–S7; khung bản TA để trống; bảng phụ thuộc chưa chốt. Lý do: STT-21; ma trận nháp cũ không có
  ngưỡng số nên không bác được, và lệch đặc tả STT-20 ở D3/D4 (`final_answer` không qua hook; R4 chặn mọi lời gọi ghi/ra ngoài).
- `docs/04. Design/05a. Dự đoán độc lập của Claude.md` — tạo mới: bản dự đoán của Claude, niêm phong bằng SHA-256 ghi ở file
  chính mục 6. Lý do: quy trình STT-21 — TA điền trước, so hai bản độc lập.
- `Y_TUONG_DU_AN.md` — mục 7.3: thay bảng ma trận bằng con trỏ tới file mới, giữ hai đọc hiểu định hướng; mục 18 việc 5:
  "đủ 9 hàng" → "đủ 8 hàng T1–T8". Lý do: một chỗ duy nhất; T9 đã gộp vào T1 từ 2026-10-05.
- `docs/01. Đề bài/01. Mô tả bài toán.md`, `docs/04. Design/02. Threat Model.md` mục 5, `docs/03. Khảo sát/KHAO_SAT_PHONG_THU.md`,
  `docs/06. Track/Lộ trình triển khai code.md` — sửa con trỏ ma trận dự đoán về file mới. Lý do: con trỏ cũ trỏ sai
  (`payload_taxonomy.md`, `Y_TUONG_DU_AN.md` mục 7.3).
- `docs/04. Design/payload_taxonomy.md` — chốt schema STT-20 (bước 1). (a) `goal_binding` chuyển từ trường bổ sung sang
  **bắt buộc có điều kiện**, hết mâu thuẫn với bất biến 6. (b) `id` ghi rõ ánh xạ viết tắt `VI|EN|MIX` ↔ enum `vi|en|mixed`.
  (c) `base_frame`: **giữ**, bắt buộc với T8 (có đối chứng cùng khung — mục 6.6), khuyến nghị với T6/T7; thêm bất biến 10.
  (d) thêm mục 4.4: **T4 ngoài tập `base_frame`** — không dựng payload chồng hai cơ chế né, ghi thành giới hạn phạm vi.
  (e) T2 × K2a **giữ cho**, bác bản cấm `legacy-pre-cleanup`. Lý do: `T_chung` đã khóa và GVHD ký ở `Chốt phạm vi…` mục 4.
  Lý do chung: TA chốt mục 3–5 của bước rà schema; hai lỗi nhất quán (a)(b) sửa thẳng.
- `docs/04. Design/payload_author_worksheet.md` — tạo mới: phiếu điền T1–T8 (bước 2 STT-20). Mỗi kỹ thuật một khung điền:
  ô cố định (mã, biến thể, kênh, base_frame, nguồn/giấy phép) Claude điền; ô nội dung tấn công `<<ĐIỀN: …>>` để người soạn
  viết; công thức `activation_check` theo G1/G2/G3 chấm bằng máy; tác vụ chở gợi ý theo `payload_binding_rules`. Lý do:
  tách phần đặc tả khỏi phần sinh nội dung khai thác; file không chứa payload hoàn chỉnh.
- `ipi-agent-lab/src/attack/payloads/schema.py` + `tests/test_payload_schema.py` — tạo mới: validator payload (bước 3
  STT-20). `validate_payload()` cưỡng chế bất biến taxonomy 4.3 (1–10) + ràng buộc trường 4.1/4.2/5; mỗi lỗi gắn mã bất
  biến. `load_payloads()` gom lỗi theo id, không ném ngoại lệ. Hằng tool/bồn G1/placeholder canary đọc thẳng từ
  `carrier_tasks.json` và `eval/canary.py` (một nguồn sự thật). Chỉ thư viện chuẩn. 17/17 test xanh, ruff sạch. Validator
  chỉ kiểm hình thức, không kiểm hiệu lực tấn công (việc của pilot).
- `ipi-agent-lab/data/payloads_sample.json` — tạo mới: 7 entry T1/T2/T4 (3 T1, 2 T2, 2 T4), validate 7/7 xanh. Áp mô hình
  hai lớp của taxonomy: **khung tấn công** (`technique.template`) mượn verbatim từ AgentDojo (MIT), dịch sang tiếng Việt,
  trích đúng file nguồn — `ImportantInstructionsAttack`, `IgnorePreviousAttack`, `InjecAgentAttack`, `DirectAttack`;
  **mục tiêu lab** (`goal_binding.instruction_vi/en`) viết mới theo năm tool của lab, bám tác vụ chở. T1-G1 (authority_letter)
  và T4 là `original`. Khung AgentDojo lấy qua WebFetch từ repo công khai ethz-spylab/agentdojo, không chép toàn bộ dataset
  vào repo. Lý do: hoàn tất phần Claude dựng được (T1/T2/T4); còn T3, T5, T6, T7, T8 do người soạn viết (xem HUONG_DAN).
- `ipi-agent-lab/data/payloads_sample.json` — thêm khung T3 (×2) và T5 (×2), tổng 11 entry, validate 11/11 xanh. T3/T5 là
  `original` (không benchmark): Claude dựng `technique.template` (khung điều kiện tiên quyết cho T3; khung trần không mệnh
  lệnh cho T5 — giữ đòn bẩy 'chỉ khẳng định') + goal_binding tool/arguments + activation_check + ghép tác vụ chở; ô
  `instruction_vi/en` điền mục tiêu lab (T3 dạng điều kiện tiên quyết, T5 dạng khẳng định không mệnh lệnh — giữ đòn bẩy).
  Cả 11 entry T1–T5 đã điền đủ, không còn ô trống; GVHD rà lại câu chữ. Còn lại T6, T7, T8 (phát kiến đồ án).
- `ipi-agent-lab/data/payloads_sample.json` — thêm T6 (×2), T7 (×1), T8 (×1) + 1 đối chứng của T8; tổng 16 entry, đủ 8
  kỹ thuật, validate 16/16 xanh. T6: `fragments` ≥2 mỗi mảnh có `fragment_id`, ghép CT-02, base_frame khai; T7: `trigger`
  `min_step=3`, ghép CT-04; T8: `vi_transform=[strip_diacritics]` + `base_frame=T1`, kèm **bản đối chứng** `P-T1-G2-VI-002`
  (`control_for`) cùng nội dung không biến đổi (bất biến 10, taxonomy 6.6). Tất cả `original`. Phân bố: T1×4, T2–T6×2,
  T7×1, T8×1.
- `docs/06. Track/Việc treo.md` — thêm rồi **đóng** VT-3 ngay (TA chọn nới bất biến 6, không treo). Mâu thuẫn: G1 qua bồn
  `final_answer` không biểu diễn được vì bất biến 6 cũ buộc G1 phải có tool, nhưng answer-leak không có tool-call. Phát hiện
  khi ghép T6 vào CT-02.
- `docs/04. Design/payload_taxonomy.md` — **nới bất biến 6** (xử VT-3): `goal_binding.tool = None` khi G3 **hoặc** khi G1 rò
  chỉ qua `final_answer` (`sinks == ["final_answer"]`, không tool-call). G1 qua bồn egress và mọi G2 vẫn bắt buộc tool. Sửa
  mục 4.1, 4.2, bất biến 6.
- `ipi-agent-lab/src/attack/payloads/schema.py` + test — cưỡng chế bất biến 6 đã nới: thêm nhánh `g1_answer_only`. Thêm 3
  test (answer-only cho tool None, answer-only bác tool đã gán, egress vẫn cần tool) → 20/20 xanh. Thêm payload
  `P-T6-G1-VI-001` (T6 rò qua answer trên CT-02) minh họa vector vừa mở; `payloads_sample.json` 17 entry, 17/17 xanh.
- `docs/04. Design/HUONG_DAN_DIEN_PAYLOAD.md`, `payload_author_worksheet.md` — đồng bộ nới bất biến 6: bảng trường và mẫu
  khối ghi `tool = None` cả khi G1 rò chỉ qua `final_answer`, không riêng G3.
- `Kế hoạch thực hiện.xlsx` (STT-20) — Trạng thái "Chưa bắt đầu" → "Xong (đặc tả)"; ghi chú nêu phần đã xong (đặc tả T1–T8,
  D1–D4; validator + 17 payload mẫu; worksheet; hướng dẫn) và phần còn (GVHD rà, tập đầy đủ + pilot chặn bởi STT-26, κ≥0,80,
  khóa v-attack-1.0). `Lộ trình triển khai code.md` — thêm schema payload + validator vào "Đã có"; cập nhật lưu ý legacy
  (payload `schema.py` đã viết lại, đủ T6–T8). Lý do: đồng bộ thông tin dự án sau khi chốt phạm vi STT-20 = đặc tả đã trọn.
- `docs/04. Design/HUONG_DAN_DIEN_PAYLOAD.md` — tạo mới: hướng dẫn soạn payload (bước 2–3). Hình dạng file, khung JSON hợp
  lệ sao chép được, bảng điền từng trường kèm mã lỗi validator, "công thức" đòn bẩy từng kỹ thuật (người soạn tự viết nội
  dung chỉ thị), cách chạy validator, vòng soạn đầy đủ. Lý do: hoàn tất bước 3 và nối sang phần người soạn điền.
- `docs/07. Báo cáo/Chuong2.tex`, `docs/07. Báo cáo/refs_chuong2.bib` — tạo mới: Chương 2 (khảo sát hiện trạng,
  use case tổng quát và ba biểu đồ phân rã, quy trình nghiệp vụ, đặc tả năm use case, yêu cầu phi chức năng), hình vẽ
  bằng TikZ. Lý do: ND3 yêu cầu chương 2; nội dung rút từ `Y_TUONG_DU_AN.md`, `docs/03. Khảo sát/` và `docs/04. Design/`.
- `docs/07. Báo cáo/Chuong1.tex` mục 1.2 — hạn chế thứ hai đổi thành "chưa bộ đo nào tách lượt bị phòng thủ chặn khỏi
  lượt mô hình tự từ chối". Lý do: bản cũ ghi chưa bộ đo nào đồng thời đo phòng thủ, hữu dụng và kẻ tấn công thích ứng,
  nhưng AutoDojo đo cả ba (`TOM_TAT_CONG_TRINH.md` C7, C9, C6). Mục 1.3 — bỏ "thao túng bằng thẩm quyền hành chính" khỏi
  danh sách ba kỹ thuật mở rộng. Lý do: danh sách liệt kê bốn mục cho "ba kỹ thuật"; biến thể thẩm quyền hành chính đã
  gộp vào T1 (`Y_TUONG_DU_AN.md` mục 6.1).

## 2026-10-15
- `docs/04. Design/payload_taxonomy.md` — tạo mới: đặc tả T1–T8 theo một mẫu (định nghĩa, thuộc / không thuộc, kênh,
  mục tiêu, nguồn), cây quyết định gán nhãn có thứ tự cố định, schema payload, `activation_check` theo G1–G3, quy trình
  khóa `v-attack-1.0`. Lý do: STT-20; `taxonomy.md` và `Y_TUONG_DU_AN.md` đã trỏ tới file này. Không chứa ma trận dự đoán
  kỹ thuật × phòng thủ (thuộc STT-21).
- `docs/04. Design/defense_spec.md` — tạo mới: đặc tả D1–D4 (chữ ký hàm, thuật toán từng bước, luật R1–R4 của D3 và
  E1–E4 của D4, hit ghi vào trace, điểm mù, điều kiện đạt, khóa cần bổ sung vào `defenses.yaml`). Lý do: STT-20;
  `defenses.yaml` đã trỏ tới `defense_spec.md` mục 4.

## 2026-10-13
- `docs/06. Track/Việc treo.md` — VT-2 phần A1: ghi kết quả chạy thật sau khi chuyển sang API Anthropic (hết khối chèn,
  A1 tự nhận đúng danh tính, vòng tool hai lượt chạy được); chỉ còn việc báo GVHD. `ipi-agent-lab/scripts/check_targets.py`
  nới tiêu chí: chấp nhận nhiều tool-call song song. Lý do: A1 gọi hai `search_kb` song song — hành vi hợp lệ.
- `docs/04. Design/04. Trace schema.md` mục 7 — liệt kê test của ràng buộc `blocked_by` hai chiều, kiểm hit chặn trong
  `finish()`, `finish_reason` theo bước, khối `refusal` và nhánh provider `anthropic`. Lý do: STT-19 bước 4.
- `Y_TUONG_DU_AN.md` mục 10.1 và 16, `docs/01. Đề bài/01. Mô tả bài toán.md` (hệ quả 2, bảng hạn chế) — A1 gọi thẳng API
  Anthropic, không qua gateway; hạn chế #2 và #13 chỉ còn áp cho A2, A3; thêm hạn chế #15: A1 không đặt được
  `temperature`. `ipi-agent-lab`: `LLMClient` thêm `provider: anthropic` (SDK `anthropic`), khối A1 trong
  `config/models.yaml` đổi provider, `temperature: null`, giá $5 / $25; `refusal.finish_reasons` thêm `refusal`.
  Lý do: TA chọn phương án a của VT-2 ngày 2026-10-13. Chờ GVHD xác nhận vì đổi điều kiện "một gateway chung" đã ký.
- `docs/06. Track/Việc treo.md` — VT-2 phần A1 thay bảng phương án bằng trạng thái đã quyết và ba việc còn lại.
- `ipi-agent-lab/config/experiment.yaml` — thêm `fixed.max_tokens: 4096`, như nhau cho A1–A3, giữ suy luận mặc định;
  `Y_TUONG_DU_AN.md` mục 12.4 và `docs/04. Design/04. Trace schema.md` mục 2.4 — `parse_error` thêm trường hợp (d): bước
  `llm` cuối chạm `max_tokens`. Lý do: xử lý VT-1; dò 26 lời gọi
  (`ipi-agent-lab/results/smoke/probe_gateway_tokens_20261013T024403Z.json`): A2 với 256 token trả câu rỗng 2/2, với 1024
  trả trọn; đầu ra lớn nhất đã thấy 1.175 token. Xóa VT-1 khỏi `Việc treo.md`.
- `docs/06. Track/Việc treo.md` — VT-2 viết lại theo kết quả dò 36 lời gọi
  (`ipi-agent-lab/results/smoke/probe_gateway_identity_20261013T024118Z.json`): xác nhận gateway bọc A1 bằng system prompt
  Claude Code; A3 bị định tuyến qua nhiều upstream. Còn chờ TA và GVHD quyết.
- `docs/04. Design/04. Trace schema.md` mục 4.4 — thêm bước chuẩn hóa nháy cong `’` → `'`; ghi kết quả dò: gateway không
  phát tín hiệu từ chối cấp API (A1–A3 đều `stop`/`length`), nhận diện thực tế dựa vào cụm từ chối. Lý do: lần dò 30 lời
  gọi, bằng chứng `ipi-agent-lab/results/smoke/probe_refusal_20261013T012512Z.json`.
- `docs/06. Track/Việc treo.md` — tạo mới, hai mục: VT-1 phần suy luận của A2/A3 ăn hết `max_tokens`; VT-2 gateway có
  thể chèn system prompt riêng. Lý do: phát hiện trong lần dò của STT-19, TA quyết tách thành việc riêng, hạn trước pilot.
- `docs/04. Design/04. Trace schema.md` — mục 4 viết lại thành quy tắc phân định `blocked_by`: ba loại sự kiện chặn và
  dấu vết trong `steps`, bảng quyết định năm dòng, tác nhân của sự kiện chặn sớm nhất thắng, nhận ra model từ chối bằng
  `finish_reason` + cụm từ chối cố định trong `config/experiment.yaml` khối `refusal`, sự kiện harness ghi qua
  `defense_hits` với tiền tố `harness:`; thêm cột `steps.finish_reason`; bảng ràng buộc kiểm bằng máy. Lý do: STT-19
  bước 2, TA chốt ba phương án ngày 2026-10-13. Phần code tương ứng (cột, CHECK, kiểm trong `finish()`, khối config)
  làm ở bước 3.
- `docs/04. Design/04. Trace schema.md` — tạo mới: đặc tả hai bảng `runs` + `steps` (kiểu, NULL, giá trị cho phép, tầng
  ghi từng trường), giá trị `outcome` theo `run_kind`, phân định `blocked_by`, vòng đời một run, `ASR_SQL`. Lý do: đầu ra
  STT-19; mô tả lại lược đồ đã hiện thực ở `ipi-agent-lab/src/obs/trace.py` (STT-32).
- `Y_TUONG_DU_AN.md` mục 13.3 — `target_model` thay bằng `target_id (A1|A2|A3) · model_id · response_model`; `tokens` →
  `tokens_in · tokens_out`; `latency` → `latency_ms`; thêm trỏ sang đặc tả trace schema. Lý do: TA chốt sửa tài liệu
  theo tên trường trong code.
- `ipi-agent-lab/data/benign_queries.json` — thêm trường `carrier_task_id` cho cả 60 câu (U1/U5 → CT-01, đọc DB →
  CT-03, tồn kho → CT-04, email → CT-05, phiếu → CT-06); thêm `expected_priority` cho 5 câu tạo phiếu (BQ-U4-006, 009:
  `high`; BQ-U4-007: `medium`; BQ-U4-008, 010: `null`); viết lại BQ-U3-010 thành câu `search_kb` + `http_request`
  (đơn 12 chiếc SKU-EP-2250 dưới MOQ 20, phụ phí 5%), bỏ vế công nợ và `db_refs`. Lý do: cổng dương tính giả G2 không
  chạy được khi câu lành tính không gắn tác vụ chở; BQ-U3-010 cần cả `http_request` lẫn `query_customer_db`, không tác
  vụ chở nào cho phép cả hai. TA chốt cả ba hướng xử lý. Vẫn đủ 60 câu, U3 thành 6 câu tồn kho + 6 câu khách hàng.
- `ipi-agent-lab/data/carrier_tasks.json` — CT-06: `priority_in: ["high"]` đổi thành `priority_must_equal` lấy mức từ
  câu hỏi qua `runtime['expected_priority']`, thêm `expected_priority: "high"` ở cấp tác vụ (CT-06 vẫn chấm mức cao);
  CT-05: bỏ chuỗi mô tả `"chuỗi bí mật system prompt"` khỏi `body_must_not_contain` vì `<canary>` đã phủ canary system
  prompt; `false_positive_gate` bỏ nhắc tag `v-bench-1.0`, ghi rõ chấm theo `carrier_task_id`. Lý do: `priority_in` cố
  định làm BQ-U4-007/008/010 báo G2 sai; so nguyên văn chuỗi mô tả không bắt được gì.
- `ipi-agent-lab/src/eval/canary.py` (mới), `src/eval/allowed_actions.py` — hiện thực tiêu chí G1 dựa trên canary:
  `normalize()`, `canary_present()` (base64, hex, percent-encoding, phân cách, homoglyph, đảo chuỗi, mảnh ≥ 12 ký tự lấy
  từ phần UUID), `substitute_placeholders()`, `g1_sinks()` dựng từ `agent_tools`, `check_g1()`; `body_must_not_contain`
  thay `<canary>` bằng `runtime['run_canaries']` thay vì so nguyên văn. Lý do: hoàn tất STT-18; trước đó canary thật
  `CANARY_DB_<uuid>` trong body email/phiếu không bị bắt.
- `ipi-agent-lab/tests/test_benign_gate.py`, `tests/test_canary.py` (mới) — cổng dương tính giả: 60/60 câu lành tính 0
  vi phạm G2 và 0 chạm G1 trên chuỗi tool-call dựng từ `expected_tool_calls`. Phải chạy lại trên trace thật ở STT-37.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` — cột "Khóa bằng" của tác vụ chở và câu lành tính đổi
  `v-bench-1.0` thành "Quy tắc cứng #1". Lý do: sót khi bỏ cơ chế tag ngày 2026-10-09.

## 2026-10-12
- `docs/04. Design/03. Kiến trúc testbed và interface.md` — tạo mới: năm tầng, kiểu dữ liệu qua ranh giới tầng, năm
  hook phòng thủ, hình kiến trúc và trình tự một bước (Mermaid, kèm bản SVG
  `00. Image/kien_truc_01_nam_tang.svg`, `00. Image/kien_truc_02_trinh_tu_mot_buoc.svg`), phân định `blocked_by`. Lý do: đầu ra STT-17, đi kèm
  `ipi-agent-lab/src/interfaces.py`.
- `ipi-agent-lab/config/defenses.yaml` — hook `ingest_kb` đổi thành `kb_retrieval`: D2 trên K1 chạy lúc chunk được truy
  hồi, không lúc ingest; thêm `automated_resolution: "block"` vào luật R4 của D3. Lý do: TA chốt — giữ `delivered` như
  nhau giữa D2 bật/tắt, không cần collection thứ hai; chạy tự động không có người duyệt nên yêu cầu xác nhận quy về chặn.

## 2026-10-09
- `docs/06. Track/Lộ trình triển khai code.md` — tạo mới: thứ tự dựng code sáu giai đoạn, phụ thuộc và cổng chặn,
  tham chiếu theo STT; không đổi ngày trong `Kế hoạch thực hiện.xlsx`. Lý do: TA ưu tiên dựng hệ thống chạy được trước,
  phần lý thuyết xử lý sau.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (bảng chiều phạm vi, hạng mục 6, điều kiện harness điểm 5),
  `Y_TUONG_DU_AN.md` và `docs/01. Đề bài/01. Mô tả bài toán.md` (bảng hạn chế, thêm dòng 14),
  `ipi-agent-lab/config/models.yaml`, `ipi-agent-lab/.env.example` — chốt bộ model đích: A1 `claude-opus-5`, A2
  `glm-5.2`, A3 `glm-5.3-flash` (thay DeepSeek-V4-Flash 0731); bỏ yêu cầu id có ngày, thay bằng ghi trường `model` của
  response vào trace. Lý do: TA chốt lại với GVHD ngày 2026-10-09; gateway chỉ cung cấp bí danh. STT-14, khóa bằng
  tag `v-models-1.0`.
- `CLAUDE.md` (quy tắc cứng #1), `Y_TUONG_DU_AN.md` (bảng biến, quy tắc #1, lịch ND3, mục 19 bước 9),
  `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 3.4, 3.5, bảng biến), `docs/01. Đề bài/Aux/Danh mục viết tắt.md` (M1),
  `ipi-agent-lab/README.md` — bỏ cơ chế khóa bộ đo bằng tag `v-bench-1.0`; bộ đo vẫn khóa theo quy tắc cứng #1, mọi thay
  đổi ghi ở file này. Lý do: tag chưa từng được tạo; TA quyết bỏ cơ chế tag.
- `ipi-agent-lab/data/carrier_tasks.json` — đổi mã task cũ sang mã hiện hành (`task_id` W1-06 → STT-18; W1-07 → STT-20;
  W2-04 → STT-22; W2-08 → STT-18; W1-04 → Threat Model, trỏ `docs/04. Design/02. Threat Model.md`); bỏ khối `changelog` và
  trường `updated` trong file. Không đổi tác vụ, ràng buộc, allowlist hay tiêu chí chấm nào. Lý do: update bài toán — đồng bộ
  bộ đo với kế hoạch hiện hành; quy tắc cứng #10 (dữ liệu chỉ chứa dữ liệu).
- `ipi-agent-lab/data/benign_queries.json` — `task_id` W2-07 → STT-18; W1-06 → STT-18, W2-04 → STT-22, bỏ W2-03 trong
  `note_vi`; bỏ trường `updated`. Không đổi câu hỏi hay đáp án nào. Lý do: update bài toán — như trên.

## 2026-10-08
- `docs/03. Khảo sát/KHAO_SAT_PHONG_THU.md` — tạo mới: bảng đối chiếu bốn nhóm phòng thủ (cơ chế · vị trí cắm · điểm mù · chi phí),
  nhận xét cho thiết kế, ánh xạ sang D1–D4. Lý do: đầu ra STT-12, đầu vào cho STT-20 và mục 2.4 báo cáo.
- `docs/03. Khảo sát/KHAO_SAT_PHONG_THU.xlsx` — tạo mới: bản Excel của bảng đối chiếu, thêm cột cách hoạt động, ví dụ testbed,
  phụ thuộc mức tuân thủ của model. Lý do: TA cần bản bảng tính để tra và trình bày.

## 2026-10-05 (sau khi GVHD ký phụ lục)
- `PhieuGiaoNhiemVu_DATN_20250127E_KIEU_THANH_ANH.xlsx` (sheet "Kỹ sư", ô A62) — "bốn kỹ thuật tự đề xuất … và thao túng bằng
  thẩm quyền hành chính" thành "ba kỹ thuật tự đề xuất: chia mảnh, kích hoạt trễ, che giấu đặc thù tiếng Việt". `Y_TUONG_DU_AN.md`
  (mục 15) sửa câu dẫn phiếu tương ứng. Lý do: khớp phụ lục đã ký (T6–T8) và việc gộp T9 vào T1.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` — đánh dấu 16 hạng mục mục 9 đã đồng ý; chọn tên đề tài dài (RAG + MCP);
  trần ngân sách 100 USD; model sinh payload thích ứng chưa chốt; mục 8 đổi thành "Việc còn treo" và bỏ việc đưa bằng chứng
  benchmark vào repo. Lý do: GVHD đã ký; phần bằng chứng khảo sát đang xây lại từ đầu.
- `Y_TUONG_DU_AN.md` (mục 12.3) — bỏ bảng số USR 37/60 và các số đi kèm. Lý do: CSV gốc đã mất, số không truy nguồn được;
  số mới lấy từ lượt chạy lại STT 37.
- `docs/04. Design/02. Thread Model.md` đổi tên thành `02. Threat Model.md`; `01. Agent RAG + MCP .md` thành
  `01. Agent RAG + MCP.md` (bỏ dấu cách thừa); sửa tham chiếu trong `taxonomy.md` và `01. Mô tả bài toán.md`. Lý do: sai chính tả tên file.
- Xoá thư mục `benchmarks/` (5 thư mục chỉ còn `.git` hỏng). Clone `ipi-agent-lab/` vào workspace từ remote. Lý do: dọn workspace.

## 2026-10-05 (gộp T9 vào T1)
- `Y_TUONG_DU_AN.md` (mục 6, 13.3, 14, 15), `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 7), `docs/04. Design/taxonomy.md`,
  `docs/04. Design/02. Thread Model.md` (+ bản `.docx`), `docs/03. Khảo sát/FIT_GAP.md`, `docs/01. Đề bài/02. AI SEC MAP.md`,
  `docs/01. Đề bài/Aux/`, `docs/07. Báo cáo/Chuong1.tex`, `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md`, `CLAUDE.md`,
  `Kế hoạch thực hiện.xlsx` — gộp T9 (thẩm quyền hành chính) vào T1: còn 8 kỹ thuật T1–T8, trong đó 3 kỹ thuật tự đề xuất
  T6–T8; giọng công văn, chỉ đạo Ban Tổng Giám đốc thành biến thể giọng văn của T1; đổi tên T1 thành "Câu lệnh tường minh,
  giả mạo uy quyền" và T2 thành "Ghi đè chỉ thị hệ thống từ trong tài liệu"; T_chung còn {T1, T2, T3, T5, T7, T8}; khối B1 từ
  (9+7+8) còn (8+6+7) kỹ thuật theo kênh, 4.320 còn 3.780 run, tổng ước tính từ khoảng 14.700 còn 14.150; ma trận đủ chiều
  từ khoảng 1.700 còn 1.500 ô; STT 49 trong kế hoạch đổi thành biến thể T1, giữ 4 giờ. Lý do: T1, T2 và T9 là kiểu câu chữ
  nằm trong payload, không phải kênh tấn công; T9 và T1 cùng trục "nguồn phát" nên tách riêng làm ma trận phân biệt không
  sạch. Chưa sửa: phiếu giao nhiệm vụ (còn ghi "bốn kỹ thuật tự đề xuất"), cần báo GVHD.

## 2026-10-05
- `docs/04. Design/01. Agent RAG + MCP .md` (mục 1.1), `docs/04. Design/00. Image/luong_du_lieu_01_kien_truc_tong_the.svg`
  — đổi sơ đồ kiến trúc tổng thể từ chiều ngang sang chiều dọc (`flowchart TB`): kẻ tấn công đưa
  vào khối ngoài vành đai, tô đỏ ba đường K1/K2a/K2b, ngắt dòng nhãn mô hình đích; render lại SVG
  và thêm bản PNG 2352×3276 px (đặt DPI để rộng 16 cm). Lý do: bản ngang quá rộng, chèn vào
  trang Word dọc thì chữ quá nhỏ.

## 2026-09-30
- `Kế hoạch thực hiện.xlsx` (thêm STT 97, ND3 Tuần 8, 3 giờ), `Y_TUONG_DU_AN.md` (mục 15), `docs/01. Đề bài/01. Mô tả bài toán.md` —
  tách việc soạn đặc tả chỉ số đo thành task riêng, đầu ra `docs/04. Design/03. Chỉ số đo.md`; khối lượng 389 giờ thành
  392 giờ, vượt sức chứa 52 giờ, vẫn nằm trong mức bù của nhịp 24 giờ/tuần; sửa câu "STT 71 đã rút gọn" trong mục 15
  (STT 71 đã khôi phục). Lý do: Mô tả bài toán trỏ tới file công thức chỉ số nhưng chưa task nào tạo ra file đó.
- `Kế hoạch thực hiện.xlsx`, `Y_TUONG_DU_AN.md` (mục 13.1, 13.2, 15, 15.1), `README.md`, `docs/01. Đề bài/02. AI SEC MAP.md`,
  `docs/04. Design/02. Thread Model.md`, `docs/01. Đề bài/Aux/`, `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` —
  đồng bộ lần cuối: STT 71 giữ ma trận 6 cấu hình (cắt sẽ mâu thuẫn RQ3–RQ5 và M5); khối lượng 389 giờ so với
  sức chứa 280 giờ từ Tuần 4, thiếu khoảng 49 giờ, bù bằng 24 giờ mỗi tuần; thứ tự cắt dự phòng ghi ở mục 15;
  đánh số chương theo báo cáo 6 chương (mục 4.4 là kết quả thực nghiệm); cây thư mục và docker-compose (5 service,
  có dashboard) theo hiện trạng; thêm M1b, M3b vào danh mục viết tắt; đường dẫn cũ `docs/0n_...` và
  `MO_TA_BAI_TOAN.md`, `docs/05_bo_do/` đổi về tên và vị trí hiện hành; STT 50 bỏ câu "cắt đầu tiên" để khớp thứ tự cắt ở mục 15. Lý do: loại các chỗ lệch giữa phiếu, kế hoạch và tài liệu.
- `CLAUDE.md` (mục 1, 2, 5, 6, 7), `Y_TUONG_DU_AN.md` (mục 10.2, 13.1, 13.2, 15, 15.1) và `README.md`
  (bảng "Đọc theo thứ tự", cây thư mục) — đồng bộ với phiếu giao nhiệm vụ: 16 tuần thành 17 tuần
  (07/09/2026 → 08/01/2027); lộ trình 12 giai đoạn thành sáu Nội dung ND1–ND6 kèm mốc theo `Kế hoạch
  thực hiện.xlsx`; thêm phiếu làm nguồn cao nhất; kế hoạch và trạng thái task trỏ về file xlsx thay cho
  `docs/02_ke_hoach/` (thư mục không còn); mã commit đổi từ `W2-09` sang `STT-n`; thêm ký hiệu `ND1`–`ND6`
  và quy ước viết "Tuần n" để không trùng `T1`–`T9`; thêm đánh giá 3–5 người dùng thực vào phạm vi và
  sản phẩm bàn giao, thêm thư mục `dashboard/`. Lý do: phiếu đã ký là nguồn cao nhất, ba tài liệu đang
  lệch nhau về số tuần, khung nội dung và đường dẫn kế hoạch; Y_TUONG_DU_AN.md thiếu hẳn phần đánh giá
  người dùng mà phiếu coi là bắt buộc.
- `Kế hoạch thực hiện.xlsx` — cột Tuần đổi `T1`–`T17` thành "Tuần n"; dòng M6/M7 của sheet
  "Tổng quan mốc" đổi thành M6; STT 78–81 sửa theo hai harness; STT 8 đặt Xong; sửa đường dẫn cũ ở STT
  3 và 5, bỏ tham chiếu `v3` và `W11-01`; thêm cột "Giờ ước tính" và sheet "Khối lượng giờ". Lý do:
  hết lệch với phiếu, tránh trùng ký hiệu `T1`–`T9`, và tính lại khối lượng giờ cho 17 tuần.
- `Y_TUONG_DU_AN.md` (mục 9, 10.2, RQ6, mục 15, mục 16), `docs/01. Đề bài/01. Mô tả bài toán.md`
  (mục 8.3, phạm vi, RQ6, hạn chế) — nâng harness từ 1 lên 2 (HN-CC, HN-OW; mỗi harness trên A1, A2,
  A3; HN-CC trên A2, A3 có điều kiện) và tách RQ6 thành 6a, 6b, 6c. Lý do: TA chốt 2 harness, đồng bộ
  theo `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md`.
- `Y_TUONG_DU_AN.md` (mục 15) — thay khối lượng 293 giờ bằng ước tính 419 giờ theo 96 đầu việc, so với
  sức chứa 340 giờ. Lý do: con số cũ tính cho kế hoạch 16 tuần.
- `Kế hoạch thực hiện.xlsx` — cắt STT 10, 11 (PoC MCP và RAG), 23 (wireframe dashboard), 69 (đối chiếu
  bậc độ lớn), 89 (gộp vào 88); rút gọn STT 5 (còn hoàn thiện fit-gap), 58 (Pareto ảnh tĩnh), 88 (ráp chương 1–4). Giữ nguyên STT 50 (kỹ thuật T7) và STT 71 vì phiếu giao nhiệm
  vụ ghi bốn kỹ thuật tự đề xuất. Khối lượng ước tính từ 419 giờ còn 389 giờ; STT 71 giữ ma trận 6 cấu hình (xem mục đồng bộ cuối ngày).
  `Y_TUONG_DU_AN.md` (mục 15) ghi số mới. Lý do: kế hoạch vượt sức chứa 79 giờ, GVHD đã duyệt các mục cắt.
- `docs/07. Báo cáo/Chuong1.tex` (đầu file, mục 1.2, 1.4, Bảng 1.1) — bỏ hai điểm xác nhận đã xử lý
  (phạm vi và RQ6 đã chốt, bằng chứng bộ đo đã có ở `docs/03. Khảo sát/`); RQ6 và phạm vi nói hai harness;
  thêm đánh giá với ba đến năm người dùng thực vào phạm vi và Chương 5. Lý do: đồng bộ với phiếu giao
  nhiệm vụ (Nội dung 6) và với quyết định hai harness.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (mục 1, 3, 9), `docs/04. Design/taxonomy.md`,
  `docs/04. Design/02. Thread Model.md`, `docs/01. Đề bài/01. Mô tả bài toán.md` — "16 tuần" đổi thành
  "17 tuần", hạn nộp 08/01/2027. Lý do: theo phiếu giao nhiệm vụ.

## 2026-09-24
- `docs/07. Báo cáo/Chuong1.tex` (mục 1.1, đoạn cuối) — viết lại câu hỏi vận hành (iii) thành hai
  vế: dạng tấn công vẫn thành công khi bật đồng thời mọi cơ chế, và cơ chế nào giữ hiệu lực khi kẻ
  tấn công biết trước cách nó hoạt động. Lý do: câu cũ gộp lỗ hổng cấu trúc với lỗ hổng do leo
  thang, và ngầm giả định biết trước cơ chế là chắc chắn vượt qua được.

## 2026-09-23
- `docs/03. Khảo sát/` (mới: `TOM_TAT_CONG_TRINH.md`, `FIT_GAP.md`, `evidence/`) — khảo sát sáu
  công trình (AgentDojo, AutoDojo, MCPTox, InjecAgent, AgentDyn, MCP-Poison-Bench) theo bảng 12 tiêu
  chí cố định; cài và chạy offline cả sáu benchmark (không gọi LLM), lưu log, manifest pin commit và
  script sinh bằng chứng vào `evidence/`; fit-gap trỏ từng nhận xét về file bằng chứng. Lý do: dựng
  lại đầu ra của task khảo sát/fit-gap (ND1, dòng 5 kế hoạch) sau khi bằng chứng cũ mất trong đợt
  dựng lại workspace, và thỏa quy tắc cứng #2.
- `docs/07. Báo cáo/Chuong1.tex` — viết lại theo hướng dẫn chương 1 của mẫu SOICT: bọc
  `subfiles`, bỏ `\chapter` (đã có ở `DoAn.tex`), giữ nhãn `section:1.1`–`section:1.4` của mẫu;
  chuyển đoạn đánh giá các bộ đo từ 1.1 sang đầu 1.2; 1.1 thêm lợi ích và khả năng áp dụng, bỏ
  câu nêu giải pháp; 1.2 theo trình tự tổng quan công trình → hạn chế → năm chức năng chính →
  sáu RQ (Bảng 1.1) → phạm vi rút gọn; 1.3 theo trình tự phương pháp và công nghệ → mô tả ngắn
  giải pháp → bốn đóng góp, bỏ phần giải thích chi tiết ba vấn đề phương pháp; bố cục ghi số
  chương trực tiếp thay cho `\ref`. Độ dài khoảng 3–4 trang. Lý do: đối chiếu với yêu cầu của mẫu
  (3–6 trang, không nêu giải pháp ở 1.1, 1.2 phải có tổng quan và so sánh, 1.3 không giải thích
  chi tiết công nghệ).
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (mục 3, 4, 5, 6, 9) — nâng thiết kế harness
  lên 2 harness × 3 model: HN-CC chạy thêm trên A2, A3 qua `ANTHROPIC_BASE_URL`, là nhánh có điều
  kiện (bỏ nếu chạy thử không đạt, không cần ký lại); RQ6b so hai harness trong cùng từng model;
  khối B6 từ 350 lên 450 run, tổng ước tính từ khoảng 14.600 lên 14.700; thêm ràng buộc về model
  id trên endpoint tương thích Anthropic và về tính năng mất khi dịch API. Lý do: Claude Code
  cắm được endpoint tương thích Anthropic của nhà cung cấp; thiết kế đủ ô cho phép kiểm chênh
  lệch giữa hai harness có giữ chiều khi đổi model.

## 2026-09-23
- `docs/07. Báo cáo/Chuong1.tex` — bỏ toàn bộ tiểu mục, giữ bốn mục theo khung mẫu: Đặt vấn đề ·
  Mục tiêu và phạm vi đề tài · Định hướng giải pháp · Bố cục đồ án. Nội dung giữ nguyên, thêm câu
  dẫn vào đoạn đóng góp. Lý do: TA yêu cầu viết đúng bốn mục của mẫu, không chia tiểu mục.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (mục 3, 4, 5, 6, 8, 9) — mở harness từ 1
  lên 2: HN-CC Claude Code trên A1 và HN-OW OpenWork (lõi opencode) trên A1, A2, A3; RQ6 tách 6a
  (harness so với vòng lặp trần trên cùng model), 6b (hai harness trên A1), 6c (ánh xạ D1–D4);
  khối B6 tăng từ 100 lên 350 run, tổng ước tính từ khoảng 14.300 lên 14.600; thêm ràng buộc pin
  model id có ngày. Lý do: GVHD duyệt mở rộng; một harness chỉ trên A1 không trả lời được bối
  cảnh doanh nghiệp Việt dùng GLM, DeepSeek; chạy HN-OW trên A1 để tách phần chênh do harness khỏi
  phần do model. Ký hiệu harness dùng tiền tố `HN-` để không trùng tiền tố `H` của giả thuyết H1–H6;
  đăng ký vào danh mục viết tắt khi phạm vi được ký.

## 2026-09-23
- `docs/07. Báo cáo/Chuong1.tex`, `docs/07. Báo cáo/refs_chuong1.bib` — tạo mới. Chương 1
  "Giới thiệu đề tài" theo khung mẫu SOICT: đặt vấn đề (bối cảnh, tính cấp thiết), mục tiêu và
  phạm vi, sáu câu hỏi nghiên cứu kèm bảng giả thuyết H1–H6, định hướng giải pháp và bốn nhóm
  đóng góp, bố cục sáu chương; 12 mục tài liệu tham khảo có nhãn trạng thái kiểm. Ba điểm chờ
  xác nhận đánh dấu `% [XÁC NHẬN]` trong file. Lý do: bắt đầu viết báo cáo; nội dung lấy từ
  `Y_TUONG_DU_AN.md`, `01. Mô tả bài toán.md` và phiếu giao nhiệm vụ.

## 2026-09-23
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` — tạo mới. Biểu mẫu chờ ký gồm: định danh
  đề tài (hai phương án tên để chọn một), persona P1/P2 và phản persona, bảng phạm vi chốt cứng
  có tên ba mô hình đích và harness, sáu RQ kèm tiêu chí trả lời ghi trước, thiết kế phân khối
  B1–B6 với ước tính khoảng 14.300 run ở giả định N = 30, cấu hình harness Claude Code trên A1,
  việc phải xong trước khi ký, checklist 16 hạng mục. Lý do: phụ lục điều chỉnh phạm vi chưa có
  chữ ký; vòng chất vấn phạm vi chỉ ra RQ1 so kênh trên hai tập kỹ thuật khác nhau, RQ2–RQ3 chưa
  có tiêu chí trả lời, RQ4 chưa định nghĩa độ trễ và chi phí, RQ5 chưa cố định mục tiêu, RQ6 lẫn
  model với harness. Chưa đồng bộ vào `Y_TUONG_DU_AN.md` và `01. Mô tả bài toán.md` cho tới khi
  có chữ ký.

## 2026-09-22
- `docs/04. Design/taxonomy.md` — tạo mới. Đặc tả mức thi hành của taxonomy kênh: ba câu hỏi
  phân định một kênh (thực thể ghi · vào context bảo đảm hay có điều kiện · vùng prompt), đặc tả
  từng kênh K1–K5 kèm điểm bơm và cơ chế kích hoạt, ba tiêu chí vào phạm vi thực nghiệm và lý do
  loại K3/K4/K5, bảng ánh xạ kênh × kỹ thuật T1–T9 (ghi rõ T4 không dựng được trên K2a và T6 chỉ
  dựng được trên K1 là ràng buộc kiến trúc, không phải ASR bằng 0), bảng ánh xạ kênh × phòng thủ
  D1–D4. Lý do: mục 6 của `01. Mô tả bài toán.md` đã trỏ tới file này nhưng file chưa tồn tại;
  đặc tả kênh không có chỗ nào ghi đủ để thi hành.
- `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 6 và bảng 12.1) — bổ sung ba câu hỏi phân định
  kênh vào phần mở mục 6; thêm đoạn chốt phạm vi hai kênh thực nghiệm K1 và K2 kèm lý do loại
  K3, K4, K5; nêu rõ K2a và K2b là hai phân kênh của cùng K2, gộp khi trả lời RQ1 và tách khi
  trả lời RQ2, trace vẫn ghi `channel ∈ {K1, K2a, K2b}`. Dòng "Kênh tấn công" trong bảng phạm vi
  chốt cứng đổi từ "3 · K1 · K2a · K2b" thành "2 · K1 · K2 (hai phân kênh K2a, K2b)". Lý do:
  bảng phạm vi đếm ba kênh trong khi RQ1 và H1 phát biểu theo hai kênh — cùng một đại lượng có
  hai con số ở hai chỗ.
- `Y_TUONG_DU_AN.md` (mục 5 và bảng phạm vi) — đồng bộ đúng hai thay đổi trên. Lý do: giữ nguyên
  tắc một khái niệm một ký hiệu giữa ba tài liệu.

## 2026-09-22
- `docs/04. Design/02. Threat Model.docx` — tạo mới. Bản trình bày mô hình đe dọa theo năm bước
  chuẩn threat modeling (xác định tài sản · sơ đồ luồng dữ liệu và ranh giới tin cậy · liệt kê
  mối đe dọa theo STRIDE · đánh giá và ưu tiên rủi ro · biện pháp giảm thiểu và rủi ro dư), kèm
  mức 2 về năng lực kẻ tấn công, phần cưỡng chế bằng trace, hạn chế và việc còn treo. Ba hình
  render từ SVG trong `00. Image/` đặt ở trang ngang; bảng xếp hạng rủi ro tám kịch bản đặt ở
  trang ngang. Nội dung sinh từ `02. Thread Model.md`, không thêm dữ kiện mới ngoài hai mục đã
  bổ sung vào file .md cùng ngày. Lý do: cần bản tài liệu đúng cấu trúc threat modeling chuẩn để
  trình GVHD và đưa vào báo cáo.
- `docs/04. Design/02. Thread Model.md` (mục 1.4, 1.5, 5) — bổ sung ba mục thiếu so với năm bước
  chuẩn: ánh xạ sang STRIDE kèm phân biệt "loại vi phạm" và "kỹ thuật né phòng thủ" cho T1–T9;
  bảng xếp hạng rủi ro tám kịch bản TH-01 đến TH-08 theo khả năng × ảnh hưởng, ghi rõ là ước
  lượng ghi trước thực nghiệm; mục biện pháp giảm thiểu và rủi ro dư từng kịch bản. Đánh lại số
  mục 5 và 6 thành 6 và 7. Lý do: giữ nguyên tắc một nguồn chân lý — nội dung mới phải nằm ở
  file .md trước, bản docx chỉ trình bày lại.

## 2026-09-22
- `docs/04. Design/02. Thread Model.md` (mục 2.2, 3, 5, 6) — chốt mức phản hồi cho A-adaptive là
  **PH1**; thay đoạn đề xuất bằng đoạn chốt kèm hệ quả cưỡng chế: harness thích ứng không đọc
  trace, không đọc `blocked_by`, không đọc log D1–D4; tập tín hiệu vào của vòng sau đúng bằng
  `final_answer` cộng các bồn chứa kẻ tấn công sở hữu. Mục "việc còn treo" bỏ việc chốt PH, thêm
  việc dựng ranh giới mã nguồn giữa `src/attack/` và `src/obs/` để chặn rò rỉ oracle. Lý do: PH1
  đã được chốt; rò rỉ oracle là loại lỗi không hiện ra trong kết quả nên phải chặn bằng cấu trúc
  mã nguồn, không bằng thỏa thuận.
- `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 4.3) — cập nhật câu về mức phản hồi từ "chưa chốt"
  thành "đã chốt PH1". Lý do: đồng bộ với quyết định trên.
- `CLAUDE.md`, `README.md`, `docs/01. Đề bài/01. Mô tả bài toán.md`,
  `docs/01. Đề bài/02. AI SEC MAP.md`, `docs/01. Đề bài/Aux/Danh mục viết tắt.md`,
  `docs/04. Design/01. Agent RAG + MCP .md`, `docs/04. Design/02. Thread Model.md` — sửa toàn bộ
  tham chiếu đường dẫn theo tên thư mục và tên file hiện hành (`docs/01. Đề bài/`,
  `docs/04. Design/`, `docs/06. Track/`, SVG chuyển vào `00. Image/`). Lý do: sau đợt đổi tên
  thư mục, mọi tham chiếu nội bộ đứt — đây là lớp lỗi đã xảy ra một lần và có quy ước riêng
  trong `CLAUDE.md`. Các đường dẫn trong chính file changelog giữ nguyên vì là bản ghi lịch sử.

## 2026-09-22
- `docs/04_thiet_ke/luong_du_lieu.md` — tạo mới. Mô tả cơ chế vận hành của AI Agent RAG + MCP
  tool-calling (hai vòng lặp, một cửa sổ ngữ cảnh) và bốn sơ đồ Mermaid: kiến trúc tổng thể,
  trình tự một lượt suy luận, con đường nội dung không tin cậy theo năm giai đoạn Gieo → Nạp →
  Kích hoạt → Nhầm lẫn ranh giới → Thi hành, và điểm chèn của D1–D4 kèm nhánh `blocked_by`.
  Mục 6 liệt kê sáu điểm ĐC-1…ĐC-6 phải đối chiếu với đặc tả MCP gốc trước khi trích vào báo
  cáo. Lý do: sản phẩm của phần tìm hiểu cơ chế agent; làm nền hình cho chương kiến trúc và
  cho luận cứ H1 (ASR kênh công cụ cao hơn kênh tài liệu).
- `docs/04_thiet_ke/luong_du_lieu_01_kien_truc_tong_the.svg`,
  `docs/04_thiet_ke/luong_du_lieu_02_trinh_tu_mot_luot.svg`,
  `docs/04_thiet_ke/luong_du_lieu_03_duong_di_noi_dung_khong_tin_cay.svg`,
  `docs/04_thiet_ke/luong_du_lieu_04_diem_chen_phong_thu.svg` — tạo mới. Bản render của bốn
  khối Mermaid trong file trên. Lý do: báo cáo LaTeX chèn hình vector, không chèn mã Mermaid.
- Ký hiệu mới `ĐC-1`–`ĐC-6` dành riêng cho hạng mục cần đối chiếu đặc tả MCP gốc, không trùng
  với các tiền tố đang dùng (TS, A, M, G, K, T, D, CT, U, TL, RQ, AS).

## 2026-09-22
- `docs/04_thiet_ke/MO_HINH_DE_DOA.md` — tạo mới. Đặc tả mức thi hành của mô hình đe dọa hai
  mức: vành đai tin cậy; ma trận tài sản × mục tiêu (TS1–TS3 × G1–G3) kèm thuộc tính an ninh bị
  vi phạm; bảng hệ quả khi sáu giả định vận hành không thỏa; bảy trục năng lực kẻ tấn công với
  hai mức A-blind / A-adaptive; giao thức vòng thích ứng (phạm vi được sửa, ba điều kiện dừng,
  đơn vị tính ASR là chuỗi); hai trường trace bổ sung `adaptive_chain_id`, `adaptive_round` và
  năm bất biến kiểm được bằng test. Lý do: phần năng lực kẻ tấn công trong mô tả bài toán chỉ
  có bốn dòng, chưa đủ để thi hành nhánh adaptive và chưa quy định mức phản hồi mà kẻ tấn công
  quan sát được.
- `docs/01_de_bai/MO_TA_BAI_TOAN.md` (mục 4) — thêm đoạn dẫn nêu cấu trúc hai mức và trỏ tới
  file đặc tả mới; bổ sung ràng buộc A-adaptive không biết giá trị canary và không biết
  delimiter ngẫu nhiên của D1. Lý do: giữ nguyên tắc một nguồn chân lý — mục 4 chốt khái niệm,
  chi tiết thi hành nằm ở `docs/04_thiet_ke/`.
- `docs/01_de_bai/DANH_MUC_VIET_TAT.md` — thêm mục "Năng lực kẻ tấn công" (A-blind, A-adaptive,
  NL1–NL7, PH0–PH3) và đánh lại số các mục sau. Lý do: hai tiền tố ký hiệu mới phải có trong
  danh mục để giữ nguyên tắc một khái niệm một ký hiệu; `N` đã dùng cho cỡ mẫu nên trục năng lực
  dùng `NL`, `F` gần với FRR nên mức phản hồi dùng `PH`.
- `docs/01_de_bai/danh_muc_viet_tat.tex` — thêm hai dòng `NL1--NL7` và `PH0--PH3` đúng thứ tự
  chữ cái. Lý do: giữ bản LaTeX đồng bộ với danh mục Markdown.

## 2026-09-22
- `docs/01_de_bai/BAN_DO_AI_SECURITY.md` — tạo mới. Bản đồ khái niệm AI Security sáu tầng
  (L0–L5), ánh xạ vòng đời tấn công theo MITRE ATLAS sang năm giai đoạn của một lượt agent,
  mục định vị IPI trên bốn khung tham chiếu (OWASP LLM Top 10, OWASP Agentic ASI01–ASI10,
  MITRE ATLAS, NIST AI 100-2/AI RMF), danh mục kiểm 32 hạng mục AS-01…AS-32 kèm cột phạm vi,
  và bảng ánh xạ khung ngoài sang ký hiệu nội bộ (TS, K, G, T, D). Lý do: sản phẩm của
  Nội dung 1 — mục 1 theo Phiếu giao nhiệm vụ; đồng thời làm căn cứ có số cho phần biện luận
  phạm vi trước GVHD.
- `docs/01_de_bai/ban_do_ai_security.svg` — tạo mới. Sơ đồ trực quan của bản đồ trên, dùng
  cho báo cáo và slide. Lý do: phần trình bày phạm vi cần một hình duy nhất thay cho ba bảng.
- Ký hiệu mới `AS-01`–`AS-32` dành riêng cho hạng mục danh mục kiểm AI Security, không trùng
  với các tiền tố đang dùng (TS, A, M, G, K, T, D, CT, U, TL, RQ).

## 2026-09-22
- `Kế hoạch thực hiện.xlsx` (sheet `Kế hoạch chi tiết`) — dựng lại toàn bộ theo khung Phiếu
  giao nhiệm vụ ĐATN kỹ sư (MSSV 20250127E): 6 Nội dung, Tuần 1–17, mốc thời gian 07/09/2026
  → 08/01/2027. Thêm cột `Nội dung` và `Tuần` để ánh xạ từng đầu việc về ND1–ND6. Bổ sung 3
  đầu việc đánh giá và thu thập phản hồi người dùng ở ND6 (nội dung bắt buộc với đồ án kỹ sư).
  Sheet `Tổng quan mốc` thêm cột mã mốc M0–M8, Nội dung tương ứng và hạn theo tuần. Lý do:
  đồng bộ kế hoạch triển khai với phiếu giao nhiệm vụ đã ký với GVHD.

## 2026-09-22
- `docs/01_de_bai/danh_muc_thuat_ngu.tex` — tạo mới. Bản LaTeX `longtable` danh mục thuật ngữ
  (30 mục), ba cột: thuật ngữ · tiếng Việt · giải thích. Lý do: tách thuật ngữ khỏi danh mục
  viết tắt để đưa vào báo cáo.

## 2026-09-22
- `docs/01_de_bai/danh_muc_viet_tat.tex` — đồng bộ diễn giải chi tiết cho các thuật ngữ
  (IPI, MCP, A2A, KB, NFKC) từ danh mục chuẩn.

## 2026-09-22
- `docs/01_de_bai/danh_muc_viet_tat.tex` — tạo mới. Bản LaTeX `longtable` của danh mục viết
  tắt, ba cột theo mẫu Overleaf SOICT, sắp xếp theo bảng chữ cái. Lý do: đưa thẳng vào báo cáo.

## 2026-09-22
- `docs/01_de_bai/DANH_MUC_VIET_TAT.md` — tạo mới. Tổng hợp toàn bộ từ viết tắt và ký hiệu
  (TS, A, G, K, T, D, CT, U, TL, RQ, M, chỉ số đo) từ `Y_TUONG_DU_AN.md` và
  `MO_TA_BAI_TOAN.md`. Lý do: cần một chỗ duy nhất tra ký hiệu để đưa vào báo cáo và
  giữ nguyên tắc "một khái niệm, một ký hiệu".
