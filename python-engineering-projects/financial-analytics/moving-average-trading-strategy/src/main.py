import argparse
import logging
import pandas as pd
import yfinance as yf


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def moving_average_strategy(ticker, period, window):

    logging.info(f"Downloading market data for {ticker}")

    data = yf.download(ticker, period=period)

    if data.empty:
        logging.error("No data retrieved from Yahoo Finance")
        return

    data[f"MA{window}"] = data["Close"].rolling(window=window).mean()

    latest_price = data["Close"].iloc[-1].item()
    latest_ma = data[f"MA{window}"].iloc[-1].item()

    print("\nMarket Analysis:\n")

    print(f"Ticker: {ticker}")
    print(f"Latest Price: {latest_price:.2f}")
    print(f"{window}-Day Moving Average: {latest_ma:.2f}")

    if latest_price > latest_ma:
        print("\nSignal: BUY (Price above moving average)")
    else:
        print("\nSignal: SELL (Price below moving average)")


def main():

    parser = argparse.ArgumentParser(description="Moving Average Trading Strategy")

    parser.add_argument(
        "--ticker",
        default="AAPL",
        help="Stock ticker symbol (default: AAPL)"
    )

    parser.add_argument(
        "--period",
        default="3mo",
        help="Market data period (default: 3mo)"
    )

    parser.add_argument(
        "--window",
        type=int,
        default=20,
        help="Moving average window (default: 20)"
    )

    args = parser.parse_args()

    moving_average_strategy(args.ticker, args.period, args.window)


if __name__ == "__main__":
    main()
