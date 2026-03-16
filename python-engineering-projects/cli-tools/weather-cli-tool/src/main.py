import argparse
import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_weather(city):

    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            logging.info(f"Weather data for {city}")
            print(response.text)
        else:
            logging.error(f"Failed to retrieve weather data (status code {response.status_code})")

    except requests.exceptions.RequestException as e:
        logging.error(f"Network error occurred: {e}")


def main():

    parser = argparse.ArgumentParser(description="Weather CLI Tool")

    parser.add_argument(
        "--city",
        required=True,
        help="City name to fetch weather information"
    )

    args = parser.parse_args()

    get_weather(args.city)


if __name__ == "__main__":
    main()
