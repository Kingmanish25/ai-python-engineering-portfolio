import pandas as pd
import sqlite3

def execute_query(query, db_path="data/finance_database.sqlite"):
    conn = sqlite3.connect(db_path)
    
    try:
        df = pd.read_sql_query(query, conn)
        return df
    finally:
        conn.close()
