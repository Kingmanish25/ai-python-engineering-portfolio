def validate_invoice(invoice):

    errors = []

    if "invoice_id" not in invoice:
        errors.append("Missing invoice ID")

    if "amount" not in invoice:
        errors.append("Missing amount")

    if invoice.get("amount", 0) <= 0:
        errors.append("Invalid amount")

    if "vendor" not in invoice:
        errors.append("Missing vendor")

    if errors:
        return False, errors

    return True, []
