"""AutoDojo — chạy offline: kiểm kê các file injections.json đã tối ưu mà tác giả phát hành
(suite × model đích × phòng thủ), đếm biến thể payload, thống kê nhãn under-specification
của user task. KHÔNG gọi LLM. Soạn với hỗ trợ AI (Claude)."""
import json, sys, csv, collections, datetime
from pathlib import Path
R = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
rows = []
for f in sorted((R/"variants").rglob("injections.json")):
    d = json.load(open(f)); parts = f.relative_to(R/"variants").parts  # suite/vendor/model/defense/injections.json
    n_pay = n_vec = 0; lens = []
    for it, vecs in d.get("injection_tasks", {}).items():
        for vec, rec in vecs.items():
            n_vec += 1; vs = rec.get("variants", []); n_pay += len(vs); lens += [len(v) for v in vs]
    rows.append({"suite": d.get("suite"), "target": "/".join(parts[1:3]), "defense": d.get("defense"),
                 "optimizer_model": d.get("model"), "method": d.get("method"), "iterations": d.get("iterations"),
                 "n_injection_tasks": len(d.get("injection_tasks", {})), "n_task_vector_pairs": n_vec,
                 "n_payload_variants": n_pay, "mean_len_chars": round(sum(lens)/len(lens), 1) if lens else 0,
                 "seed_styles": "|".join(d.get("seed_styles", [])), "path": str(f.relative_to(R))})
b = json.load(open(R/"user_task_buckets.json"))
bucket_counts = {s: {k: len(v) for k, v in bk.items()} for s, bk in b["buckets"].items()}
C = collections.Counter
summary = {"run_at_utc": datetime.datetime.utcnow().isoformat()+"Z", "n_injection_files": len(rows),
           "suites": C(r["suite"] for r in rows), "targets": C(r["target"] for r in rows),
           "defenses": C(r["defense"] for r in rows), "optimizer_models": C(r["optimizer_model"] for r in rows),
           "total_payload_variants": sum(r["n_payload_variants"] for r in rows),
           "user_task_buckets": bucket_counts, "bucket_definitions": b["bucket_definitions"],
           "NOTE": "Payload do tac gia AutoDojo toi uu va phat hanh; do an CHUA tu chay vong toi uu (can LLM)."}
(OUT/"inventory.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
with open(OUT/"injection_files.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(json.dumps(summary, indent=1, ensure_ascii=False))
