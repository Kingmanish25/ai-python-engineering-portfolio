import streamlit as st
from rag_pipeline import run_rag
from ingest import ingest
import os

st.title("💼 Enterprise RAG Assistant")

uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

if uploaded_files:
    os.makedirs("data/uploads", exist_ok=True)

    for file in uploaded_files:
        with open(f"data/uploads/{file.name}", "wb") as f:
            f.write(file.getbuffer())

    ingest()  # re-ingest
    st.success("Documents indexed!")

query = st.text_input("Ask a question:")

if query:
    result = run_rag(query)

    st.write(result["answer"])

    with st.expander("Sources"):
        st.write(result["sources"])
