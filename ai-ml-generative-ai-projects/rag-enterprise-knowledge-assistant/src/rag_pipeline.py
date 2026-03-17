from retriever import get_retriever
from reranker import rerank
from llm_inference import get_llm
from answer_generator import generate_answer

def run_rag(query, year=None, month=None):
    retriever = get_retriever(query, year, month)
    docs = retriever.get_relevant_documents(query)

    docs = rerank(query, docs)

    llm = get_llm()
    answer = generate_answer(llm, query, docs)

    return {
        "answer": answer,
        "sources": [d.metadata for d in docs]
    }
