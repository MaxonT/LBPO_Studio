---
title: "LBPO‑Studio — The First Prototype of Promptly"
subtitle: "Outcome‑First Prompt Optimization — where everything started"
author: "Tiger Yang"
date: "`r format(Sys.Date())`"
output:
  html_document:
    toc: true
    toc_depth: 2
    number_sections: false
    theme: cosmo
    df_print: paged
  pdf_document:
    toc: true
    number_sections: false
---

> ⚠️ **Project Status · Archived**  
> LBPO‑Studio 是我关于 **Outcome‑First Prompt Engineering（结果导向提示词优化）** 的**第一代原型**。  
> 研发已迁移至 **Promptly** —— 一个更简洁、面向实时优化的新工作区。  
> This repository is preserved for **reference and learning**.

---

# 🌟 Overview · 概览

**LBPO‑Studio (Layer‑Based Prompt Optimizer)** 是一套用于**定义、测试与优化**提示词（Prompts）的实验系统。  
它不追求让模型“更聪明”，而是让提示词**更精准、可度量、与人类目标对齐**。

- It helps you **define** your task spec & golden outputs  
- Automatically **search, evaluate, and refine** prompts  
- Tracks **delta improvements** across iterations

## 🧠 Core Loop · 核心循环
```
Define Spec → Generate Candidates → Evaluate → Optimize → Export
```

## ✨ Core Concepts · 核心理念
- **Outcome‑First Thinking｜结果导向** — 优化你真正想要的输出  
- **Human‑in‑the‑Loop｜人类在环** — 由用户定义金标准输出  
- **Prompt Evolution Tracking｜演化轨迹** — 可视化 Δ Accuracy / F1 / Pass Rate  
- **Layered Architecture｜分层架构** — 将搜索、评测、反馈解耦

---

# 📊 Key Features (v0.5 Final) · 关键特性
- Visualization‑first dashboard（折线/柱状/仪表盘）  
- Five real‑time metrics: **Accuracy / F1 / Pass Rate / Token Cost / Progress %**  
- Multi‑language UI (English / 中文 / more)  
- Prompt version history with **Δ performance**  
- Two modes: **Demo (static‑UI)** & **Cloud (frontend + backend)**

> **Note:** This is the **final archived state** of LBPO‑Studio. Future work happens in **Promptly**.

---

# 🗂 Project Structure · 项目结构
```
LBPO_Studio/
├─ LBPO-Studio-v0.5-Demo/       # Static UI preview (index.html)
├─ LBPO-Studio-v0.5-Cloud/      # Backend + frontend version
├─ docs/                        # Product overview & notes
├─ README.md
├─ LICENSE (MIT)
└─ CHANGELOG.md
```

---

# 🚀 Legacy Impact · 传承与影响

LBPO‑Studio 为 **Promptly** 奠定了概念与工程基础，  
其中「Outcome‑First Real‑Time Alignment」观念在新项目中得到充分发展：

> “Don’t make the model smarter.  
> Make the **outcome** closer.”

通过分层评测与可视化分析，LBPO‑Studio 将提示词优化从“灵感游戏”推进为一种**可工程化的流程**。

---

# 🧭 Successor Project · 后继项目

**Promptly** — A cleaner, evolving workspace for **real‑time prompt testing, scoring, and refinement**.  
All future development continues there.

- Repo: *(to be added by you)*  
- Live Demo: *(to be added by you)*

---

# 🖼 Screenshots · 截图（可选）

> 将图片放在 `screenshots/` 目录，然后在此引用：

- `screenshots/dashboard.png`  
- `screenshots/evolution.gif`  

```{r, echo=FALSE, out.width='80%', fig.align='center'}
# placeholder example (no image embedded in this template)
```

---

# 🗒 Changelog · 里程碑摘录
- **v0.5** — Visualization dashboard, prompt evolution, bilingual UI, demo & cloud modes  
- **v0.4** — Outcome‑metrics baseline, initial cloud wiring  
- **v0.2** — First complete loop (spec → evaluate → optimize)

> Full details are available in Releases (if published).

---

# 🪶 Author

**Tiger Yang** · Vanderbilt University  
Exploring **AI × Human Cognition × Product Design**

> “Every prototype is a footprint of thought — not perfection, but evolution.”

---

# 📝 License

MIT © LBPO‑Studio Contributors  
This project is archived and preserved for reference.
