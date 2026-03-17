from document_loader import load_documents
from chunking import chunk_documents
from vector_store import save_vectorstore

def ingest():
    docs = []
    docs.extend(load_documents("data/invoices"))
    docs.extend(load_documents("data/reports"))
    docs.extend(load_documents("data/uploads"))

    chunks = chunk_documents(docs)
    save_vectorstore(chunks)

if __name__ == "__main__":
    ingest()
