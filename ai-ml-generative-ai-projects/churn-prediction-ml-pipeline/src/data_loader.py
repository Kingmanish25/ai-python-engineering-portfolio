import pandas as pd


def load_data(path):

    df = pd.read_csv(path)

    # Remove € and convert to float
    df["Balance"] = df["Balance"].replace("[€,]", "", regex=True).astype(float)

    # Convert categorical to numeric
    df["HasCrCard"] = df["HasCrCard"].map({"Yes": 1, "No": 0})
    df["IsActiveMember"] = df["IsActiveMember"].map({"Yes": 1, "No": 0})

    # Drop duplicates
    df = df.drop_duplicates()

    return df
