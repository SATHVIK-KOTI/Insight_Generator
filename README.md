# 🤖 INSIGHT GENERATOR

> **Real-time market-insight assistant powered by local Llama 3 + lightweight FastAPI backend.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Build Status](https://github.com/SATHVIK-KOTI/Insight_Generator/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/SATHVIK-KOTI/Insight_Generator/actions)

> ![UI Screenshot](docs/ui_screenshot.png)
>
> *Figure 1 – glassmorphic React frontend (dark-mode).*

---

## ✨ Features

| What | Why it matters |
|------|----------------|
| **Sub-2 s responses on CPU** | GGUF-quantised Llama 3 weights via **Ollama**. |
| **Market-aware prompts** | Blends live web search with local LLM for up-to-date answers. |
| **Two output modes** | `Market Insight` (concise) and `Content Ideas` (bullet-style). |
| **Glassmorphic React UI** | Smooth dark-mode SPA (lives in `/frontend`). |
| **100 % offline-capable** | After the first search, answers can run fully air-gapped. |

---

## 🗂️ Repository layout

