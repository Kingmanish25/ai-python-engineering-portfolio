import matplotlib.pyplot as plt


def plot_forecast(dates, actual, predicted):

    plt.figure(figsize=(12,6))

    plt.plot(dates, actual, label="Actual Price")

    plt.plot(dates[-len(predicted):], predicted, label="Forecast")

    plt.title("Stock Price Forecast")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    plt.grid(True)

    plt.show()
