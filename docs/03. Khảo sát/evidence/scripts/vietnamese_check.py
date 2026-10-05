"""Đếm payload có ký tự ĐẶC THÙ tiếng Việt (ă đ ơ ư và nguyên âm mang dấu thanh không có trong
tiếng Pháp/Tây Ban Nha) trong dữ liệu 5 benchmark. Dùng regex hẹp để tránh đếm nhầm tên riêng
tiếng Pháp (é, à). Soạn với hỗ trợ AI (Claude). Chạy: python3 vietnamese_check.py <benchmarks_dir> <evidence_dir>"""
import re, json, glob, csv, sys, importlib.util
B, E = sys.argv[1], sys.argv[2]
vi = re.compile(r"[ăđơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]", re.I)
def cnt(name, texts):
    t = list(texts); print(f"{name}: tong {len(t)}, co ky tu dac thu tieng Viet {sum(bool(vi.search(x)) for x in t)}")
cnt("AgentDojo payload_samples_all.csv", [r["payload"] for r in csv.DictReader(open(f"{E}/agentdojo/payload_samples_all.csv", encoding="utf-8"))])
cnt("MCPTox pure_tool.json tool_content", [v["tool_content"] for it in json.load(open(f"{B}/MCPTox-Benchmark/pure_tool.json")) for v in it.values()])
cnt("InjecAgent base Attacker Instruction", [x["Attacker Instruction"] for f in glob.glob(f"{B}/InjecAgent/data/test_cases_*_base.json") for x in json.load(open(f))])
ad = []
for f in glob.glob(f"{B}/AutoDojo/agentdojo/variant_generation/variants/**/injections.json", recursive=True):
    for it in json.load(open(f)).get("injection_tasks", {}).values():
        for r in it.values(): ad += r.get("variants", [])
cnt("AutoDojo variants", ad)
sys.path.insert(0, f"{B}/MCP-Poison-Bench"); import fixtures.payloads as P
cnt("MCP-Poison-Bench PAYLOAD_SETS", [str(p) for reg in P.PAYLOAD_SETS.values() for v in reg.values() for p in v])
