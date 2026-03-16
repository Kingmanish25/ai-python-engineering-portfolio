import argparse
import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


API_URL = "https://api.coingecko.com/api/v3/simple/price"


def analyze_crypto(coins, currency):

    params = {
        "ids": coins,
        "vs_currencies": currency
    }

    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

        logging.info("Crypto market data retrieved successfully")

        print("\nCrypto Market Prices:\n")

        for coin, price_data in data.items():
            print(f"{coin.capitalize()} : {price_data[currency]} {currency.upper()}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch crypto data: {e}")


def main():

    parser = argparse.ArgumentParser(description="Crypto Market Analyzer")

    parser.add_argument(
        "--coins",
        default="bitcoin,ethereum",
        help="Comma-separated crypto coin IDs (default: bitcoin,ethereum)"
    )

    parser.add_argument(
        "--currency",
        default="usd",
        help="Currency for price comparison (default: usd)"
    )

    args = parser.parse_args()

    analyze_crypto(args.coins, args.currency)


if __name__ == "__main__":
    main()
