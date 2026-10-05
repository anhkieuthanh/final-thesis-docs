"""MCPTox — đếm DẠNG TU TỪ của payload theo từng khuôn (Template-1/2/3) bằng regex thô.
Đây là heuristic sơ bộ để thảo luận ánh xạ khuôn → kỹ thuật T1–T5, KHÔNG phải nhãn kỹ thuật
theo cây quyết định của lab (cây đó chưa viết). Soạn với hỗ trợ AI (Claude).
Chạy: python3 mcptox_form_heuristic.py <MCPTox-Benchmark>"""
import json, re, sys, collections
p = [dict(id=k, **v) for it in json.load(open(f"{sys.argv[1]}/pure_tool.json")) for k, v in it.items()]
F = {
    "tien_quyet": r"\b(before|prior to)\b.*\b(must|first|call|use)\b|\bfirst (call|use|run)\b",
    "sua_tham_so": r"\b(change|modify|replace|redirect|overwrite|set|append|add)\b[^.]{0,80}\bto\b",
    "uy_quyen_ghi_de": r"priority is higher|ignore (all|the|previous)|<important>|\bimportant\b|override|\bsystem\b",
    "ly_do_nghiep_vu": r"\b(ensure|security|secure|complian|audit|prevent|verify|validat)",
    "vuot_quyen_user": r"priority is higher than the user|ignore (all|the|previous)|regardless of (the )?user|override",
}
n = collections.Counter(); c = collections.defaultdict(collections.Counter)
for r in p:
    t = r["paradigm"]; s = r["tool_content"]; n[t] += 1
    hit = {k: bool(re.search(rx, s, re.I | re.S)) for k, rx in F.items()}
    for k, v in hit.items(): c[t][k] += v
    c[t]["chi_tien_quyet"] += hit["tien_quyet"] and not hit["sua_tham_so"]
    c[t]["chi_sua_tham_so"] += hit["sua_tham_so"] and not hit["tien_quyet"]
    c[t]["khong_dang_nao"] += not hit["tien_quyet"] and not hit["sua_tham_so"]
for t in sorted(n):
    print(f"{t} n={n[t]}: " + ", ".join(f"{k}={v} ({v/n[t]:.0%})" for k, v in c[t].items()))
tot = sum(c[t]["tien_quyet"] for t in n); print(f"TONG co dang tien_quyet: {tot}/{sum(n.values())}")
