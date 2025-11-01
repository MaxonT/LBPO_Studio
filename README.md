---
title: "LBPO-Studio — Outcome-First Prompt Engineering（分层提示优化工作室）"
author: "LBPO-Studio Contributors"
date: "`r format(Sys.Date())`"
output:
  html_document:
    toc: true
    toc_depth: 2
    number_sections: false
    theme: readable
    df_print: paged
---

# 🧠 LBPO-Studio

English | 中文（简体）

---

## 🌟 Overview · 概览

**LBPO-Studio (Layer-Based Prompt Optimizer Studio)**  
is an intelligent system that helps users **define**, **test**, and **optimize** prompts for large language models (LLMs).

The core mechanism is: **you write your own task instructions and test cases**.  
Based on these, the system **searches**, **tests**, and **optimizes** prompts, improving model performance on your cases.

Goal: **let the model automatically approach the “ideal output” you define.**

---

**LBPO-Studio（分层提示优化工作室）**  
用于帮助用户**定义**、**测试**与**优化**大语言模型的提示词（Prompt）。

核心机制：**用户自行编写任务指令与测试用例**。  
系统据此**搜索**、**测试**并**优化**提示词，让模型在你的场景上表现更好。

目标：**让模型自动接近你所定义的「理想输出」**。

---

## ⚙️ Core Mechanism · 核心机制

| Step | Description (English) | 说明（中文） |
|:---:|:---|:---|
| 1️⃣ | **User Input** — Users write task instructions and test cases. | **用户输入**：编写任务指令与测试用例。 |
| 2️⃣ | **Automatic Search** — System explores multiple prompt candidates. | **自动搜索**：系统生成与筛选多种提示词方案。 |
| 3️⃣ | **Evaluation & Testing** — Test each prompt on your cases. | **评估与测试**：在测试用例上逐一评估提示词。 |
| 4️⃣ | **Optimization** — Refine prompts based on test performance. | **优化**：依据测试结果自动迭代优化提示词。 |
| 5️⃣ | **Ideal Output Alignment** — Approach your defined “ideal output.” | **对齐理想输出**：模型逐步接近你的目标答案。 |

---

## 💡 Key Features · 主要特性

- 🧩 **Custom Task & Test Design** — Define your own tasks and metrics.  
  **自定义任务与测试**：可自定任务与评估指标。

- 🔍 **Automated Prompt Search & Evaluation** — Iteratively find better wordings.  
  **自动搜索与评估**：迭代寻找更优提示表达。

- 🧠 **Performance-Driven Optimization** — Score and improve each iteration.  
  **以表现为导向的优化**：以测试结果为依据持续改进。

- 🎯 **Outcome Alignment** — Match your **ideal output**.  
  **结果对齐**：对齐你定义的目标产出。

- 🌐 **Multi-Language Interface** — English / 中文 / Español / Français / 日本語 / 한국어, etc.  
  **多语言界面**：支持多语种切换。

---

## 🚀 Vision · 愿景

LBPO-Studio introduces **Outcome-First Prompt Engineering** —  
replacing intuition-based crafting with a **quantitative loop** among prompts, tests, and model performance.

LBPO-Studio 代表**结果优先的提示工程**：  
以**提示-模型-测试**的**量化闭环**取代拍脑袋式的写法，实现持续优化与自我校准。

---

## 📂 Project Structure · 项目结构
