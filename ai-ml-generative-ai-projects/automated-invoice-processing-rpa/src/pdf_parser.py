import pdfplumber
import re


def parse_invoice(file_path):

    with pdfplumber.open(file_path) as pdf:

        text = ""

        for page in pdf.pages:
            text += page.extract_text() + "\n"

    invoice_number = extract_invoice_number(text)
    vendor = extract_vendor(text)
    amount = extract_amount(text)

    return {
        "invoice_number": invoice_number,
        "vendor": vendor,
        "amount": amount
    }


def extract_invoice_number(text):

    match = re.search(r"Invoice\s*#?:?\s*(\w+)", text, re.IGNORECASE)

    if match:
        return match.group(1)

    return "UNKNOWN"


def extract_vendor(text):

    lines = text.split("\n")

    if len(lines) > 0:
        return lines[0]

    return "UNKNOWN"


def extract_amount(text):

    match = re.search(r"Total\s*\$?\s*([0-9,.]+)", text, re.IGNORECASE)

    if match:
        return float(match.group(1).replace(",", ""))

    return 0.0
