from langchain.retrievers.multi_query import MultiQueryRetriever
from vector_store import load_vectorstore
from llm_inference import get_llm
from metadata_filter import build_filter

def get_retriever(query, year=None, month=None):
    db = load_vectorstore()
    llm = get_llm()

    base = db.as_retriever(
        search_kwargs={
            "k": 20,
            "filter": build_filter(year, month)
        }
    )

    return MultiQueryRetriever.from_llm(
        retriever=base,
        llm=llm
    )
