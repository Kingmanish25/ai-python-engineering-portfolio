from data_loader import load_data
from arima_model import train_arima, forecast_arima
from prophet_model import train_prophet, forecast_prophet
from lstm_model import train_lstm
from evaluate import evaluate_model

import matplotlib.pyplot as plt


def run_pipeline():

    print("Loading dataset...")

    df = load_data()

    series = df["Close"]

    train = series[:-30]
    test = series[-30:]

    print("Training ARIMA model...")

    arima_model = train_arima(train)

    arima_pred = forecast_arima(arima_model, steps=30)

    arima_metrics = evaluate_model(test, arima_pred)

    print("ARIMA Results:", arima_metrics)

    print("Training Prophet model...")

    prophet_model = train_prophet(df)

    prophet_forecast = forecast_prophet(prophet_model)

    print("Training LSTM model...")

    lstm_model, scaler = train_lstm(series)

    print("Forecast pipeline completed")

    plt.figure(figsize=(12, 6))

    plt.plot(series.index, series.values, label="Actual")

    plt.plot(test.index, arima_pred, label="ARIMA Forecast")

    plt.legend()

    plt.title("Stock Forecast")

    plt.show()


if __name__ == "__main__":
    run_pipeline()
