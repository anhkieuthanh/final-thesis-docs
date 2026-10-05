"""InjecAgent — chạy offline: nạp 4 tập test case, đếm theo loại tấn công / user tool / attacker tool,
kiểm tỉ lệ ca mà 'Tool Response' đã được điền sẵn (tức là phản hồi tool là tĩnh, mô phỏng trước).
KHÔNG gọi LLM. Soạn với hỗ trợ AI (Claude)."""
import json, sys, collections, datetime
from pathlib import Path
R = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
C = collections.Counter; res = {"run_at_utc": datetime.datetime.utcnow().isoformat()+"Z", "sets": {}}
allcases = []
for name in ["test_cases_dh_base", "test_cases_dh_enhanced", "test_cases_ds_base", "test_cases_ds_enhanced"]:
    d = json.load(open(R/"data"/f"{name}.json")); allcases += [(name, x) for x in d]
    res["sets"][name] = {"n": len(d), "attack_type": C(x["Attack Type"] for x in d),
        "n_user_tools": len({x["User Tool"] for x in d}),
        "n_attacker_tools": len({t for x in d for t in x["Attacker Tools"]}),
        "n_multi_step_attacker_tools": sum(len(x["Attacker Tools"]) > 1 for x in d),
        "tool_response_prefilled": sum(bool(x.get("Tool Response")) for x in d),
        "thought_prefilled": sum(bool(x.get("Thought")) for x in d)}
base = [x for n, x in allcases if n.endswith("_base")]
res["base_total"] = len(base)
res["base_unique_user_tools"] = len({x["User Tool"] for x in base})
res["base_unique_attacker_tools"] = len({t for x in base for t in x["Attacker Tools"]})
enh = json.load(open(R/"data"/"test_cases_dh_enhanced.json"))[0]
bas = json.load(open(R/"data"/"test_cases_dh_base.json"))[0]
res["enhanced_vs_base_example"] = {"base_tool_response": bas["Tool Response"][:400], "enhanced_tool_response": enh["Tool Response"][:600]}
res["tools_json_entries"] = len(json.load(open(R/"data"/"tools.json")))
(OUT/"inventory.json").write_text(json.dumps(res, indent=2, ensure_ascii=False))
print(json.dumps(res, indent=1, ensure_ascii=False))
