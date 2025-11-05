# LBPO‑Studio (Layer‑Based Prompt Optimizer)

**Outcome‑First Prompt Engineering — Spec → Tests → Score → Argmax**  
KPI Cards · Version Evolution (ΔAccuracy) · Multi‑chart Dashboard · i18n‑ready UI · One‑click Export

---

## What is LBPO‑Studio?
LBPO‑Studio is an outcome‑first, layer‑based prompt optimizer. You define the **task specification** and **test cases**; the system then **searches**, **tests**, and **optimizes** prompts so the model steadily approaches the **ideal output you define**. It replaces “prompting by vibe” with evidence‑backed iteration.

### Why it matters
- **Evidence over intuition** — Quality is measured with tests and KPIs, not gut feel.  
- **Outcome‑first** — Aligns generation with your target result and acceptance criteria.  
- **Reusable pipeline** — Templated Specs, Tests, KPIs, and Version Evolution logs.

---

## Core Features
- **Prompt Enhancer** — Structures intent, injects CoT when the task requires reasoning, supports parameterized placeholders.
- **Validator & Metrics** — Accuracy, F1, Pass Rate, Token Cost, and Progress; extensible scoring.
- **Version Evolution** — Records each change and its **ΔAccuracy** contribution.
- **Visualization‑First Dashboard** — Line/Bar/Pie/Gauge charts with consistent legends and units.
- **One‑click Export** — Share results as Markdown, PDF, or PPTX with evidence and notes.
- **i18n‑ready UI** — Language switching architecture; prioritize effective languages first.

---

## Architecture
```
UI (Vercel)  →  API (Render)  →  Evaluator  →  Metrics Store  →  KPI Dashboard
       ↑              ↓                ↓               ↑
   Prompt Enhancer → Candidate Generation → Scoring → Version Evolution
```

- **Enhancer** converts user intent into structured prompts and can auto‑enable CoT for reasoning tasks.  
- **Evaluator** runs test cases and emits scores (Accuracy, F1, etc.).  
- **Dashboard** displays KPI cards, charts, and the version evolution timeline.

---

## Project Structure
```
LBPO-Studio/
├─ frontend/        # React/Vite (or similar) UI
├─ backend/         # Node/Express (or similar) API & evaluator
└─ others/          # Docs, diagrams, samples, scripts
```
**Demo mode**: static UI preview (`index.html` can be opened directly).  
**Cloud mode**: split frontend/backed; deploy frontend on Vercel and backend on Render.

---

## Quickstart

### A) Demo (Static UI)
1. Download the demo package and open `index.html` in your browser.  
2. Load the sample **Spec** and **Tests** to preview the workflow.  
3. KPI cards and charts render placeholders until linked to backend data.

### B) Cloud (Vercel + Render)

**Backend**
```bash
cd backend
cp .env.example .env
# Add your keys: OPENAI_API_KEY (and optionally ANTHROPIC_API_KEY, GEMINI_API_KEY)
# If using a database: DATABASE_URL
npm install
npm run dev   # or: npm run start
```

**Frontend**
```bash
cd frontend
npm install
npm run dev   # set BACKEND_BASE_URL in your .env (e.g., http://localhost:10000)
```

**Deploy**
- **Vercel (Frontend)**: import repo → set `VITE_API_BASE` → deploy.  
- **Render (Backend)**: add environment variables → rely on platform `$PORT` → deploy.

---

## Environment Variables
```
# Common
NODE_ENV=production
PORT=           # use the platform-injected PORT on Render

# Providers (pick what you use)
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GEMINI_API_KEY=...

# Optional
DATABASE_URL=...
JWT_SECRET=...
METRICS_WRITE_KEY=...
VITE_API_BASE=https://your-backend.onrender.com
```

---

## Usage Flow
1. **Define Spec** — Goal, constraints, quality bar, and tolerances.  
2. **Write Tests** — A compact but representative set with gold answers.  
3. **Run Optimize** — LBPO‑Studio explores prompts/parameters and scores them automatically.  
4. **Review Evidence** — Inspect KPI cards, trend charts, and the ΔAccuracy evolution timeline.  
5. **Export & Share** — Package the winning prompt and evidence as Markdown/PDF/PPTX.

---

## KPIs
- Accuracy · F1 · Pass Rate · Token Cost · Progress%  
- Optional: A/B comparisons and cost‑quality trade‑off plots.

---

## Roadmap
- **v0.4** — Visualization dashboard, Version Evolution, i18n (effective languages first).  
- **v0.5** — Data binding and one‑click exports (MD/PDF/PPTX).  
- **v0.6** — A/B testing, team collaboration, and audit trails.

---

## Contributing
Issues and PRs are welcome. Please include a minimal repro and screenshots/screencasts.


## 🪪 License
© 2025 Tiger — Released under the MIT License.  
Attribution is appreciated but not required.  
This project embodies an open-source spirit — designed to inspire and evolve through collective creativity.  

## Acknowledgments
Lucide icons · Inter font · Vercel · Render. Thanks to early users and reviewers!
