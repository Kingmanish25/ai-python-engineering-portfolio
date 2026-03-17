import pandas as pd


def load_data(path):

    df = pd.read_csv(path)

    # Convert datetime
    df["purchase_time"] = pd.to_datetime(df["purchase_time"])

    # Basic cleaning
    df = df.dropna()

    return df
