from invoice_processor import (
    load_invoices,
    sales_by_city,
    sales_by_product,
    customer_summary
)

from validation_engine import validate_dataset

from anomaly_detection import (
    detect_large_orders,
    ml_anomaly_detection
)


def run_pipeline():

    print("Loading invoice dataset...")

    df = load_invoices("../data/data1.csv")

    print("Total invoices:", len(df))

    print("\nRunning validation checks...")

    validation_errors = validate_dataset(df)

    if validation_errors:
        print("Validation issues found:")
        for err in validation_errors[:5]:
            print(err)
    else:
        print("No validation issues found")

    print("\nDetecting large orders...")

    large_orders = detect_large_orders(df)

    print("Large orders detected:", len(large_orders))

    print("\nRunning ML anomaly detection...")

    anomalies = ml_anomaly_detection(df)

    print("ML anomalies detected:", len(anomalies))

    print("\nGenerating reports...")

    print("\nTop Cities by Revenue")
    print(sales_by_city(df).head())

    print("\nTop Products by Revenue")
    print(sales_by_product(df).head())

    print("\nTop Customers")
    print(customer_summary(df).head())

    print("\nAutomation pipeline completed successfully")


if __name__ == "__main__":

    run_pipeline()
