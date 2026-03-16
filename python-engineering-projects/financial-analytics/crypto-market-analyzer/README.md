# Crypto Market Analyzer

A Python command-line utility that retrieves cryptocurrency market prices using the CoinGecko API.
This project demonstrates practical Python scripting for **financial data analysis, API integration, and cryptocurrency market monitoring**.

---

## Overview

The **Crypto Market Analyzer** fetches real-time cryptocurrency prices using the **CoinGecko public API**.
It allows users to analyze crypto prices directly from the command line.

This project demonstrates:

* Financial data retrieval using APIs
* Cryptocurrency market analysis
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* API-based data workflows

---

## Features

* Retrieve cryptocurrency prices
* Support multiple crypto assets
* CLI-based financial data analysis
* Logging output for API requests
* Lightweight crypto market monitoring utility

---

## Project Structure

```text
crypto-market-analyzer
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
cd crypto-market-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --coins bitcoin,ethereum --currency usd
```

---

## Example

Run the crypto market analyzer:

```bash
python src/main.py --coins bitcoin,ethereum --currency usd
```

Example terminal output:

```text
2025-02-08 18:10:05 - INFO - Crypto market data retrieved successfully

Crypto Market Prices:

Bitcoin : 42150 USD
Ethereum : 2280 USD
```

Another example run:

```text
2025-07-17 18:12:14 - INFO - Crypto market data retrieved successfully

Crypto Market Prices:

Bitcoin : 64230 USD
Ethereum : 3180 USD
```

---

## How It Works

1. The CLI tool receives cryptocurrency IDs and a target currency.
2. A request is sent to the **CoinGecko API**.
3. The API returns the current market prices.
4. Prices are displayed in a readable format.
5. Logging reports the API request status.

---

## API Used

This project uses the public API from:

**CoinGecko API**

Endpoint used:

```
https://api.coingecko.com/api/v3/simple/price
```

Example request parameters:

* `ids` → cryptocurrency IDs
* `vs_currencies` → target currency

---

## Use Cases

This tool can be useful for:

* Monitoring cryptocurrency prices
* Learning financial data API integration
* CLI-based financial analytics tools
* Crypto market data exploration
* Building financial automation scripts

---

## Future Improvements

Possible enhancements include:

* Historical crypto price analysis
* Price change tracking
* Portfolio tracking tools
* Data visualization dashboards
* Support for more financial APIs

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
