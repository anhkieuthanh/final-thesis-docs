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

**A1 — đã quyết và đã chạy được, chờ GVHD.** TA chọn gọi A1 thẳng Messages API của Anthropic (2026-10-13).
Đã làm: `LLMClient` có nhánh `provider: anthropic` dùng SDK chính thức; khối A1 trong
`config/models.yaml` bỏ gateway, `temperature: null` (`claude-opus-5` trả 400 khi có tham số này),
giá $5 / $25 mỗi triệu token; `stop_reason = refusal` của API thành tín hiệu từ chối cấp API; hạn
chế #2, #13 sửa lại và thêm #15 trong `Y_TUONG_DU_AN.md` mục 16 và `01. Mô tả bài toán.md`.
Đã kiểm chạy thật (2026-10-13, `ipi-agent-lab/results/smoke/`): `check_targets_20261013T030145Z.json`
đạt; `probe_gateway_identity_20261013T030241Z.json` — `prompt_tokens` khớp request (50 token cho
câu ngắn, trước là 12.196), A1 tự nhận là Claude của Anthropic, không có chỉ dẫn hay công cụ nào
ngoài thứ testbed gửi; vòng gọi tool hai lượt chạy được khi gửi lại block gốc.

Còn lại: báo GVHD: A1 rời "một gateway chung" — `Chốt phạm vi và checklist ký GVHD.md` (điều kiện
   harness, điểm 3 và 5) và hạn chế #2 đều giả định cả ba target qua gateway; xin xác nhận bằng
   văn bản. `model_id` không đổi nên `v-models-1.0` giữ nguyên.

**Phương án cho A3:**
1. Hỏi gateway có tham số ghim nhà cung cấp upstream không (kiểu định tuyến `provider` của các
   gateway tổng hợp). Có thì ghim một nơi, dò lại.
2. Không ghim được: trace đã ghi `response_model` — chuẩn hóa nhãn upstream, báo cáo tỉ lệ run theo
   upstream ở mỗi ô, và khai thành hạn chế.

**Hạn:** trước pilot (STT-60).

---

## VT-4. Preset `d3_no_confirm` — chờ GVHD đồng ý đưa vào ma trận

**Phát hiện ở:** STT-21, lúc dựng ô cấu trúc của ma trận dự đoán.

**Bằng chứng:** `config/defenses.yaml` — R4 bật, `consequential_severities: [internal_write, external_action]`,
`automated_resolution: "block"` ⇒ D3 chặn mọi `send_email`, `http_request`, `create_ticket`, hợp lệ hay không
(`defense_spec.md` mục 5.2).

**Hệ quả:** ở `d3_only`, ASR của D3 trên mọi bồn ghi/ra ngoài gần 0 theo thiết kế, FRR trên CT-05, CT-06, U4 bằng 100%;
không tách được hiệu lực R1–R3; H4 được "xác nhận" vô nghĩa; đường Pareto của D3 suy biến.

**Đã làm:** khai preset `d3_no_confirm` trong `config/defenses.yaml` (khối `preset_overrides` tắt R4), kiểm bằng
`eval.experiment.validate`. **Chưa** đưa vào khối nào của `experiment.yaml`, chưa có trong dự toán.

**Cần GVHD:** đồng ý thêm một cấu hình vào B2/B3 (6 → 7 preset, khoảng +17% số run của hai khối), kết quả báo cáo dạng
khám phá vì ma trận `v-pred-1.0` không có dự đoán cho nó. Không đồng ý thì xóa preset và ghi thành hạn chế: D3 chỉ
đo với R4 chặn tự động.

**Hạn:** buổi họp GVHD kế tiếp, trước khi chốt dự toán chạy ma trận.
