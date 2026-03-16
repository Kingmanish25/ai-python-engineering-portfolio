import sqlite3

DB = "invoices.db"


def save_invoice(data):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS invoices(
            invoice_number TEXT,
            supplier TEXT,
            invoice_date TEXT,
            buyer TEXT,
            total_amount REAL,
            tax REAL
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO invoices VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            data["invoice_number"],
            data["supplier"],
            data["invoice_date"],
            data["buyer"],
            data["total_amount"],
            data["tax"]
        )
    )

    conn.commit()

    conn.close()

    print("Saved invoice:", data["invoice_number"])
