def generate_answer(llm, query, docs):
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are an enterprise financial assistant.

Use ONLY the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    return llm.invoke(prompt)
