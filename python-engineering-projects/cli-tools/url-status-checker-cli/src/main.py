import argparse
import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_url(url):

    try:
        response = requests.get(url, timeout=5)

        logging.info(f"URL checked: {url}")
        logging.info(f"Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to reach URL: {e}")


def main():

    parser = argparse.ArgumentParser(description="URL Status Checker CLI Tool")

    parser.add_argument(
        "--url",
        required=True,
        help="URL to check"
    )

    args = parser.parse_args()

    check_url(args.url)


if __name__ == "__main__":
    main()
