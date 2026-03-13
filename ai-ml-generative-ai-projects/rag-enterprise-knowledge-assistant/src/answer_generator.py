def generate_answer(llm, context, query):

    prompt = f"""
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}

    Provide source references.
    """

    response = llm(prompt)

    return response
