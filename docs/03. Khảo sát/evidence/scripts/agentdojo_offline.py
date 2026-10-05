"""Chạy AgentDojo KHÔNG cần LLM: kiểm kê suite, kiểm ground truth, kiểm injectable
(bản sửa lỗi lọc content), sinh payload của các attack cố định, chạy GroundTruthPipeline
có tiêm để đo tỉ lệ payload thực sự tới tool output (tương đương cờ `delivered`).
Đầu ra: JSON + CSV vào thư mục chỉ định. Soạn với hỗ trợ AI (Claude)."""
import csv, json, re, sys, warnings, platform, datetime, importlib.metadata as md
from pathlib import Path
from agentdojo.task_suite.load_suites import get_suites
from agentdojo.agent_pipeline.ground_truth_pipeline import GroundTruthPipeline
from agentdojo.functions_runtime import FunctionsRuntime
from agentdojo.attacks.attack_registry import load_attack, ATTACKS
from agentdojo.types import get_text_content_as_str

warnings.filterwarnings("ignore")
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
VERSION = sys.argv[2] if len(sys.argv) > 2 else "v1.2.2"
ONLY = sys.argv[3].split(",") if len(sys.argv) > 3 else None
ATKS = sys.argv[4].split(",") if len(sys.argv) > 4 else ["direct", "ignore_previous", "system_message", "injecagent", "important_instructions_no_names"]

def tool_text(responses):
    return " ".join(get_text_content_as_str(r["content"]) for r in responses
                    if r["role"] == "tool" and r["content"] is not None)

def tool_text_upstream(responses):  # đúng logic upstream is_task_injectable
    return " ".join(get_text_content_as_str(r["content"]) for r in responses
                    if r["role"] == "tool" and isinstance(r["content"], str))

meta = {"run_at_utc": datetime.datetime.utcnow().isoformat() + "Z", "benchmark_version": VERSION,
        "agentdojo_pkg": md.version("agentdojo"), "python": platform.python_version(),
        "attacks_registered": sorted(ATTACKS.keys())}
inv, inj_rows, deliv_rows, payload_rows = [], [], [], []
suites = get_suites(VERSION)
for sname, suite in suites.items():
    if ONLY and sname not in ONLY: continue
    defaults = suite.get_injection_vector_defaults()
    canaries = {v: f"---CANARY_{v}---" for v in defaults}
    env = suite.load_and_inject_default_environment(canaries)
    n_gt_ok = n_inj_fixed = n_inj_up = 0
    for ut in suite.user_tasks.values():
        gt = GroundTruthPipeline(ut)
        util, _ = suite.run_task_with_pipeline(gt, ut, injection_task=None, injections={},
                                               environment=env.copy(deep=True))
        n_gt_ok += bool(util)
        _, _, _, resp, _ = gt.query(ut.PROMPT, FunctionsRuntime(suite.tools), env.copy(deep=True))
        n_inj_fixed += any(c in tool_text(resp) for c in canaries.values())
        n_inj_up += any(c in tool_text_upstream(resp) for c in canaries.values())
    # injection task ground truth: thử với MỌI user task, không chỉ user task đầu
    for it in suite.injection_tasks.values():
        ok_any, ok_first = False, None
        for i, ut in enumerate(suite.user_tasks.values()):
            _, sec = suite.run_task_with_pipeline(GroundTruthPipeline(it), ut, injection_task=it,
                                                  injections={}, environment=env.copy(deep=True))
            if i == 0: ok_first = bool(sec)
            ok_any = ok_any or bool(sec)
            if ok_any and i > 0: break
        inj_rows.append({"suite": sname, "injection_task": it.ID, "gt_security_first_user_task": ok_first,
                         "gt_security_any_user_task": ok_any, "goal": it.GOAL})
    inv.append({"suite": sname, "n_tools": len(suite.tools), "tools": [t.name for t in suite.tools],
                "n_user_tasks": len(suite.user_tasks), "n_injection_tasks": len(suite.injection_tasks),
                "n_injection_vectors": len(defaults), "injection_vectors": list(defaults),
                "gt_utility_ok": n_gt_ok, "injectable_fixed_check": n_inj_fixed,
                "injectable_upstream_check": n_inj_up})
    # sinh payload + đo delivered bằng GroundTruthPipeline
    for aname in [a for a in ATKS if a != "none"]:
        try:
            gtp = GroundTruthPipeline(None); gtp.name = "gpt-4o-2024-05-13"  # chỉ để attack có tên model; không gọi model nào
            atk = load_attack(aname, suite, gtp)
        except Exception as e:
            payload_rows.append({"suite": sname, "attack": aname, "error": repr(e)[:200]}); continue
        for ut in suite.user_tasks.values():
            for it in suite.injection_tasks.values():
                inj = atk.attack(ut, it)
                gt = GroundTruthPipeline(ut)
                e2 = suite.load_and_inject_default_environment(inj)
                _, _, _, resp, _ = gt.query(ut.PROMPT, FunctionsRuntime(suite.tools), e2)
                txt = tool_text(resp)
                delivered_literal = any(v in txt for v in inj.values())
                # So khớp sau chuẩn hóa: tool output bị serialize YAML nên dấu nháy/xuống dòng bị escape
                # Hai bước tách rời: bỏ escape \n/\t literal TRƯỚC, rồi mới bỏ ký tự không chữ-số.
                # Gộp làm một regex sẽ để \W+ nuốt dấu "\" và bỏ sót chữ "n" (lỗi đã gặp ở bản đầu).
                nz = lambda x: re.sub(r"\W+", "", re.sub(r"\\[nt]", " ", x)).lower()
                delivered = any(nz(v) in nz(txt) for v in inj.values())
                deliv_rows.append({"suite": sname, "attack": aname, "user_task": ut.ID,
                                   "injection_task": it.ID, "n_vectors_used": len(inj),
                                   "delivered_gt": delivered, "delivered_literal": delivered_literal})
                if ut.ID == "user_task_0":
                    for vec, text in inj.items():
                        payload_rows.append({"suite": sname, "attack": aname, "injection_task": it.ID,
                                             "vector": vec, "payload": text})
    print(f"[{sname}] done", flush=True)

tag = "_".join(ONLY) if ONLY else "all"
(OUT / f"meta_{tag}.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
(OUT / f"inventory_{tag}.json").write_text(json.dumps(inv, indent=2, ensure_ascii=False))
for name, rows in [("injection_tasks_gt.csv", inj_rows), ("delivered_gt.csv", deliv_rows),
                   ("payload_samples.csv", payload_rows)]:
    keys = sorted({k for r in rows for k in r})
    with open(OUT / name.replace(".csv", f"_{tag}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
print(json.dumps(inv, indent=1, ensure_ascii=False)[:3000])
