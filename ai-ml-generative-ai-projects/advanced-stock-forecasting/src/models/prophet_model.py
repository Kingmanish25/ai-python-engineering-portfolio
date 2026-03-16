from prophet import Prophet
import pandas as pd


def train_prophet(df):
    """
    Train Prophet forecasting model
    """

    prophet_df = df.reset_index()[["Date", "Close"]]
    prophet_df.columns = ["ds", "y"]

    model = Prophet()

    model.fit(prophet_df)

    return model


def forecast_prophet(model, periods=30):

    future = model.make_future_dataframe(periods=periods)

    forecast = model.predict(future)

    return forecast
