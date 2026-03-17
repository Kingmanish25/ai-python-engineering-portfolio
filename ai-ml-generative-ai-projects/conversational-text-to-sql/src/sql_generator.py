def build_prompt(user_query):
    return f"""
Convert the following natural language query into SQL.

Rules:
- Only generate SQL
- Use table: finance_data
- Do NOT use DELETE, UPDATE, DROP
- Only SELECT queries allowed

User Query:
{user_query}
"""
