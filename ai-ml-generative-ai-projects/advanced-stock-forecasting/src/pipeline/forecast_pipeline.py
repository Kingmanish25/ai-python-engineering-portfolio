from data_loader import load_data
from indicators import compute_rsi, compute_macd
from models.arima_model import train_arima
from evaluation.evaluate import evaluate_model
from visualization import plot_forecast


def run_pipeline():

    df = load_data()

    close = df["Close"]

    df["RSI"] = compute_rsi(close)

    macd, signal = compute_macd(close)

    df["MACD"] = macd

    train = close[:-30]
    test = close[-30:]

    model = train_arima(train)

    forecast = model.forecast(steps=30)

    metrics = evaluate_model(test, forecast)

    print("Model Performance")

    print(metrics)

    plot_forecast(df.index, close, forecast)


if __name__ == "__main__":
    run_pipeline()
