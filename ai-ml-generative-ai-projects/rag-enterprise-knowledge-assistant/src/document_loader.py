import os
import re
from langchain_community.document_loaders import PyPDFLoader

def extract_metadata(filename):
    match = re.search(r'(\d{4})-(\d{2})', filename)
    return {
        "year": int(match.group(1)) if match else None,
        "month": int(match.group(2)) if match else None
    }

def load_documents(folder):
    docs = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder, file))
            pages = loader.load()
            metadata = extract_metadata(file)

            for p in pages:
                p.metadata.update(metadata)
                docs.append(p)
    return docs
