import pandas as pd


def load_data(path="../data/retail_sales.csv"):

    df = pd.read_csv(path)

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    return df


def train_test_split_time(df, test_size=30):

    train = df.iloc[:-test_size]

    test = df.iloc[-test_size:]

    return train, test
