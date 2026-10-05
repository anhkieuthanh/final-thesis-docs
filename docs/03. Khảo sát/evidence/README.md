# Bằng chứng chạy thật — chỉ mục

> Tài liệu soạn với sự hỗ trợ của AI (Claude). Thư mục này là nơi duy nhất `FIT_GAP.md` được phép trỏ tới khi nhận xét về một benchmark (quy tắc cứng #2). Mọi file ở đây là đầu ra thô của script, không sửa tay.

## Quy ước

- Mỗi thư mục con có `run_manifest*.txt`: repo, commit đã pin, máy chạy, phiên bản Python, lệnh đã chạy, số lời gọi LLM (bằng 0 ở mọi lần chạy hiện có).
- Mã nguồn benchmark **không** nằm trong repo này: clone vào `benchmarks/` (bị `.gitignore`) rồi `git checkout <commit>` theo manifest.
- Script sinh bằng chứng nằm ở `scripts/`; chạy lại đúng lệnh trong manifest sẽ tái sinh file tương ứng (trừ trường thời gian).

## Chỉ mục mã bằng chứng dùng trong `FIT_GAP.md`

| Mã | Benchmark | File | Nội dung |
|---|---|---|---|
| E-1 | AgentDojo `ethz-spylab/agentdojo@089ed468` | `agentdojo/inventory_all.json`, `agentdojo/check_suites_upstream.log`, `agentdojo/run_manifest_device.txt` | 4 suite v1.2.2: 74 tool (cộng theo suite; 69 tên không trùng), 97 user task, 35 injection task, 949 cặp; ground truth giải 97/97 user task; kiểm injectable: bản gốc 0/97, bản sửa 97/97 |
| E-1b | AgentDojo | `agentdojo/injection_tasks_gt_all.csv`, `agentdojo/workspace_v1_2_empty_ground_truth.txt` | 8/35 injection task (workspace 6–13) có `ground_truth() = []` |
| E-2 | AgentDojo | `agentdojo/delivered_gt_all.csv`, `agentdojo/payload_samples_all.csv`, `agentdojo/meta_all.json`, `agentdojo/offline_run_full.log`, `agentdojo/run_manifest_cloud.txt` | 5 attack × 949 cặp chạy bằng `GroundTruthPipeline`: payload tới tool output 4.745/4.745 sau chuẩn hóa; khớp literal chỉ 1.004/4.745 (travel 700/700, banking 168/720, slack 276/525, workspace 0/2.800); 175 mẫu payload; 17 attack đăng ký |
| E-3 | AutoDojo `xhOwenMa/AutoDojo` | `autodojo/inventory.json`, `autodojo/injection_files.csv` | 150 file payload tối ưu, 38.000 biến thể; nhãn mức đặc tả tác vụ |
| E-4 | MCPTox `zhiqiangwang4/MCPTox-Benchmark` | `mcptox/inventory.json`, `mcptox/payload_index.csv` | 485 payload, 45 server, phân bố khuôn 77/183/225; dữ liệu phát hành 1.348 instance, 11 model; không có file giấy phép |
| E-5 | InjecAgent `uiuc-kang-lab/InjecAgent` | `injecagent/inventory.json` | 1.054 ca base (510 DH + 544 DS), 17 user tool, 63 attacker tool; phản hồi tool viết sẵn 100% |
| E-6 | MCP-Poison-Bench `chirag-dewan/MCP-Poison-Bench` | `mcp_poison_bench/pytest.log`, `mcp_poison_bench/inventory.json` | 463 test qua offline; 5 lớp tấn công, 3 mục tiêu, register seen/held-out |
| E-7 | AgentDyn `SaFo-Lab/AgentDyn` | `agentdyn/check_suites_upstream_locked.log`, `agentdyn/inventory_shopping.json`, `agentdyn/injection_tasks_gt_shopping.csv`, `agentdyn/released_runs_inventory.json` | shopping: 39 tool, 20 user task, 9 injection task, 28 vector, ground truth 0/20; github và dailylife crash khi nạp; 47.723 log phát hành |
| E-8 | 5 benchmark | `vietnamese_check/result.log`, `scripts/vietnamese_check.py` | Số payload chứa ký tự đặc thù tiếng Việt: 0 ở cả năm bộ đã kiểm |

## Hai lần chạy AgentDojo

- `run_manifest_device.txt`: `check_suites` gốc trên máy TA — nguồn của phát hiện "script kiểm suite báo sai".
- `run_manifest_cloud.txt`: lô đầy đủ 4 suite × 5 attack trên workspace cloud của Claude (máy TA giới hạn 180 giây mỗi lệnh, không đủ cho suite workspace). Script dùng là `scripts/agentdojo_offline.py`, cùng sha256 ghi trong manifest.

## Chưa có

Không có lần chạy nào gọi LLM. Hướng dẫn chạy có LLM: `RUN_WITH_LLM.md`.
