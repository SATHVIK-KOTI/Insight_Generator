# 🤖 INSIGHT GENERATOR

_A lightweight, local-first assistant that converts natural-language prompts into **market insights** and **content ideas** inside a chat-style interface._

---

## 📖 Introduction  

**Generative AI** is reshaping how marketers, analysts and startups create copy and interpret market data. Most cloud-based tools are costly, generic and raise privacy concerns.  
INSIGHT GENERATOR addresses these gaps with a **React + Bootstrap 5** frontend, a **FastAPI** backend and a **local LLM (LLaMA 3 via Ollama)** that runs entirely on CPU hardware. It produces structured results in **under three seconds** and enables a dual-phase workflow: rapid local ideation followed by polishing in Jasper AI. :contentReference[oaicite:0]{index=0}

---

## 🌐 System architecture  

*Three-layer design* (Fig. 1 in the paper):  

1. **Frontend** – React UI with dark mode, chat history, copy-to-clipboard and a glassmorphic layout.  
2. **Backend** – FastAPI server that forwards prompts to a local LLM and returns **Market Insights** + **Content Ideas**.  
3. **Refinement layer** – manual hand-off of copy-ready text to Jasper AI for tone, SEO and publication. :contentReference[oaicite:1]{index=1}

#### Execution flow  

1. User enters a topic (e.g. “AI in Retail”).  
2. Frontend POSTs the prompt to the backend.  
3. Backend calls Ollama-hosted LLaMA 3 with a templated prompt.  
4. Response is split into _Insights_ and _Content Ideas_.  
5. User optionally pastes the result into Jasper AI for further editing. :contentReference[oaicite:2]{index=2}

---

## ✨ Key features  

| Feature | Paper reference |
|---------|-----------------|
| Dark-mode, glassmorphic UI | Sec. V-A, V-D |
| Chat history stored in `localStorage` | Sec. V-B |
| Copy-to-clipboard buttons for Jasper workflow | Sec. V-C |
| Runs fully **offline** on standard Windows-11 i5/8 GB laptop | Sec. IV-A |
| Average latency **< 3 s** (2.8 s measured) | Table II & Sec. VI-A |
| Structured output: **Market Insights** + **Content Ideas** | Sec. III-C / Fig. 3 |

---

## 🧩 Model selection (Table I)

| Model            | Size | Avg. latency | Local-ready | Output quality |
|------------------|------|--------------|-------------|----------------|
| **LLaMA 3 (8 B)**| 13 GB| **1.5 s**    | ✔︎ | High |
| Mistral (7 B)    | 12 GB| 1.6 s        | ✔︎ | High |
| GPT-J (6 B)      | 11 GB| 2.3 s        | ✔︎ | Moderate |
| Falcon (7 B)     | 13 GB| 2.0 s        | ✔︎ | Moderate |
| GPT-3.5 API      | Cloud| 0.5 s        | ✖︎ | High | :contentReference[oaicite:3]{index=3}

_LLaMA 3 was chosen for its balance of speed, quality and CPU-only execution._ :contentReference[oaicite:4]{index=4}

---

## 💻 Development environment  

* Tested on **Windows 11**, Intel Core i5, **8 GB RAM**, no GPU.  
* Backend: **Python 3.11** + FastAPI.  
* Frontend: **React + Bootstrap 5**. :contentReference[oaicite:5]{index=5}

---

## 🔮 Future work  

* GPU or further quantisation to support larger models (e.g., LLaMA 3-70B).  
* Automate Jasper AI integration through their API.  
* Multi-user profiles, customizable prompt templates, analytics dashboard.  
* Mobile or Electron desktop build. :contentReference[oaicite:6]{index=6}

---

## 👥 Contributors  

| Name | Affiliation | Email |
|------|-------------|-------|
| **Sri Lokesh Reddy Ankireddypalli** | MSc Robotics & Embedded AI, Maynooth Univ. | sri.ankireddypalli.2025@mumail.ie |
| **Prashanth Gujjula** | MSc Robotics & Embedded AI, Maynooth Univ. | prasanth.gujjula.2025@mumail.ie |
| **Sathvik Koti** | MSc Robotics & Embedded AI, Maynooth Univ. | sathvik.koti.2025@mumail.ie | :contentReference[oaicite:7]{index=7}

---

## 📄 References  

See the reference list in the accompanying PDF for all cited works, including OpenAI ChatGPT [1], Jasper AI [2], FastAPI [3], Ollama [4] and LLaMA 3 [5]. :contentReference[oaicite:8]{index=8}
