import pandas as pd


def load_invoices(path):

    df = pd.read_csv(path)

    # convert date
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)

    # compute total value
    df["total_value"] = df["qty"] * df["amount"]

    return df


def sales_by_city(df):

    summary = df.groupby("city")["total_value"].sum().sort_values(ascending=False)

    return summary


def sales_by_product(df):

    summary = df.groupby("product_id")["total_value"].sum().sort_values(ascending=False)

    return summary


def customer_summary(df):

    df["customer_name"] = df["first_name"] + " " + df["last_name"]

    summary = df.groupby("customer_name")["total_value"].sum().sort_values(ascending=False)

    return summary
