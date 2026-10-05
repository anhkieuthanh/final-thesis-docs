# Chạy benchmark có LLM (mức L3) — TA tự chạy

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Claude không chạy các lệnh này vì cần API key và ngân sách. Trước khi chạy: hạn mức đã có trong `cost_budget.md` (quy tắc vận hành: kiểm chi phí mỗi 2 giờ trong 4 giờ đầu, vượt 120% dự toán thì dừng).

## Nguyên tắc

- Export key trong shell hiện tại, **không** ghi vào file trong repo, không sửa `.env` của lab.
- Chạy lô nhỏ trước (1 suite, vài user task), đọc trace của vài ca thất bại trước khi kết luận về model (bài học #4).
- Chép toàn bộ thư mục `runs/` sinh ra vào `evidence/<benchmark>/llm_runs/<model>/` kèm một `run_manifest.txt` mới ghi model, ngày, lệnh, chi phí thực.

## AgentDojo (commit `089ed468`)

Luôn truyền `--benchmark-version v1.2.2` để khớp bản đã kiểm offline (mặc định của CLI là `v1.2`).

```bash
cd benchmarks/agentdojo && git checkout 089ed468cf3ed0322acc66b0211f26d9d90dbf60
uv venv .venv && uv pip install -p .venv/bin/python -e .
export OPENAI_API_KEY=...          # hoặc dùng gateway, xem dưới
# Lô thử: utility, 1 suite, 3 user task
.venv/bin/python -m agentdojo.scripts.benchmark --benchmark-version v1.2.2 \
  -s banking -ut user_task_0 -ut user_task_1 -ut user_task_2 \
  --model GPT_4O_MINI_2024_07_18 --logdir runs
# Lô tấn công: 1 suite, attack chuẩn
.venv/bin/python -m agentdojo.scripts.benchmark --benchmark-version v1.2.2 \
  -s banking --model GPT_4O_MINI_2024_07_18 \
  --attack important_instructions --logdir runs
```

Qua gateway tương thích OpenAI (dùng chung cho A1–A3):

```bash
export OPENAI_COMPATIBLE_BASE_URL=...   OPENAI_COMPATIBLE_API_KEY=...
.venv/bin/python -m agentdojo.scripts.benchmark --benchmark-version v1.2.2 \
  -s banking --model OPENAI_COMPATIBLE --model-id <tên model trên gateway> \
  --attack important_instructions --logdir runs
```

Mốc chi phí tác giả công bố: khoảng 35 USD cho 629 ca trên GPT-4o (bài báo, Phụ lục D). Banking đủ cặp là 144 ca.

## AutoDojo

```bash
cd benchmarks/AutoDojo   # commit trong evidence/autodojo/run_manifest.txt
python -m agentdojo.scripts.benchmark --model openai/gpt-4o-mini --suite banking \
  --attack important_instructions --defense datafilter --logdir runs
```

Vòng tối ưu (`optimize_variants.py`) gọi thêm optimizer LLM qua OpenRouter; xem `agentdojo/variant_generation/README.md` của repo trước khi chạy và cộng chi phí optimizer vào dự toán.

## MCPTox

Repo không có runner. Muốn đạt L3 phải tự viết adapter đưa `(system prompt sạch + poisoned tool, query)` vào model và đọc tool-call đầu ra — đây là việc của task Adapter MCPTox (kế hoạch, dòng 39), chỉ chạy **chế độ mô phỏng**, không kết nối MCP server thật (quy tắc #7).

## InjecAgent

```bash
cd benchmarks/InjecAgent && export PYTHONPATH=. && pip install -r requirements.txt
python3 src/evaluate_prompted_agent.py --model_type GPT --model_name gpt-4o-mini --setting base --prompt_type InjecAgent
```

Kiểm lại tên tham số bằng `--help` trước khi chạy; bước 2 của data stealing gọi thêm GPT-4 để mô phỏng phản hồi tool.

## MCP-Poison-Bench

```bash
cd benchmarks/MCP-Poison-Bench && . .venv/bin/activate
export OPENAI_API_KEY=...
python -m harness.runner --server servers/poisoned/server.py --task tasks/notes_pipeline.json \
  --model gpt-4o-mini --seed 42 --poison-class rug_pull
```

## AgentDyn

Chưa nên chạy L3: ground truth của cả ba suite lỗi khi chạy offline (`agentdyn/check_suites_upstream_locked.log`), nên không có cách tự kiểm bộ chấm trước khi tốn tiền.
