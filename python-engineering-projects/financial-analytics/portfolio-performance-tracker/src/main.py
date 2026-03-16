import argparse
import logging
import pandas as pd
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def analyze_portfolio(input_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Portfolio file not found: {input_file}")

    df = pd.read_csv(input_file)

    logging.info("Portfolio data loaded successfully")

    df["Profit"] = df["Current_Value"] - df["Investment"]
    df["Return_%"] = (df["Profit"] / df["Investment"]) * 100

    total_investment = df["Investment"].sum()
    total_value = df["Current_Value"].sum()
    total_profit = total_value - total_investment

    print("\nPortfolio Performance:\n")
    print(df)

    print("\nPortfolio Summary:\n")

    print(f"Total Investment : {total_investment:.2f}")
    print(f"Current Value    : {total_value:.2f}")
    print(f"Total Profit     : {total_profit:.2f}")


def main():

    parser = argparse.ArgumentParser(description="Portfolio Performance Tracker")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to portfolio CSV file"
    )

    args = parser.parse_args()

    analyze_portfolio(args.input)


if __name__ == "__main__":
    main()
