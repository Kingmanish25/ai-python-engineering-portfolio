import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("h2", class_="title")

    for job in jobs:
        print(job.text.strip())

if __name__ == "__main__":
    scrape_jobs()
