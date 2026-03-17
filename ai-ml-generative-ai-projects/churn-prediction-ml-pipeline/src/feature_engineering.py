from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def prepare_features(df):

    X = df.drop(columns=["Exited", "CustomerId"])
    y = df["Exited"]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


def split_data(X, y):

    return train_test_split(X, y, test_size=0.2, random_state=42)
