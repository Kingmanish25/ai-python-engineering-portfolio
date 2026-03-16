from invoice_reader import get_invoice_files
from pdf_parser import extract_text
from ai_extractor import extract_invoice_ai
from validation_engine import validate_invoice
from database_writer import save_invoice
import matplotlib.pyplot as plt
import os


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

    plt.savefig(os.path.join(SCREENSHOT_DIR, "img.png"))

    plt.close()


def run_pipeline():

    files = get_invoice_files(DATA_DIR)

    amounts = []

    for file in files:

        print("\nProcessing:", file)

        text = extract_text(file)

        invoice_data = extract_invoice_ai(text)

        if validate_invoice(invoice_data):

            save_invoice(invoice_data)

            amounts.append(invoice_data["total_amount"])

        else:

            print("Validation failed")

    if amounts:
        generate_visualization(amounts)


if __name__ == "__main__":
    run_pipeline()
