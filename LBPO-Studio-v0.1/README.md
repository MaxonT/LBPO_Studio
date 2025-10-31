# LBPO‑Studio (Learning by Prompt Optimization) · Demo v0.1

**中文 / English**

A tiny, production‑lean demo that **turns prompt optimization into an automated ML loop**:
> Spec → Generate candidate prompts → Call model (OpenAI or Mock) → Evaluate on tests → Score → Pick best prompt → Export.

This is a *download‑and‑run* starter you can commercialize as a micro‑SaaS or embed into your product.

---

## ✨ Features
- **Outcome‑First loop**: Optimize prompts against *your* test set and evaluator.
- **Two model backends**: `openai` (GPT‑4o‑mini by default) or `mock` (offline rule‑based model).
- **Two evaluators**: `exact_match` and `keyword_f1` (precision/recall style).
- **Web UI + REST API**: run experiments, see leaderboard, export CSV/JSON.
- **No vendor lock‑in**: simple Python + Flask; deploy anywhere (Render/VM/Docker).

---

## 🚀 Quickstart (Local)

### 0) Requirements
- Python 3.9+
- (Optional) An OpenAI API key in environment variable `OPENAI_API_KEY`

### 1) Create & activate venv
```bash
cd LBPO-Studio
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run the app
```bash
python app.py
```
Then open **http://localhost:5000**.

> If you don't have an API key, select **Backend = mock** in the UI to run fully offline.

---

## 🖥️ Web UI Walkthrough

1. Fill **Task Instruction** (e.g., "Sentiment classification: respond as 'POS' or 'NEG'").  
2. Add **Test Cases** (input + expected).  
3. Choose **Backend** (`openai` or `mock`) and **Evaluator** (`exact_match` or `keyword_f1`).  
4. Click **Run Optimization** → The optimizer generates prompt candidates, runs the loop, and ranks them.  
5. Download results as CSV/JSON; copy the **Best Prompt** for production.

> Tip: Start with `mock` to see the loop work instantly, then switch to `openai` for real quality.

---

## 🔌 REST API (for your own frontend)

### POST `/optimize`
- **Body** (JSON):
```json
{
  "instruction": "Classify sentiment as POS or NEG",
  "backend": "mock",
  "evaluator": "exact_match",
  "iterations": 3,
  "beam_width": 5,
  "testcases": [
    {"input": "I love this", "expected": "POS"},
    {"input": "This is terrible", "expected": "NEG"}
  ]
}
```
- **Response** (JSON): best prompt, leaderboard, run_id, scores.

### GET `/api/runs`
- List previous runs (IDs, timestamps, summary).

### GET `/download/<filename>`
- Download CSV/JSON exported results.

---

## 🧪 Evaluators

- **`exact_match`**: normalize spaces/case, compare to expected string.
- **`keyword_f1`**: provide a comma‑separated string of keywords in the `expected` field, we compute token‑level precision/recall/F1.

You can write your own evaluator in `evaluators.py` to fit your task (e.g., regex scoring, Rouge, BLEU, custom rubric).

---

## 🧱 Architecture

```
/app.py           Flask app + routes
/lbpo.py          Optimizer (generate → evaluate → select → mutate)
/models.py        Model adapters: OpenAI + Mock
/evaluators.py    Scorers: exact_match, keyword_f1
/templates/       Jinja2 HTML templates
/static/          Client JS/CSS
/runs/            Saved artifacts (CSV, JSON)
```

---

## ☁️ One‑Stop Deploy (Render)

1. **Push repo to GitHub** (this folder).
2. On **Render.com → New → Web Service**.
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `python app.py`
5. **Environment**:
   - `PYTHON_VERSION=3.11`
   - `OPENAI_API_KEY=...` *(if using OpenAI)*
6. Click **Deploy** → open the URL.

> The app binds to `0.0.0.0:5000` by default and respects Render's `PORT` env if provided.

---

## 🧭 Commercialization (mini plan)

**竞争优势 / Competitive Advantage**
1. **Outcome‑First**：以可度量的任务测试集为核心，prompt 即参数 → 可持续优化。  
2. **可插拔**：模型、评估器、任务模板可替换，避免被一家厂商锁死。  
3. **从 Demo 到产品**：内置数据导出与 REST API，轻松嵌入现有工作流。

**盈利模式 / Business Model**
- SaaS 订阅（按项目/次/月计费）
- 按调用量计费（带速率限制与配额）
- 企业版：自建部署 + SSO + 自定义评估器

**增长策略 / Growth Strategy**
- DevRel：开源社区版 + 教程内容种草
- 垂直案例：为“客服回复、文案风格、分类器提示词”等做专用模板
- 合作渠道：和标注平台、A/B 实验平台做集成

---

## ⚙️ Config

Environment variables:
- `OPENAI_API_KEY` *(optional)*
- `DEFAULT_MODEL` (default: `gpt-4o-mini`)
- `PORT` (Render/Heroku will inject; local default 5000)

---

## 📄 License

MIT License — see `LICENSE`.

---

Made with ♥ for Tiger — keep building. 加油！
