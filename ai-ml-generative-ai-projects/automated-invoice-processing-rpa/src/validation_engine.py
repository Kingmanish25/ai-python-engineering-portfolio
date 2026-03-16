def validate_invoice(data):

    if not data["invoice_number"]:
        return False

    if not data["supplier"]:
        return False

    if not data["total_amount"]:
        return False

    return True
