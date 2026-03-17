from llm_inference import get_llm

def plan_query(query):
    llm = get_llm()

    prompt = f"""
Classify this query:

Query: {query}

Return:
- "RAG" if needs document retrieval
- "DIRECT" if general knowledge
"""

    decision = llm.invoke(prompt)

    return "RAG" if "RAG" in decision else "DIRECT"
