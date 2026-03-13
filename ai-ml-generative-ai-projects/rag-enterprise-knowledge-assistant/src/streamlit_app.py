import streamlit as st

from src.rag_pipeline import run_rag

st.title("Enterprise Financial RAG Assistant")

query = st.text_input("Ask about financial documents")

if query:

    response = run_rag(query)

    st.write(response)
