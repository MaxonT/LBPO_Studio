# LBPO‑Studio v0.4 (Cloud)

**EN** · Visualization‑first Prompt Optimizer (v0.4).  
This cloud package contains:
- `backend/` (Node/Express) — `/api/optimize` returns simulated growth data.
- `frontend/` (static HTML) — fetches backend and renders charts (line/bar/percentage).
- `others/` — docs & env examples.

## Quick Start (Render + Vercel)
1) Deploy **backend/** to Render (Node). Use default `PORT`.  
   - Health: `GET /health`  
   - API: `POST /api/optimize` → `{ acc,f1,pass,cost,labels,series,barsL,barsV,best,versions,progress }`
2) Host **frontend/** on Vercel as a static site.  
   - Open `index.html`, set “Backend URL” to your Render domain.

## API (POST /api/optimize)
```json
{ "task": "string", "examples": "string" }
```
**Response**  
```json
{ "acc": 91, "f1": 90, "pass": 88, "cost": 79,
  "labels": ["v1","v2","v3","v4","v5"],
  "series": [64,71,79,85,91],
  "barsL": ["Explicit output schema","Few-shot from examples","Short CoT reasoning","Negative constraints","Self-check verifier"],
  "barsV": [4.5,6.8,3.2,2.1,4.7],
  "best": "string",
  "versions": "v1 · ...\nv2 · ...",
  "progress": 82
}
```

---

**中文** · 可视化优先的提示词优化器（v0.4）。  
本 Cloud 包含：
- `backend/`（Node/Express）—— `/api/optimize` 返回可视化所需数据；
- `frontend/`（静态站点）—— 连接后端并绘制折线/柱状/百分比图；
- `others/`—— 文档与环境示例。

## 快速部署（Render + Vercel）
1）将 **backend/** 部署到 Render（Node）。保留默认 `PORT`。  
   - 健康检查：`GET /health`  
   - 接口：`POST /api/optimize`
2）将 **frontend/** 部署到 Vercel（静态）。  
   - 打开页面，在 “Backend URL” 中填入 Render 域名。

## 环境变量
- `PORT`（可选；Render 会注入）
