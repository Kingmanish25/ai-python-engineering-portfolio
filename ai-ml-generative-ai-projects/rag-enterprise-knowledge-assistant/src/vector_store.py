from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings
import os

VECTOR_PATH = "embeddings/faiss_index"

def load_vectorstore():
    embeddings = get_embeddings()
    return FAISS.load_local(VECTOR_PATH, embeddings, allow_dangerous_deserialization=True)

def save_vectorstore(docs):
    embeddings = get_embeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_PATH)
