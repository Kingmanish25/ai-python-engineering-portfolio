import matplotlib.pyplot as plt
import os


def save_forecast_plot(dates, actual, predicted):

    os.makedirs("../screenshots", exist_ok=True)

    plt.figure(figsize=(12,6))

    plt.plot(dates, actual, label="Historical Price")

    plt.plot(dates[-len(predicted):], predicted, label="Forecast", color="red")

    plt.title("Stock Price Forecast")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("../screenshots/forecast_plot.png")

    plt.close()
