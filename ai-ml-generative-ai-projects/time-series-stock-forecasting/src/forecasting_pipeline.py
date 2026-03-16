from data_loader import load_data
from arima_model import train_arima, forecast_arima
from prophet_model import train_prophet, forecast_prophet
from lstm_model import train_lstm

import matplotlib.pyplot as plt


def run_pipeline():

    df = load_data()

    close = df["Close"]

    print("Training ARIMA model")

    arima_model = train_arima(close)

    arima_forecast = forecast_arima(arima_model)

    print("Training Prophet model")

    prophet_model = train_prophet(df)

    prophet_forecast = forecast_prophet(prophet_model)

    print("Training LSTM model")

    lstm_model, scaler = train_lstm(close)

    print("Forecasting completed")

    plot_results(close, arima_forecast)


def plot_results(series, forecast):

    plt.figure(figsize=(10, 5))

    plt.plot(series[-100:], label="Historical")

    plt.plot(range(len(series), len(series) + len(forecast)), forecast, label="Forecast")

    plt.legend()

    plt.title("Stock Price Forecast")

    plt.show()


if __name__ == "__main__":

    run_pipeline()
