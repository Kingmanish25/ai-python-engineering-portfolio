import argparse
import logging
import yfinance as yf


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def analyze_stock(ticker, period):

    logging.info(f"Downloading stock data for {ticker}")

    stock = yf.Ticker(ticker)

    data = stock.history(period=period)

    if data.empty:
        logging.error("No market data retrieved")
        return

    latest_close = data["Close"].iloc[-1].item()
    highest_price = data["High"].max().item()
    lowest_price = data["Low"].min().item()
    avg_price = data["Close"].mean().item()

    print("\nStock Price Analysis:\n")

    print(f"Ticker: {ticker}")
    print(f"Latest Closing Price: {latest_close:.2f}")
    print(f"Highest Price ({period}): {highest_price:.2f}")
    print(f"Lowest Price ({period}): {lowest_price:.2f}")
    print(f"Average Price ({period}): {avg_price:.2f}")


def main():

    parser = argparse.ArgumentParser(description="Stock Price Analyzer")

    parser.add_argument(
        "--ticker",
        default="AAPL",
        help="Stock ticker symbol (default: AAPL)"
    )

    parser.add_argument(
        "--period",
        default="1mo",
        help="Market data period (default: 1mo)"
    )

    args = parser.parse_args()

    analyze_stock(args.ticker, args.period)


if __name__ == "__main__":
    main()
