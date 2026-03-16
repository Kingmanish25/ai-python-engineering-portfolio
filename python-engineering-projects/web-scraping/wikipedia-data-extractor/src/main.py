import argparse
import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_wikipedia(url, limit):

    logging.info(f"Fetching Wikipedia page: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.select("p")

        if not paragraphs:
            logging.warning("No paragraphs found on the page")
            return

        print("\nWikipedia Extracted Content:\n")

        count = 0
        for paragraph in paragraphs:

            text = paragraph.text.strip()

            if text:
                print(f"{count+1}. {text}\n")
                count += 1

            if count >= limit:
                break

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve Wikipedia page: {e}")


def main():

    parser = argparse.ArgumentParser(description="Wikipedia Data Extractor")

    parser.add_argument(
        "--url",
        default="https://en.wikipedia.org/wiki/Web_scraping",
        help="Wikipedia article URL"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Number of paragraphs to extract"
    )

    args = parser.parse_args()

    extract_wikipedia(args.url, args.limit)


if __name__ == "__main__":
    main()
