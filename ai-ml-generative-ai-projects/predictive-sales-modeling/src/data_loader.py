import pandas as pd


def load_data(path="../data/retail_sales.csv"):

    df = pd.read_csv(path)

    # convert date
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

    # ensure numeric fields
    df["Quantity"] = pd.to_numeric(df["Quantity"])
    df["Price per Unit"] = pd.to_numeric(df["Price per Unit"])
    df["Total Amount"] = pd.to_numeric(df["Total Amount"])

    # sort
    df = df.sort_values("date")

    return df


def aggregate_daily_sales(df):

    daily_sales = (
        df.groupby("date")["Total Amount"]
        .sum()
        .reset_index()
        .rename(columns={"Total Amount": "sales"})
    )

    return daily_sales


def train_test_split_time(df, test_size=30):

    train = df.iloc[:-test_size]
    test = df.iloc[-test_size:]

    return train, test
