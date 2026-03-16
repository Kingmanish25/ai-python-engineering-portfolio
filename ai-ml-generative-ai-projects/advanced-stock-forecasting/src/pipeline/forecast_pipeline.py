import logging

from data_loader import load_data
from indicators import compute_rsi, compute_macd
from hyperparameter_tuning import tune_arima
from models.arima_model import train_arima
from evaluation.evaluate import evaluate_model
from visualization import save_forecast_plot


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():

    logging.info("Loading dataset")

    df = load_data()

    close = df["Close"]

    logging.info("Computing technical indicators")

    df["RSI"] = compute_rsi(close)

    macd, signal = compute_macd(close)

    df["MACD"] = macd
    df["MACD_SIGNAL"] = signal

    logging.info("Splitting train and test data")

    train = close[:-30]
    test = close[-30:]

    logging.info("Running ARIMA hyperparameter tuning")

    best_order = tune_arima(train)

    logging.info(f"Best ARIMA order found: {best_order}")

    logging.info("Training ARIMA model")

    model = train_arima(train, order=best_order)

    logging.info("Generating forecast")

    forecast = model.forecast(steps=30)

    logging.info("Evaluating model")

    metrics = evaluate_model(test, forecast)

    print("\nModel Performance Metrics\n")

    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    logging.info("Saving forecast visualization")

    save_forecast_plot(df.index, close, forecast)

    logging.info("Forecast pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
