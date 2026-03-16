# Crypto Price Scraper

A Python command-line utility that retrieves the current Bitcoin price using the CoinDesk API.
This project demonstrates practical Python scripting for **API-based web scraping, JSON data parsing, and cryptocurrency price monitoring**.

---

## Overview

The **Crypto Price Scraper** fetches real-time Bitcoin price data from the CoinDesk API and displays it in the terminal.

This project demonstrates:

* API-based data scraping
* JSON data parsing
* Command-line interface (CLI) tool development
* Logging and error handling
* Cryptocurrency price monitoring

---

## Features

* Retrieve real-time Bitcoin price
* Support different currencies
* CLI-based crypto price monitoring
* Logging output for API requests
* Lightweight cryptocurrency data scraper

---

## Project Structure

```text
crypto-price-scraper
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

```bash
git clone <repository-url>
cd crypto-price-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --currency USD
```

---

## Example

Run the crypto price scraper:

```bash
python src/main.py --currency USD
```

Example terminal output:

```text
2025-02-05 18:10:05 - INFO - Fetching Bitcoin price from CoinDesk API

Crypto Price:

Bitcoin Price (USD): 64,210.11
```

Another example run:

```text
2025-09-09 18:12:14 - INFO - Fetching Bitcoin price from CoinDesk API

Crypto Price:

Bitcoin Price (EUR): 58,432.27
```

---

## How It Works

1. The script sends an HTTP request to the CoinDesk API.
2. The API returns cryptocurrency price data in JSON format.
3. The script extracts the Bitcoin price for the selected currency.
4. The price is displayed in the terminal.

---

## API Used

This project uses the public API from:

**CoinDesk Bitcoin Price Index**

Endpoint:

```
https://api.coindesk.com/v1/bpi/currentprice.json
```

---

## Technologies Used

* Python
* Requests
* JSON parsing
* CLI utilities
* Logging systems

---

## Use Cases

This tool can be useful for:

* Monitoring cryptocurrency prices
* Learning API-based web scraping
* Financial data automation scripts
* Cryptocurrency analytics tools
* CLI-based data utilities

---

## Future Improvements

Possible enhancements include:

* Support multiple cryptocurrencies
* Historical crypto price analysis
* Price trend visualization
* Portfolio integration
* Scheduled price monitoring

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
