import argparse
import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def get_crypto_price(currency):

    logging.info("Fetching Bitcoin price from CoinDesk API")

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        price = data["bpi"][currency]["rate"]

        print("\nCrypto Price:\n")
        print(f"Bitcoin Price ({currency}): {price}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve crypto price: {e}")


def main():

    parser = argparse.ArgumentParser(description="Crypto Price Scraper")

    parser.add_argument(
        "--currency",
        default="USD",
        help="Currency to display Bitcoin price (default: USD)"
    )

    args = parser.parse_args()

    get_crypto_price(args.currency)


if __name__ == "__main__":
    main()
