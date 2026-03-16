import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_large_orders(df, threshold=10):

    anomalies = df[df["qty"] > threshold]

    return anomalies


def ml_anomaly_detection(df):

    features = df[["qty", "amount"]]

    model = IsolationForest(contamination=0.05, random_state=42)

    df["anomaly"] = model.fit_predict(features)

    anomalies = df[df["anomaly"] == -1]

    return anomalies
