import pdfplumber
import re


def parse_invoice(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    invoice_number = extract_invoice_number(text)
    supplier = extract_supplier(text)
    total_amount = extract_total(text)

    return {
        "invoice_number": invoice_number,
        "vendor": supplier,
        "amount": total_amount
    }


def extract_invoice_number(text):

    match = re.search(r"INVOICE\s+(INV-\d+)", text)

    if match:
        return match.group(1)

    return "UNKNOWN"


def extract_supplier(text):

    match = re.search(r"Supplier:\s*(.*)", text)

    if match:
        return match.group(1).strip()

    return "UNKNOWN"


def extract_total(text):

    match = re.search(r"Total Amount:\s*([0-9.]+)", text)

    if match:
        return float(match.group(1))

    return 0.0
