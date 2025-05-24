# 🤖 INSIGHT GENERATOR

> _Lightning-fast market-insight assistant that runs **locally** on Llama 3, fetches live information when needed, and serves everything through a tidy FastAPI + React stack._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Build Status](https://github.com/SATHVIK-KOTI/Insight_Generator/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/SATHVIK-KOTI/Insight_Generator/actions)
[![Open Issues](https://img.shields.io/github/issues/SATHVIK-KOTI/Insight_Generator)](https://github.com/SATHVIK-KOTI/Insight_Generator/issues)

---

## 📖 Introduction
Insight Generator is a **local-first market-insight assistant**.  
It pairs a quantised Llama 3 model (running on your laptop via Ollama) with a FastAPI backend and a sleek React UI.  
The goal: deliver sub-2-second, privacy-friendly answers that blend fresh web data with powerful language-model reasoning.

---

## 🌟 1 · Why this project exists

Content creators, marketers, and researchers often need **fresh insights** (“What’s trending in AI hiring right now?”) and **ready-to-post ideas** (tweets, LinkedIn hooks, blog titles).  
Cloud LLMs are powerful but:

* ✖️ **Bandwidth & privacy** – shipping your data to the cloud is slow and sometimes forbidden.  
* ✖️ **Cost** – tokens add up.  
* ✖️ **Latency** – 4-10 s round-trip pauses creativity.

**Insight Generator** solves that by:

1. Running a _quantised_ Llama 3 model **inside your laptop** (thanks Ollama).  
2. Triggering a quick web search only when the prompt demands new facts.  
3. Returning two flavours of output: **Market Insight** (TL;DR paragraph) and **Content Ideas** (bullet list).  

The result is sub-2 s answers on a modern CPU, with zero data leaving your machine after the first search.

---

## 🏗️ 2 · High-level architecture

```

┌──────────────┐      HTTP      ┌─────────────┐
│ React UI     │◀──────────────▶│ FastAPI app │
│ (frontend/)  │                │  (main.py)  │
└──────────────┘                └────┬────────┘
│
▼
┌───────────────────────┐
│ Llama-3-8B-GGUF model │ ← Ollama runtime
└───────────────────────┘
▲
│
┌─────────────────┐
│ Web-search shim │ ← DuckDuckGo / SerpAPI
└─────────────────┘

```

---

## 🗂️ 3 · Repository layout

```

Insight\_Generator/
├── main.py               # FastAPI entry-point
├── llm\_handler.py        # prompt templates + Llama call
├── web\_search.py         # search wrapper
├── prompts.py            # centralised prompt strings
├── requirements.txt
├── .env.example
├── models/               # GGUF weights (Git LFS-tracked or ignored)
├── frontend/             # React SPA (Vite + Tailwind)
└── tests/
└── test\_llm\_handler.py

````

---

## 🚀 4 · Quick start (5 min)

```bash
# 0. prerequisites: git, Python 3.10+, Node 18+, Ollama
git clone https://github.com/SATHVIK-KOTI/Insight_Generator.git
cd Insight_Generator

python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Download a local Llama 3 model (~4 GB 8-bit)
ollama run llama3

# copy and edit env
cp .env.example .env
# → adjust LLAMA_MODEL_PATH if you stored weights elsewhere

# backend
uvicorn main:app --reload
# open http://127.0.0.1:8000/docs for Swagger

# (optional) frontend
cd frontend && npm i && npm run dev
````

---

## ⚙️ 5 · Configuration keys (`.env`)

| Key                | Default                       | Purpose                                               |
| ------------------ | ----------------------------- | ----------------------------------------------------- |
| `LLAMA_MODEL_PATH` | \~/.ollama/models/llama3.gguf | Path to GGUF file                                     |
| `SERPAPI_KEY`      | *empty*                       | If set, web\_search uses SerpAPI; else DuckDuckGo API |
| `TEMPERATURE`      | `0.7`                         | LLM creativity                                        |
| `MAX_TOKENS`       | `1024`                        | Output length cap                                     |

---

## 🔧 6 · Common dev tasks

| Task                    | Command              |
| ----------------------- | -------------------- |
| Format code             | `black .`            |
| Lint                    | `ruff check .`       |
| Run tests               | `pytest`             |
| Pre-commit hook install | `pre-commit install` |

---

## 📈 7 · Benchmarks (M1 Max 14-core CPU)

| Model      | Precision        | Prompt-to-answer latency | RAM used |
| ---------- | ---------------- | ------------------------ | -------- |
| Llama 3 8B | 8-bit (Q8\_0)    | **1.9 s**                | 9.4 GB   |
| Llama 3 8B | 4-bit (Q4\_K\_M) | 1.6 s                    | 5.2 GB   |

> *Measured with **`uvicorn --workers 1`** and avg. of 10 “What’s a rising topic in edge AI?” queries.*

---

## 🗺️ 8 · Roadmap

* [ ] Websocket streaming (token-by-token)
* [ ] Docker Compose (backend + frontend)
* [ ] Automatic latency benchmarks CI job
* [ ] Optional OpenAI fallback if `confidence < 0.5`
* [ ] Plug-in system for extra data sources (RSS, Twitter, SEC filings)

Track items in [https://github.com/SATHVIK-KOTI/Insight\_Generator/projects](https://github.com/SATHVIK-KOTI/Insight_Generator/projects).

---

## 🤝 9 · Contributing

1. **Fork** → `git checkout -b feature/my-change`
2. Make changes; run `black . && ruff check . && pytest`
3. **Commit** conventional style: `feat:`, `fix:`, `docs:` …
4. **Push** & open a **PR** – fill out the template.
5. One approval + green CI = merge.

Respect the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 👥 10 · Core contributors

| Name                 | GitHub                                                     |
| -------------------- | ---------------------------------------------------------- |
| Lokesh               | [@SRILOKESHREDDY-ai](https://github.com/SRILOKESHREDDY-ai) |
| Prashant             | [@Prasanth217](https://github.com/Prasanth217)             |
| Sathvik (maintainer) | [@SATHVIK-KOTI](https://github.com/SATHVIK-KOTI)           |

---

## ❓ 11 · FAQ & Troubleshooting

<details>
<summary>“`ModuleNotFoundError: llama_cpp`”</summary>

You skipped `pip install -r requirements.txt` **or** the install failed to compile
`llama-cpp-python`. On Linux, make sure you have a C++ compiler (`build-essential`).

</details>

<details>
<summary>“Badge shows ‘no status’”</summary>

GitHub only generates a status badge after you add a workflow file.<br>
Copy `ci.yml.sample` to `.github/workflows/ci.yml` or use your own.

</details>

<details>
<summary>Can I load a 13B model?</summary>

Yes – adjust `ollama run llama3:13b` and bump `LLAMA_MODEL_PATH`.
Expect \~18 GB RAM and \~3-4 s latency on high-end CPUs.

</details>

---

## 📜 12 · License

This project is released under the **MIT License** – see [`LICENSE`](LICENSE).

---

## 🙏 13 · Acknowledgements

* **Meta AI** for releasing Llama 3 weights
* **Ollama** for one-command local LLM serving
* **FastAPI** for a silky dev experience
* Everyone who opens issues or PRs – ✨ thank you!

> *Made with ❤️ and caffeine by the Insight Generator team. Reach us at `<sathvikk35@gmail.com>` if you build something cool on top!*

