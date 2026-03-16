import pandas as pd
from prophet import Prophet


def train_prophet(df):

    data = df.reset_index()[["Date", "Close"]]

    data.columns = ["ds", "y"]

    model = Prophet()

    model.fit(data)

    return model


def forecast_prophet(model, periods=30):

    future = model.make_future_dataframe(periods=periods)

    forecast = model.predict(future)

    return forecast
