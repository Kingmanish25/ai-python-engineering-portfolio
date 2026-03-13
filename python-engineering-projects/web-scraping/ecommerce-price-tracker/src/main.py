import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

def track_prices():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    prices = soup.select(".price_color")

    for price in prices[:10]:
        print(price.text)

if __name__ == "__main__":
    track_prices()
