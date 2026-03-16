def validate_invoice(invoice):

    if invoice["invoice_number"] == "UNKNOWN":
        print("Invalid invoice number")
        return False

    if invoice["amount"] <= 0:
        print("Invalid invoice amount")
        return False

    return True
