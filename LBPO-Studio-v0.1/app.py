import os
import json
import csv
import uuid
from datetime import datetime
from flask import Flask, request, render_template, jsonify, send_from_directory
from lbpo import run_optimization
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json(force=True)
    instruction = data.get("instruction", "").strip()
    backend = data.get("backend", "mock")
    evaluator = data.get("evaluator", "exact_match")
    iterations = int(data.get("iterations", 3))
    beam_width = int(data.get("beam_width", 5))
    model_name = data.get("model", os.getenv("DEFAULT_MODEL", "gpt-4o-mini"))
    api_key = data.get("api_key") or os.getenv("OPENAI_API_KEY", None)
    testcases = data.get("testcases", [])

    if not instruction:
        return jsonify({"error": "instruction is required"}), 400
    if not testcases or not isinstance(testcases, list):
        return jsonify({"error": "testcases must be a non-empty list"}), 400

    run_id = datetime.utcnow().strftime("%Y%m%d-%H%M%S-") + str(uuid.uuid4())[:8]
    result = run_optimization(
        instruction=instruction,
        testcases=testcases,
        backend=backend,
        evaluator=evaluator,
        model_name=model_name,
        api_key=api_key,
        iterations=iterations,
        beam_width=beam_width,
    )

    os.makedirs("runs", exist_ok=True)
    json_path = os.path.join("runs", f"{run_id}.json")
    csv_path = os.path.join("runs", f"{run_id}.csv")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "score", "prompt"])
        for i, row in enumerate(result["leaderboard"], 1):
            writer.writerow([i, row["score"], row["prompt"]])

    out = result.copy()
    out["run_id"] = run_id
    out["artifacts"] = {"json": f"/download/{run_id}.json", "csv": f"/download/{run_id}.csv"}
    return jsonify(out)

@app.route("/api/runs", methods=["GET"])
def list_runs():
    items = []
    if not os.path.isdir("runs"):
        return jsonify({"runs": items})
    for name in sorted(os.listdir("runs")):
        if name.endswith(".json"):
            path = os.path.join("runs", name)
            with open(path, "r", encoding="utf-8") as f:
                payload = json.load(f)
            ts = name.replace(".json", "")
            items.append({
                "run_id": ts,
                "best_score": payload.get("best", {}).get("score", None),
                "instruction": (payload.get("instruction") or "")[:120],
                "backend": payload.get("backend"),
                "evaluator": payload.get("evaluator"),
            })
    return jsonify({"runs": items})

@app.route("/download/<path:filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory("runs", filename, as_attachment=True)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
