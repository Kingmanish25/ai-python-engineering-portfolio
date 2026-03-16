import re


def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def validate_row(row):

    errors = []

    if row["qty"] <= 0:
        errors.append("Invalid quantity")

    if row["amount"] <= 0:
        errors.append("Invalid price")

    if not validate_email(row["email"]):
        errors.append("Invalid email")

    if row["product_id"] <= 0:
        errors.append("Invalid product id")

    return errors


def validate_dataset(df):

    validation_errors = []

    for idx, row in df.iterrows():

        errors = validate_row(row)

        if errors:
            validation_errors.append(
                {
                    "row": idx,
                    "errors": errors
                }
            )

    return validation_errors
