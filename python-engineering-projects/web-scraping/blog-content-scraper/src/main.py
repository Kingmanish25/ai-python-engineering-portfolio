import argparse
import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def scrape_blog(url):

    logging.info(f"Fetching blog content from {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.select(".post-title")

        if not posts:
            logging.warning("No blog posts found")
            return

        print("\nLatest Blog Posts:\n")

        for i, post in enumerate(posts, 1):
            print(f"{i}. {post.text.strip()}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve blog content: {e}")


def main():

    parser = argparse.ArgumentParser(description="Blog Content Scraper")

    parser.add_argument(
        "--url",
        default="https://blog.python.org/",
        help="Blog URL to scrape (default: Python official blog)"
    )

    args = parser.parse_args()

    scrape_blog(args.url)


if __name__ == "__main__":
    main()
