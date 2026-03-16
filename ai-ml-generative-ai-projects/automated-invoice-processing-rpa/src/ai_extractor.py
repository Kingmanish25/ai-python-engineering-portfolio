import re


def extract_invoice_ai(text):

    fields = {}

    patterns = {
        "invoice_number": r"INVOICE\s+(INV-\d+)",
        "supplier": r"Supplier:\s*(.*)",
        "invoice_date": r"Invoice Date:\s*(.*)",
        "buyer": r"Buyer:\s*(.*)",
        "total_amount": r"Total Amount:\s*([0-9.]+)",
        "tax": r"Tax.*:\s*([0-9.]+)"
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, text)

        if match:
            fields[key] = match.group(1).strip()
        else:
            fields[key] = None

    if fields["total_amount"]:
        fields["total_amount"] = float(fields["total_amount"])

    if fields["tax"]:
        fields["tax"] = float(fields["tax"])

    return fields
