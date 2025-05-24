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

Insight_Generator/
├── main.py # FastAPI entry-point
├── llm_handler.py # prompt templates + Llama 3 inference
├── web_search.py # SerpAPI / DuckDuckGo wrapper
├── requirements.txt
├── models/ # GGUF weights (Git LFS or ignored)
├── docs/
│ ├── embedded_AI_project.pdf
│ └── ui_screenshot.png
└── …

yaml
Copy code

---

## 🚀 Quick start

### 1 · Clone & set up Python env

```bash
git clone https://github.com/SATHVIK-KOTI/Insight_Generator.git
cd Insight_Generator

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
2 · Pull Llama 3 weights via Ollama
bash
Copy code
# Smallest 8-bit quantised 8-B model (~4 GB)
ollama run llama3
Ollama stores weights under ~/.ollama/models/.
Override with LLAMA_MODEL_PATH in your .env if you keep them elsewhere.

3 · Run the API
bash
Copy code
uvicorn main:app --reload
Open http://127.0.0.1:8000/docs to explore the Swagger UI.

4 · (Optional) launch the React UI
bash
Copy code
cd frontend
npm i
npm start
⚙️ Configuration
Copy the provided template:

bash
Copy code
cp .env.example .env
Edit any values:

env
Copy code
LLAMA_MODEL_PATH=/absolute/path/to/llama3.gguf
SERPAPI_KEY=your_key_here        # if you opted for SerpAPI
TEMPERATURE=0.7
MAX_TOKENS=1024
Everything is auto-loaded by python-dotenv in main.py.

🛠️ Available scripts
Command	Description
python -m pytest	Run unit tests (coming soon)
black .	Format code
ruff check .	Lint code

🏗️ Roadmap / TODO
 Websocket streaming for token-by-token UI updates

 Dockerfile (multi-stage: backend + frontend)

 Automated benchmark suite (latency vs model size)

 Optional OpenAI fallback when local model confidence < 0.5

Track progress on the Projects tab.

🤝 Contributing
Fork the repo & create a branch: git checkout -b feature/my-feature

Commit your changes: git commit -m "feat: add my feature"

Push to your fork: git push origin feature/my-feature

Open a pull request and fill in the template.

Please run lint + tests before submitting.

👥 Contributors
Name	GitHub
Lokesh	@SRILOKESHREDDY-ai
Prashant	@Prasanth217

📜 License
Distributed under the MIT License.
See the LICENSE file for details.

🙏 Acknowledgements
Ollama – friction-less local LLM orchestration

Llama 3 weights by Meta AI

FastAPI – a gorgeous developer DX

Enjoy building with INSIGHT GENERATOR! 🎉
