"""MCPTox — chạy offline: nạp dữ liệu công bố, kiểm kê payload theo server/paradigm/rủi ro,
kiểm def_tool/*.py khớp pure_tool.json, và thống kê nhãn trong response_all.json.
KHÔNG gọi LLM, KHÔNG kết nối MCP server nào (quy tắc cứng #7). Soạn với hỗ trợ AI (Claude)."""
import json, sys, collections, ast, datetime
from pathlib import Path
R = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
p = json.load(open(R/"pure_tool.json")); resp = json.load(open(R/"response_all.json"))
recs = [dict(id=k, **v) for item in p for k, v in item.items()]
C = collections.Counter
inv = {"run_at_utc": datetime.datetime.utcnow().isoformat()+"Z",
       "n_payload_records": len(recs), "n_servers": len({r["server_name"] for r in recs}),
       "by_paradigm": C(r["paradigm"] for r in recs), "by_security_risk": C(r["security risk"] for r in recs),
       "tool_content_len_chars": {"min": min(len(r["tool_content"]) for r in recs),
                                  "max": max(len(r["tool_content"]) for r in recs),
                                  "mean": round(sum(len(r["tool_content"]) for r in recs)/len(recs),1)},
       "response_all_top_keys": list(resp.keys()), "response_all_data_length": resp.get("data_length"),
       "label_scopes": resp.get("label_scopes"), "call_behaviors": resp.get("call_behaviors"),
       "license_file_present": any((R/n).exists() for n in ["LICENSE","LICENSE.md","LICENCE","COPYING"])}
# def_tool: parse AST, đếm file, khớp docstring với tool_content
defs = {}
for f in sorted((R/"def_tool").glob("*.py")):
    t = ast.parse(f.read_text())
    for n in ast.walk(t):
        if isinstance(n, ast.FunctionDef): defs[f.stem] = (n.name, (ast.get_docstring(n) or "").strip())
norm = lambda x: " ".join(x.split())
contents = {norm(r["tool_content"]) for r in recs}
inv["def_tool_files"] = len(defs)
inv["def_tool_docstring_matches_pure_tool"] = sum(norm(d[1]) in contents for d in defs.values())
# servers trong response_all
srv = resp.get("servers", {})
inv["servers_in_response_all"] = len(srv)
sample = next(iter(srv.values())); inv["server_record_keys"] = list(sample.keys())
def walk_labels(o, c):
    if isinstance(o, dict):
        for k, v in o.items():
            if k.lower() in ("label", "labels") and isinstance(v, str): c[v] += 1
            walk_labels(v, c)
    elif isinstance(o, list):
        for v in o: walk_labels(v, c)
per_model = collections.defaultdict(C); n_inst = n_datas = 0; paradigm_inst = C()
for sv in srv.values():
    for mi in sv.get("malicious_instance", []):
        n_inst += 1; paradigm_inst[mi.get("metadata", {}).get("paradigm")] += 1
        for dt in mi.get("datas", []):
            n_datas += 1
            for m, l in (dt.get("label") or {}).items(): per_model[m][l] += 1
inv["released_malicious_instances"] = n_inst
inv["released_malicious_instances_by_paradigm"] = paradigm_inst
inv["released_query_cases"] = n_datas
inv["released_label_counts_per_model"] = {m: dict(c) for m, c in per_model.items()}
inv["NOTE"] = "released_label_counts_* la nhan do tac gia MCPTox cham tren phan hoi model ho da chay; KHONG phai so do ASR do do an tu chay."
(OUT/"inventory.json").write_text(json.dumps(inv, indent=2, ensure_ascii=False))
with open(OUT/"payload_index.csv","w",encoding="utf-8") as f:
    f.write("id,server_name,tool_name,paradigm,security_risk,tool_content_len\n")
    for r in recs: f.write(f'{r["id"]},{r["server_name"]},{r["tool_name"]},{r["paradigm"]},{r["security risk"]},{len(r["tool_content"])}\n')
print(json.dumps(inv, indent=1, ensure_ascii=False))
