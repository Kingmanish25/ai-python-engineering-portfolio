import argparse
import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def scrape_jobs(url, limit):

    logging.info(f"Fetching job listings from {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.select(".card-content")

        if not jobs:
            logging.warning("No job listings found")
            return

        print("\nJob Listings:\n")

        for i, job in enumerate(jobs[:limit], 1):

            title = job.select_one(".title").text.strip()
            company = job.select_one(".company").text.strip()
            location = job.select_one(".location").text.strip()

            print(f"{i}. {title}")
            print(f"   Company : {company}")
            print(f"   Location: {location}\n")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve job listings: {e}")


def main():

    parser = argparse.ArgumentParser(description="Job Listing Scraper")

    parser.add_argument(
        "--url",
        default="https://realpython.github.io/fake-jobs/",
        help="Job listing website URL"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of jobs to display"
    )

    args = parser.parse_args()

    scrape_jobs(args.url, args.limit)


if __name__ == "__main__":
    main()
