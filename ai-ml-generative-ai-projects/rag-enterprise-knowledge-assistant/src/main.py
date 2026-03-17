from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import run_rag
from query_planner import plan_query
from cache import get_cache, set_cache
from llm_inference import get_llm

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(q: Query):
    cached = get_cache(q.query)
    if cached:
        return cached

    decision = plan_query(q.query)

    if decision == "RAG":
        result = run_rag(q.query)
    else:
        llm = get_llm()
        result = {"answer": llm.invoke(q.query)}

    set_cache(q.query, result)
    return result
