import os

from document_loader import load_documents
from chunking import chunk_documents
from embeddings import load_embeddings
from vector_store import build_vector_index
from retriever import retrieve_context
from llm_inference import load_llm
from answer_generator import generate_answer


def initialize_rag():

    print("Loading financial documents...")

    docs = load_documents("../data/financial_documents_sample")

    print("Chunking documents...")

    chunks = chunk_documents(docs)

    print("Loading embedding model...")

    embeddings = load_embeddings()

    print("Building FAISS vector database...")

    vector_db = build_vector_index(chunks, embeddings)

    print("Loading local LLM (Ollama)...")

    llm = load_llm()

    return vector_db, llm


def run_query(vector_db, llm):

    while True:

        query = input("\nAsk a question about financial documents (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        docs = retrieve_context(vector_db, query)

        context = "\n".join([d.page_content for d in docs])

        answer = generate_answer(llm, context, query)

        print("\nAnswer:\n", answer)

        print("\nSources:")
        for i, d in enumerate(docs):
            print(f"{i+1}. {d.metadata}")


def main():

    vector_db, llm = initialize_rag()

    run_query(vector_db, llm)


if __name__ == "__main__":
    main()
