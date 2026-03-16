import argparse
import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def scrape_news(url, limit):

    logging.info(f"Fetching news from {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.select(".titleline")

        if not articles:
            logging.warning("No news articles found")
            return

        print("\nLatest News Articles:\n")

        for i, article in enumerate(articles[:limit], 1):

            title = article.text.strip()
            link = article.a["href"]

            print(f"{i}. {title}")
            print(f"   Link: {link}\n")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve news: {e}")


def main():

    parser = argparse.ArgumentParser(description="News Scraper")

    parser.add_argument(
        "--url",
        default="https://news.ycombinator.com/",
        help="News website URL"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of news articles to display"
    )

    args = parser.parse_args()

    scrape_news(args.url, args.limit)


if __name__ == "__main__":
    main()
