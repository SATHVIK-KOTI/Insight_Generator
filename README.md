# 🤖 INSIGHT GENERATOR

> _Lightning-fast market-insight assistant that runs **locally** on Llama 3, fetches live information when needed, and serves everything through a tidy FastAPI + React stack._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Build Status](https://github.com/SATHVIK-KOTI/Insight_Generator/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/SATHVIK-KOTI/Insight_Generator/actions)
[![Open Issues](https://img.shields.io/github/issues/SATHVIK-KOTI/Insight_Generator)](https://github.com/SATHVIK-KOTI/Insight_Generator/issues)

---

# 🤖 INSIGHT GENERATOR

_A lightweight, local-first assistant that converts natural-language prompts into **Market Insights** and **Content Ideas** in under three seconds._

---

## 📖 Introduction

Most cloud LLM tools are costly, generic and raise privacy concerns. INSIGHT GENERATOR combines:  
- a **React + Bootstrap 5** frontend  
- a **FastAPI** backend  
- a **local LLaMA 3** model served by **Ollama**  

to produce structured results on a standard Windows 11 laptop (Intel i5, 8 GB RAM) in under three seconds, with zero data leaving your machine.

---

## 🏗️ System Architecture

**Three-layer design** (Fig. 1 in the paper):

1. **Frontend**  
   - React UI with dark mode, glassmorphic layout, chat history & copy-to-clipboard  
2. **Backend**  
   - FastAPI endpoint `/generate_insights` that forwards prompts via Ollama to LLaMA 3  
3. **Refinement**  
   - Manual hand-off of JSON output (“Insights” + “Content Ideas”) into Jasper AI for polishing  

### Execution Flow

1. User enters a topic (e.g., “AI in Retail”).  
2. Frontend sends a POST request to the backend.  
3. Backend calls the LLM through Ollama.  
4. LLM returns **Insights** (trends) and **Content Ideas** (blog titles, tweets).  
5. User pastes the output into Jasper AI for refinement.

---

## 🚀 Quickstart & Commands

```bash
# 1. Clone the repo
git clone https://github.com/SATHVIK-KOTI/Insight_Generator.git
cd Insight_Generator

# 2. Create and activate a Python virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Pull a local LLaMA 3 model via Ollama (~4 GB)
ollama run llama3

# 5. Copy and edit environment variables
copy .env.example .env         # Windows PowerShell
cp .env.example .env           # macOS/Linux
# Then open .env and set:
#   LLAMA_MODEL_PATH=/absolute/path/to/llama3.gguf
#   SERPAPI_KEY=your_serpapi_key  (optional)
#   TEMPERATURE=0.7
#   MAX_TOKENS=1024

# 6. Start the backend
uvicorn main:app --reload
# Browse: http://127.0.0.1:8000/docs

# 7. (Optional) Launch the frontend
cd frontend
npm install
npm start
# Browse: http://localhost:3000
````

---

## 🗂️ Repository Layout

```
Insight_Generator/
├── main.py               # FastAPI entry-point
├── llm_handler.py        # prompt templates + LLaMA call
├── web_search.py         # search wrapper
├── prompts.py            # centralised prompt strings
├── requirements.txt
├── .env.example
├── models/               # GGUF weights (Git LFS-tracked or ignored)
├── frontend/             # React SPA (Bootstrap 5)
├── docs/
│   ├── embedded_AI_project.pdf
│   └── ui_overview.png
└── tests/
    └── test_llm_handler.py
```

---

## ⚙️ Configuration (`.env`)

| Key                | Default                        | Purpose                                          |
| ------------------ | ------------------------------ | ------------------------------------------------ |
| `LLAMA_MODEL_PATH` | `~/.ollama/models/llama3.gguf` | Path to the GGUF weights                         |
| `SERPAPI_KEY`      | *(empty)*                      | Use SerpAPI instead of DuckDuckGo for web search |
| `TEMPERATURE`      | `0.7`                          | Controls LLM creativity                          |
| `MAX_TOKENS`       | `1024`                         | Maximum tokens in output                         |

---

## 🔧 Development Commands

| Task              | Command                    |
| ----------------- | -------------------------- |
| Format code       | `black .`                  |
| Lint code         | `ruff check .`             |
| Run unit tests    | `pytest`                   |
| Install Git hooks | `pre-commit install`       |
| Track large files | `git lfs track "models/*"` |

---

## ✨ Key Features

| Feature                                                    | PDF Section        |
| ---------------------------------------------------------- | ------------------ |
| Dark-mode glassmorphic UI                                  | Sec. V-A, V-D      |
| Chat history via `localStorage`                            | Sec. V-B           |
| Copy-to-clipboard for Jasper AI workflow                   | Sec. IV-F, V-C     |
| Offline-capable on CPU                                     | Sec. IV-A          |
| Average latency < 3 s (2.8 s measured)                     | Table II, VI-A     |
| Structured output: **Market Insights** + **Content Ideas** | Sec. III-C, Fig. 3 |

---

## 📊 Model Comparison (Table I)

| Model             | Size  | Avg. Latency | Local-ready | Quality  |
| ----------------- | ----- | ------------ | ----------- | -------- |
| **LLaMA 3 (8 B)** | 13 GB | **1.5 s**    | ✔︎          | High     |
| Mistral (7 B)     | 12 GB | 1.6 s        | ✔︎          | High     |
| GPT-J (6 B)       | 11 GB | 2.3 s        | ✔︎          | Moderate |
| Falcon (7 B)      | 13 GB | 2.0 s        | ✔︎          | Moderate |
| GPT-3.5 API       | Cloud | 0.5 s        | ✖︎          | High     |

*LLaMA 3 was chosen for its balance between speed, quality and CPU-only execution.*

---

## 🔮 Future Work

* GPU or deeper quantisation to support larger models (e.g., LLaMA 3-70 B)
* Automated Jasper AI API integration to remove manual copy-paste
* Multi-user profiles & custom prompt templates
* Analytics dashboard & Electron/mobile build

---

## 👥 Contributors

| Name                            | Programme                  | Email                                                                         |
| ------------------------------- | -------------------------- | ----------------------------------------------------------------------------- |
| Sri Lokesh Reddy Ankireddypalli | MSc Robotics & Embedded AI | [sri.ankireddypalli.2025@mumail.ie](mailto:sri.ankireddypalli.2025@mumail.ie) |
| Prashanth Gujjula               | MSc Robotics & Embedded AI | [prasanth.gujjula.2025@mumail.ie](mailto:prasanth.gujjula.2025@mumail.ie)     |
| Sathvik Koti                    | MSc Robotics & Embedded AI | [sathvik.koti.2025@mumail.ie](mailto:sathvik.koti.2025@mumail.ie)             |

---

## 📄 References

See the PDF’s reference list for sources on ChatGPT, Jasper AI, FastAPI, Ollama, LLaMA 3 and Bootstrap 5.

```
```
