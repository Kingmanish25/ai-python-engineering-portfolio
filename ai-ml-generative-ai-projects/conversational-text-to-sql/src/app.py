import streamlit as st

from llm_engine import generate_sql_from_llm
from sql_generator import build_prompt
from query_executor import execute_query
from validator import validate_sql
from memory import ChatMemory

memory = ChatMemory()

st.set_page_config(page_title="Text-to-SQL AI", layout="wide")

st.title("💬 Conversational Text-to-SQL AI")

query = st.text_input("Ask your question:")

if st.button("Run Query"):

    try:
        context = memory.get_context()

        prompt = build_prompt(query + "\nContext:\n" + context)

        sql_query = generate_sql_from_llm(prompt)

        validate_sql(sql_query)

        st.code(sql_query, language="sql")

        df = execute_query(sql_query)

        st.dataframe(df)

        if not df.empty:
            st.bar_chart(df.select_dtypes(include=["number"]))

        memory.add(query, sql_query)

    except Exception as e:
        st.error(f"Error: {str(e)}")
