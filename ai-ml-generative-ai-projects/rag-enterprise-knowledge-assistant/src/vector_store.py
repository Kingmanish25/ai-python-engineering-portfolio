from langchain.vectorstores import FAISS

def build_vector_index(chunks, embeddings):

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_db
