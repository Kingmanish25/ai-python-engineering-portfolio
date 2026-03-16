# News Scraper

A Python command-line utility that scrapes news article titles and links from a news website.
This project demonstrates practical Python scripting for **web scraping, news data extraction, and automated content monitoring**.

---

## Overview

The **News Scraper** retrieves the latest news articles from a website and extracts the article titles and links.

This project demonstrates:

* Web scraping using Python
* HTML parsing with BeautifulSoup
* Command-line interface (CLI) tool development
* Logging and error handling
* Structured content extraction

---

## Features

* Extract news article titles
* Extract article links
* CLI-based scraping tool
* Logging output for scraping operations
* Lightweight news aggregation utility

---

## Project Structure

```text id="uln3a0"
news-scraper
│
├── README.md
├── requirements.txt
│
└── src
    └── main.py
```

---

## Installation

Clone the repository and navigate to the project directory.

```bash id="wxtqv7"
git clone <repository-url>
cd news-scraper
```

Install dependencies:

```bash id="bcl7x1"
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash id="ntxnp1"
python src/main.py --limit 10
```

---

## Example

Run the news scraper:

```bash id="ovh7x6"
python src/main.py --limit 10
```

Example terminal output:

```text id="uxo27n"
2025-02-09 18:10:05 - INFO - Fetching news from https://news.ycombinator.com/

Latest News Articles:

1. OpenAI releases new AI model
   Link: https://example.com/article1

2. Python 3.13 announced
   Link: https://example.com/article2

3. New database engine released
   Link: https://example.com/article3
```

Another example run:

```text id="upcr7o"
2025-08-24 18:12:14 - INFO - Fetching news from https://news.ycombinator.com/

Latest News Articles:

1. AI startups raise record funding
   Link: https://example.com/article4

2. Advances in machine learning research
   Link: https://example.com/article5

3. Open source tools for developers
   Link: https://example.com/article6
```

---

## How It Works

1. The script sends an HTTP request to the news website.
2. The HTML content of the page is retrieved.
3. BeautifulSoup parses the HTML structure.
4. Article titles and links are extracted using CSS selectors.
5. The extracted news data is displayed in the terminal.

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* HTML parsing
* CLI utilities
* Logging systems

---

## Use Cases

This tool can be useful for:

* Monitoring technology news
* Learning web scraping techniques
* Building news aggregation systems
* Content monitoring automation
* Data collection for analytics

---

## Future Improvements

Possible enhancements include:

* Scraping multiple news pages
* Exporting news data to CSV or JSON
* Keyword-based article filtering
* Building a news recommendation system
* Integrating with analytics dashboards

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
