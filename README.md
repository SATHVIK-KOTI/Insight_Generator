# 🤖 INSIGHT GENERATOR

> **Real-time market-insight assistant powered by local Llama 3 + FastAPI backend.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Build Status](https://github.com/SATHVIK-KOTI/Insight_Generator/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/SATHVIK-KOTI/Insight_Generator/actions)

![UI Screenshot](docs/ui_screenshot.png)

---

## ✨ Features

| What | Why it matters |
|------|----------------|
| **Sub-2 s CPU replies** | GGUF-quantised Llama 3 via **Ollama** |
| **Market-aware prompts** | Live web search + local LLM |
| **Two modes** | `Market Insight` (concise) / `Content Ideas` (bullets) |
| **Glassmorphic React UI** | Dark-mode SPA in `/frontend` |
| **Offline-capable** | Works air-gapped after first search |

---

## 🗂️ Repo layout

```

Insight\_Generator/
├── main.py
├── llm\_handler.py
├── web\_search.py
├── requirements.txt
├── models/               # GGUF weights
├── docs/
│   ├── embedded\_AI\_project.pdf
│   └── ui\_screenshot.png
└── …

````

---

## 🚀 Quick start

```bash
git clone https://github.com/SATHVIK-KOTI/Insight_Generator.git
cd Insight_Generator

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

ollama run llama3                 # download weights
uvicorn main:app --reload         # run API
````

Visit **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** for Swagger.
To launch the React UI:

```bash
cd frontend && npm i && npm start
```

---

## ⚙️ Configuration

Copy `.env.example` ➜ `.env` and edit:

```env
LLAMA_MODEL_PATH=/abs/path/llama3.gguf
SERPAPI_KEY=your_key
TEMPERATURE=0.7
MAX_TOKENS=1024
```

---

## 🛠️ Scripts

| Command            | Purpose        |
| ------------------ | -------------- |
| `python -m pytest` | (coming soon)  |
| `black .`          | code formatter |
| `ruff check .`     | linter         |

---

## 🏗️ Roadmap

* [ ] Websocket streaming
* [ ] Dockerfile (backend + frontend)
* [ ] Benchmark suite
* [ ] Optional OpenAI fallback

---

## 👥 Contributors

| Name     | GitHub                                                     |
| -------- | ---------------------------------------------------------- |
| Lokesh   | [@SRILOKESHREDDY-ai](https://github.com/SRILOKESHREDDY-ai) |
| Prashant | [@Prasanth217](https://github.com/Prasanth217)             |

---

## 📜 License

MIT – see `LICENSE`.

---

## 🙏 Acknowledgements

Ollama • Llama 3 • FastAPI

Enjoy building with **Insight Generator**! 🎉

