# Stock Price Analyzer

A Python command-line utility that analyzes stock market prices using historical data from Yahoo Finance.
This project demonstrates practical Python scripting for **financial market analysis, stock price monitoring, and CLI-based financial analytics tools**.

---

## Overview

The **Stock Price Analyzer** retrieves historical stock data and calculates key price statistics such as the latest closing price, highest price, lowest price, and average price.

This project demonstrates:

* Financial market data retrieval
* Stock price analytics using Python
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* Financial data analysis workflows

---

## Features

* Download historical stock market data
* Analyze stock price trends
* Calculate price statistics
* CLI-based financial analysis
* Logging output for data retrieval
* Lightweight stock analytics tool

---

## Project Structure

```text
stock-price-analyzer
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
cd stock-price-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --ticker AAPL --period 1mo
```

---

## Example

Run the stock analyzer:

```bash
python src/main.py --ticker AAPL --period 1mo
```

Example terminal output:

```text
2025-02-10 18:10:05 - INFO - Downloading stock data for AAPL

Stock Price Analysis:

Ticker: AAPL
Latest Closing Price: 188.42
Highest Price (1mo): 195.10
Lowest Price (1mo): 180.25
Average Price (1mo): 187.31
```

Another example run:

```text
2025-09-02 18:12:14 - INFO - Downloading stock data for MSFT

Stock Price Analysis:

Ticker: MSFT
Latest Closing Price: 421.11
Highest Price (1mo): 430.50
Lowest Price (1mo): 398.22
Average Price (1mo): 412.76
```

---

## Financial Metrics Explained

### Latest Closing Price

The most recent closing price of the stock within the selected time period.

---

### Highest Price

The maximum price reached by the stock during the selected period.

---

### Lowest Price

The minimum price reached by the stock during the selected period.

---

### Average Price

The average closing price during the selected time period.

---

## Data Source

Market data is retrieved from:

**Yahoo Finance API**

via the Python library:

```text
yfinance
```

---

## Use Cases

This tool can be useful for:

* Stock market monitoring
* Financial analytics practice
* Investment research
* Market data analysis
* CLI-based financial tools

---

## Future Improvements

Possible enhancements include:

* Multi-stock comparison
* Price trend visualization
* Moving average indicators
* Portfolio integration
* Automated financial reports

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
