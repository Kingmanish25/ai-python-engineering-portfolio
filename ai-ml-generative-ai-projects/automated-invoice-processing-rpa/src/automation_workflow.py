import os
from invoice_reader import get_invoice_files
from pdf_parser import parse_invoice
from validation_engine import validate_invoice
from database_writer import save_invoice
import matplotlib.pyplot as plt


DATA_DIR = "data/invoices"
SCREENSHOT_DIR = "screenshots"


def generate_visualization(amounts):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    plt.figure(figsize=(8,5))
    plt.plot(amounts, marker="o")
    plt.title("Processed Invoice Amounts")
    plt.xlabel("Invoice Index")
    plt.ylabel("Amount")
    plt.grid(True)

    path = os.path.join(SCREENSHOT_DIR, "img.png")
    plt.savefig(path)
    plt.close()

    print("Screenshot saved:", path)


def run_pipeline():

    invoice_files = get_invoice_files(DATA_DIR)

    processed_amounts = []

    for file in invoice_files:

        print("\nProcessing:", file)

        invoice_data = parse_invoice(file)

        if validate_invoice(invoice_data):

            save_invoice(invoice_data)

            processed_amounts.append(invoice_data["amount"])

        else:
            print("Invoice validation failed")

    if processed_amounts:
        generate_visualization(processed_amounts)


if __name__ == "__main__":
    run_pipeline()
