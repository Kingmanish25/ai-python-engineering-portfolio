import pandas as pd

from email_parser import parse_email
from invoice_classifier import InvoiceClassifier
from validation_engine import validate_invoice


def load_training_data():

    df = pd.read_csv("../data/data.csv")

    texts = df["invoice_text"]

    labels = df["category"]

    return texts, labels


def run_pipeline():

    print("Loading training data")

    texts, labels = load_training_data()

    classifier = InvoiceClassifier()

    classifier.train(texts, labels)

    print("Classifier trained")

    sample_invoice = {
        "invoice_id": "INV001",
        "vendor": "ABC Corp",
        "amount": 1200,
        "text": "Invoice for office supplies"
    }

    print("Validating invoice")

    valid, errors = validate_invoice(sample_invoice)

    if not valid:
        print("Validation errors:", errors)
        return

    category = classifier.predict(sample_invoice["text"])

    print("Invoice classified as:", category)

    print("Automation pipeline completed")


if __name__ == "__main__":

    run_pipeline()
