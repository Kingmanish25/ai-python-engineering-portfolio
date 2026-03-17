FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]

def validate_sql(query):
    query_upper = query.upper()
    
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in query_upper:
            raise ValueError("Unsafe query detected!")
    
    if not query_upper.strip().startswith("SELECT"):
        raise ValueError("Only SELECT queries allowed!")
    
    return True
