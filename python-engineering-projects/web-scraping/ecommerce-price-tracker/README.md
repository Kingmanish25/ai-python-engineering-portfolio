# E-commerce Price Tracker

A Python command-line utility that scrapes product titles and prices from an e-commerce webpage.
This project demonstrates practical Python scripting for **web scraping, product data extraction, and automated price monitoring**.

---

## Overview

The **E-commerce Price Tracker** retrieves product information from an online store and extracts product titles along with their prices.

This project demonstrates:

* Web scraping using Python
* HTML parsing with BeautifulSoup
* Command-line interface (CLI) tool development
* Logging and error handling
* Automated product price tracking

---

## Features

* Extract product names
* Extract product prices
* CLI-based scraping tool
* Logging output for scraping operations
* Lightweight product price monitoring utility

---

## Project Structure

```text id="kzv0d7"
ecommerce-price-tracker
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

```bash id="goh8cd"
git clone <repository-url>
cd ecommerce-price-tracker
```

Install dependencies:

```bash id="n02ac1"
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash id="kn1qkh"
python src/main.py --limit 10
```

---

## Example

Run the price tracker:

```bash id="sx43sn"
python src/main.py --limit 10
```

Example terminal output:

```text id="82b8z7"
2025-01-30 18:10:05 - INFO - Fetching product prices from https://books.toscrape.com/

E-commerce Price Tracker:

1. A Light in the Attic
   Price: £51.77

2. Tipping the Velvet
   Price: £53.74

3. Soumission
   Price: £50.10
```

Another example run:

```text id="rmkqpt"
2025-08-12 18:12:14 - INFO - Fetching product prices from https://books.toscrape.com/

E-commerce Price Tracker:

1. Sharp Objects
   Price: £47.82

2. Sapiens: A Brief History of Humankind
   Price: £54.23

3. The Requiem Red
   Price: £22.65
```

---

## How It Works

1. The script sends an HTTP request to the e-commerce page.
2. The HTML content of the page is retrieved.
3. BeautifulSoup parses the HTML structure.
4. Product titles and prices are extracted using CSS selectors.
5. The extracted data is displayed in the terminal.

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

* Monitoring product prices
* Learning web scraping techniques
* E-commerce data analysis
* Market research automation
* Product price tracking tools

---

## Future Improvements

Possible enhancements include:

* Track price changes over time
* Export product data to CSV
* Scrape multiple pages
* Price alert notifications
* Integration with analytics dashboards

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
