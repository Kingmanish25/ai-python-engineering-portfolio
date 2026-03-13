import requests
from bs4 import BeautifulSoup

URL = "https://blog.python.org/"

def scrape_blog():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    posts = soup.select(".post-title")

    for post in posts:
        print(post.text.strip())

if __name__ == "__main__":
    scrape_blog()
