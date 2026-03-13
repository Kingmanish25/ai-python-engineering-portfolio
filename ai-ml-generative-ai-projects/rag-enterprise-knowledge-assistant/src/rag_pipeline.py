from retriever import retrieve_context
from answer_generator import generate_answer

def run_rag(vector_db, llm, query):

    docs = retrieve_context(vector_db, query)

    context = "\n".join([d.page_content for d in docs])

    answer = generate_answer(llm, context, query)

    return answer
