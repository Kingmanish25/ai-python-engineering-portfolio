import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Web_scraping"

def extract_wikipedia():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.select("p")

    for p in paragraphs[:5]:
        print(p.text.strip())

if __name__ == "__main__":
    extract_wikipedia()
