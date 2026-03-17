# 💼 Enterprise RAG Knowledge Assistant

### *Agentic AI System for Financial Document Intelligence*

---

## 🚀 Overview

This project is a **production-grade Retrieval-Augmented Generation (RAG) system** designed to enable intelligent querying over enterprise financial documents such as invoices and reports.

It combines **LLMs, vector search, reranking, and agent-based decision-making** to deliver accurate, context-aware answers from unstructured data.

> ⚡ Built as a real-world simulation of enterprise AI systems used in analytics, finance, and business intelligence platforms.

---

## 🧠 Key Highlights

* 🧩 **Agentic RAG Architecture** (LLM-based query planning)
* 🔍 **Multi-query retrieval** for better recall
* 🎯 **CrossEncoder reranking** for high precision answers
* ⚡ **Redis caching** for performance optimization
* 📄 **Real-time document ingestion** via UI
* 🌐 **Dual interface**: Streamlit UI + FastAPI backend
* 📊 **Evaluation-ready** with RAGAS metrics

---

## 🏗️ System Architecture

```
User Query
   ↓
Query Planner (LLM Decision Engine)
   ↓
Retriever (Multi-Query + Metadata Filter)
   ↓
FAISS Vector Database
   ↓
CrossEncoder Reranker
   ↓
Top-K Context
   ↓
LLM (LLaMA3 via Ollama)
   ↓
Answer Generator
   ↓
Redis Cache
   ↓
Response (UI / API)
```

---

## 🔍 Core Components

### 1. Query Planner (Agentic Layer)

* Uses LLM to decide:

  * Retrieval required (RAG)
  * Direct response
* Mimics **tool-use decision systems**

---

### 2. Retrieval Layer

* FAISS-based vector search
* Multi-query expansion (LangChain)
* Metadata filtering (year, month)

---

### 3. Reranking Layer

* CrossEncoder (`ms-marco-MiniLM`)
* Improves semantic relevance
* Filters top-k high-quality documents

---

### 4. Generation Layer

* LLaMA3 (via Ollama)
* Context-grounded answer generation
* Prompt-controlled responses

---

### 5. Performance Layer

* Redis caching
* Avoids redundant LLM calls
* Reduces latency & cost

---

### 6. Ingestion Pipeline

* PDF → Text → Chunking → Embeddings → FAISS
* Supports dynamic document upload

---

## 📁 Project Structure

```
rag-enterprise-knowledge-assistant/
│
├── data/
│   ├── invoices/
│   ├── reports/
│   └── uploads/
│
├── embeddings/
│
├── src/
│   ├── answer_generator.py
│   ├── cache.py
│   ├── chunking.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── llm_inference.py
│   ├── main.py
│   ├── metadata_filter.py
│   ├── query_planner.py
│   ├── rag_pipeline.py
│   ├── reranker.py
│   ├── retriever.py
│   ├── streamlit_app.py
│   └── vector_store.py
│
├── architecture-diagrams/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd rag-enterprise-knowledge-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Setup LLM (Ollama)

```bash
ollama run llama3
ollama pull nomic-embed-text
```

---

## 📥 Data Ingestion

```bash
python src/ingest.py
```

---

## 💻 Run Application

### ▶️ Streamlit UI

```bash
streamlit run src/streamlit_app.py
```

### 🌐 FastAPI Backend

```bash
uvicorn src.main:app --reload
```

---

## 🔌 API Example

```json
POST /ask

{
  "query": "Show revenue trends for 2023"
}
```

---

## 📊 Tech Stack

| Layer      | Technology           |
| ---------- | -------------------- |
| LLM        | Ollama (LLaMA3)      |
| Framework  | LangChain            |
| Vector DB  | FAISS                |
| Reranking  | SentenceTransformers |
| Backend    | FastAPI              |
| Frontend   | Streamlit            |
| Caching    | Redis                |
| Evaluation | RAGAS                |

---

## 📈 Business Impact

* Enables **natural language access to enterprise data**
* Reduces manual analysis effort
* Improves decision-making speed
* Demonstrates real-world **AI assistant architecture**

---

## 🧠 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* LLM orchestration & prompt engineering
* Vector search & semantic retrieval
* Agentic AI systems (query planning)
* Backend API development (FastAPI)
* Performance optimization (Redis caching)
* End-to-end AI system design

---

## 🚀 Future Enhancements

* LangGraph workflow orchestration
* Streaming responses
* Cloud deployment (AWS/GCP)
* Multi-tenant support
* Advanced evaluation dashboards

---

## 👨‍💻 Author

**Manish Rathi**
Data Scientist | Generative AI Engineer
Specializing in LLMs, RAG Systems & AI Agents

---
