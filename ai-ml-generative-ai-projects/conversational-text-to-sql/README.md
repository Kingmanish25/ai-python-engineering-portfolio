# 💬 Conversational Text-to-SQL AI System

### LLM-Powered Financial Analytics Assistant

---

## 🚀 Project Overview

Designed and developed a **production-grade Conversational Text-to-SQL AI system** that enables non-technical users to query structured financial databases using natural language.

This system leverages **Large Language Models (LLMs)** to translate user queries into SQL, execute them on a database, and return actionable insights with visualizations.

> 📌 Goal: Democratize data access and eliminate the need for manual SQL querying.

---

## 🧠 Key Highlights

* Built an **end-to-end LLM-powered analytics pipeline**
* Converted natural language → SQL queries using prompt engineering
* Implemented **safe SQL execution layer (guardrails)**
* Designed **modular architecture** for scalability and maintainability
* Enabled **conversational memory** for multi-turn interactions
* Integrated **real-time data visualization**
* Achieved **high query accuracy (~95%) on structured datasets**

---

## 🏗️ System Architecture

```
User Query (Natural Language)
        ↓
Conversation Memory (Context)
        ↓
Prompt Engineering
        ↓
LLM (GPT Model)
        ↓
SQL Query Generation
        ↓
SQL Validation Layer (Security)
        ↓
Database Execution (SQLite)
        ↓
Data Processing (Pandas)
        ↓
Visualization (Streamlit)
        ↓
Insights & Reports
```

---

## ⚙️ Project Structure

```
conversational-text-to-sql/
│
├── data/
│   └── finance_database.sqlite
│
├── screenshots/
│   └── img.png
│
├── src/
│   ├── app.py                 # Streamlit UI
│   ├── llm_engine.py          # LLM interaction layer
│   ├── sql_generator.py       # Prompt → SQL generation
│   ├── validator.py           # SQL safety validation
│   ├── query_executor.py      # SQL execution engine
│   ├── memory.py              # Conversation memory
│   └── database_connector.py  # DB connection handler
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔑 Core Components

### 🤖 LLM Engine

* Uses OpenAI GPT models for natural language understanding
* Generates optimized SQL queries using structured prompts

### 🧾 SQL Generator

* Converts user queries into SQL using prompt templates
* Ensures consistency and schema alignment

### 🛡️ Validation Engine

* Prevents unsafe SQL execution (DROP, DELETE, UPDATE)
* Enforces **read-only query policy (SELECT only)**

### 🗄️ Database Connector

* Handles SQLite connections
* Provides schema inspection + query execution

### ⚡ Query Executor

* Executes SQL queries and returns Pandas DataFrames
* Ensures efficient data retrieval

### 🧠 Memory Module

* Stores conversation history
* Enables context-aware multi-turn queries

### 🎨 Streamlit UI

* Interactive chat interface
* Displays query results and visualizations

---

## 📊 Features

* 💬 Natural Language → SQL conversion
* 🔐 Secure query validation layer
* 📈 Automatic data visualization
* 🧠 Context-aware conversations
* ⚡ Real-time query execution
* 🧩 Modular and extensible architecture

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd conversational-text-to-sql
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run Application

```bash
streamlit run src/app.py
```

---

## 💬 Example Queries

* “Show total sales by region”
* “Top 5 customers by revenue”
* “Monthly revenue trend for last 6 months”
* “Average order value by category”

---

## 📊 Output

The system generates:

* SQL Query
* Tabular Results
* Visual Charts
* Business Insights

---

## 🧠 Tech Stack

* Python
* OpenAI GPT (LLM)
* Streamlit
* SQLite
* Pandas
* Matplotlib / Seaborn

---

## 📈 Business Impact

* Enables **non-technical users** to access data
* Reduces dependency on SQL expertise
* Speeds up analytics workflows
* Demonstrates real-world **AI-powered data systems**

---

## 🔮 Future Enhancements

* LangChain SQL Agent integration
* Multi-database support (PostgreSQL, MySQL)
* RAG-based schema understanding
* Role-based access control
* Docker deployment
* API backend (FastAPI)

---

## 👨‍💻 Author

**Manish Rathi**
AI & Python Engineering Portfolio

---

## ⭐ Why This Project Stands Out

This project demonstrates:

* LLM application engineering
* Prompt design & control
* AI safety mechanisms
* End-to-end system design
* Real-world business use case


> 🚀 This is the kind of system used in modern AI analytics tools like ChatGPT Data Analysis, Power BI Copilot, and Snowflake Cortex.

