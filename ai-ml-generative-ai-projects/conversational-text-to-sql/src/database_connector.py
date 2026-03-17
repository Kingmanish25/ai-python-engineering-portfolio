import sqlite3
from contextlib import contextmanager
import pandas as pd


class DatabaseConnector:
    """
    Handles database connections and operations for SQLite.
    Designed for safe and reusable query execution.
    """

    def __init__(self, db_path: str = "data/finance_database.sqlite"):
        self.db_path = db_path

    @contextmanager
    def get_connection(self):
        """
        Context manager for safe DB connection handling.
        """
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def test_connection(self):
        """
        Test if database connection is successful.
        """
        try:
            with self.get_connection() as conn:
                conn.execute("SELECT 1")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def get_tables(self):
        """
        Fetch all table names in the database.
        """
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        with self.get_connection() as conn:
            result = conn.execute(query).fetchall()
        return [row[0] for row in result]

    def get_schema(self, table_name: str):
        """
        Get schema (columns) of a specific table.
        """
        query = f"PRAGMA table_info({table_name});"
        with self.get_connection() as conn:
            result = conn.execute(query).fetchall()

        schema = [
            {
                "column": row[1],
                "type": row[2],
                "not_null": row[3],
                "default": row[4],
                "primary_key": row[5],
            }
            for row in result
        ]

        return schema

    def execute_query(self, query: str) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a Pandas DataFrame.
        """
        try:
            with self.get_connection() as conn:
                df = pd.read_sql_query(query, conn)
            return df

        except Exception as e:
            raise RuntimeError(f"Query execution failed: {e}")

    def preview_table(self, table_name: str, limit: int = 5):
        """
        Preview top rows of a table.
        """
        query = f"SELECT * FROM {table_name} LIMIT {limit};"
        return self.execute_query(query)

    def get_row_count(self, table_name: str):
        """
        Get total number of rows in a table.
        """
        query = f"SELECT COUNT(*) as count FROM {table_name};"
        df = self.execute_query(query)
        return int(df["count"][0])
