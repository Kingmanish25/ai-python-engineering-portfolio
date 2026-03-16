import argparse
import logging
import pandas as pd
import yfinance as yf


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def analyze_volatility(ticker, period):

    logging.info(f"Downloading market data for {ticker}")

    data = yf.download(ticker, period=period)

    if data.empty:
        logging.error("No data retrieved from Yahoo Finance")
        return

    returns = data["Close"].pct_change().dropna()

    daily_volatility = returns.std().item()
    annualized_volatility = daily_volatility * (252 ** 0.5)

    print("\nRisk & Volatility Analysis:\n")

    print(f"Ticker: {ticker}")
    print(f"Daily Volatility: {daily_volatility:.4f}")
    print(f"Annualized Volatility: {annualized_volatility:.4f}")

    if annualized_volatility > 0.40:
        print("\nRisk Level: HIGH")
    elif annualized_volatility > 0.20:
        print("\nRisk Level: MEDIUM")
    else:
        print("\nRisk Level: LOW")


def main():

    parser = argparse.ArgumentParser(description="Risk Volatility Analyzer")

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

    args = parser.parse_args()

    analyze_volatility(args.ticker, args.period)


if __name__ == "__main__":
    main()
