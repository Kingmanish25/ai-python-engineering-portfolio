import pandas as pd


def load_data(path="data/data.csv"):
    """
    Load and preprocess stock dataset
    """

    df = pd.read_csv(path)

    df.rename(columns={"Adj Close": "Adj_Close"}, inplace=True)

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

    df = df.sort_values("Date")

    df.set_index("Date", inplace=True)

    return df
