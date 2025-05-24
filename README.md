# 🤖 INSIGHT GENERATOR

> **Real-time market-insight assistant powered by local Llama 3 + lightweight FastAPI backend.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Build](https://img.shields.io/github/actions/workflow/status/your-user/insight-generator/ci.yml?branch=main)](https://github.com/your-user/insight-generator/actions)

---

## ✨ Features

| What | Why it matters |
|------|----------------|
| **Sub-2 s responses on CPU** | Uses Ollama’s GGUF quantised Llama 3 weights. |
| **Market-aware prompts** | Blends live web search with local LLM for up-to-date answers. |
| **Two output modes** | `Market Insight` (concise) and `Content Ideas` (bullet-style). |
| **Glassmorphic React UI** | Smooth dark-mode SPA—ships separately under `/frontend`. |
| **100 % offline-capable** | After the first search, answers can run fully air-gapped. |

---

## 🗂️ Repository layout

```

insight-generator/
├── main.py              # FastAPI entry-point
├── llm\_handler.py       # prompt templates + Llama 3 inference
├── web\_search.py        # SerpAPI / DuckDuckGo wrapper
├── requirements.txt
├── models/              # GGUF weights (Git LFS or ignored)
├── docs/embedded\_AI\_project.pdf
└── ...

````

---

## 🚀 Quick start

### 1 · Clone & set up Python env

```bash
git clone https://github.com/your-user/insight-generator.git
cd insight-generator

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 2 · Pull Llama 3 weights via **Ollama**

```bash
# smallest 8-bit quantised 8 B model ~4 GB
ollama run llama3
```

> Ollama places weights under `~/.ollama/models/`. Adjust `LLAMA_MODEL_PATH`
> in `.env` if you store them elsewhere.

### 3 · Run the API

```bash
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to play with the Swagger UI.

### 4 · (Optionally) launch the React UI

```bash
cd frontend
npm i
npm start
```

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
LLAMA_MODEL_PATH=/absolute/path/to/llama3.gguf
SERPAPI_KEY=your_key_here       # if you opted for SerpAPI
TEMPERATURE=0.7
MAX_TOKENS=1024
```

Anything set here is auto-loaded by **python-dotenv** in `main.py`.

---

## 🛠️ Available scripts

| Command            | Description                   |
| ------------------ | ----------------------------- |
| `python -m pytest` | Run unit tests (coming soon). |
| `black .`          | Format code.                  |
| `ruff check .`     | Lint code.                    |

---

## 🏗️ Roadmap / TODO

* [ ] Add websocket streaming for token-by-token UI updates
* [ ] Dockerfile (separate stages for backend & frontend)
* [ ] Automated benchmark suite (latency vs model size)
* [ ] Optional OpenAI fallback when local model confidence < 0.5

Use [GitHub Projects](../../projects) to track progress.

---

## 🤝 Contributing

1. Fork the repo & create your branch: `git checkout -b feature/foo`.
2. Commit your changes: `git commit -m 'Add some foo'`.
3. Push to the branch: `git push origin feature/foo`.
4. Open a pull request and fill in the template.

Please run *lint + tests* before submitting.

---


## 👥 Contributors

| Name | GitHub |
|------|--------|
| Lokesh | [@SRILOKESHREDDY-ai](https://github.com/SRILOKESHREDDY-ai) |
| Prashant | [@Prasanth217](https://github.com/Prasanth217) |


## 📜 License

Distributed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

* [Ollama](https://github.com/ollama/ollama) for dead-simple local LLM orchestration.
* [Llama 3](https://ai.meta.com/llama/) weights by Meta AI.
* [FastAPI](https://fastapi.tiangolo.com/) for a gorgeous developer DX.

Enjoy building with **INSIGHT GENERATOR**! 🎉

```
```
