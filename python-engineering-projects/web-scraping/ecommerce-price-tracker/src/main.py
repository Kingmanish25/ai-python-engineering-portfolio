import argparse
import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def track_prices(url, limit):

    logging.info(f"Fetching product prices from {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.select(".product_pod")

        if not products:
            logging.warning("No products found on the page")
            return

        print("\nE-commerce Price Tracker:\n")

        for i, product in enumerate(products[:limit], 1):

            title = product.h3.a["title"]
            price = product.select_one(".price_color").text

            print(f"{i}. {title}")
            print(f"   Price: {price}\n")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve product data: {e}")


def main():

    parser = argparse.ArgumentParser(description="E-commerce Price Tracker")

    parser.add_argument(
        "--url",
        default="https://books.toscrape.com/",
        help="E-commerce page URL (default: books.toscrape.com)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of products to display (default: 10)"
    )

    args = parser.parse_args()

    track_prices(args.url, args.limit)


if __name__ == "__main__":
    main()
