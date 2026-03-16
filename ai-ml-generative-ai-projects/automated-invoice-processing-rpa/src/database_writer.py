import sqlite3


DB_FILE = "invoices.db"


def save_invoice(invoice):

    conn = sqlite3.connect(DB_FILE)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS invoices(
            invoice_number TEXT,
            vendor TEXT,
            amount REAL
        )
        """
    )

    cursor.execute(
        "INSERT INTO invoices VALUES (?, ?, ?)",
        (
            invoice["invoice_number"],
            invoice["vendor"],
            invoice["amount"]
        )
    )

    conn.commit()
    conn.close()

    print("Saved invoice:", invoice["invoice_number"])
