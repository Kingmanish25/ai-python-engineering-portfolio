# Moving Average Trading Strategy

A Python command-line utility that analyzes stock market data and generates trading signals using a moving average strategy.
This project demonstrates practical Python scripting for **financial analytics, quantitative trading strategies, and market data analysis**.

---

## Overview

The **Moving Average Trading Strategy** downloads historical stock market data and calculates a moving average indicator.
Based on the relationship between the latest market price and the moving average, the tool generates a simple **BUY or SELL trading signal**.

This project demonstrates:

* Financial market data retrieval
* Technical analysis using moving averages
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* Quantitative trading strategy implementation

---

## Features

* Download stock market data using **Yahoo Finance**
* Calculate moving averages
* Generate trading signals
* CLI-based financial analysis
* Logging output for market data retrieval
* Lightweight quantitative trading strategy tool

---

## Project Structure

```text
moving-average-trading-strategy
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
cd moving-average-trading-strategy
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --ticker AAPL --period 3mo --window 20
```

---

## Example

Run the trading strategy analyzer:

```bash
python src/main.py --ticker AAPL --period 3mo --window 20
```

Example terminal output:

```text
2025-02-18 18:10:05 - INFO - Downloading market data for AAPL

Market Analysis:

Ticker: AAPL
Latest Price: 188.42
20-Day Moving Average: 184.30

Signal: BUY (Price above moving average)
```

Another example run:

```text
2025-07-11 18:12:14 - INFO - Downloading market data for AAPL

Market Analysis:

Ticker: AAPL
Latest Price: 173.15
20-Day Moving Average: 176.90

Signal: SELL (Price below moving average)
```

---

## Trading Strategy Explained

### Moving Average

A **moving average (MA)** smooths price data to identify trends.

Formula:

```text
MA = Average of closing prices over N days
```

In this project:

* **20-day moving average** is used.

---

### Trading Signal Logic

```text
If Price > Moving Average → BUY signal

If Price < Moving Average → SELL signal
```

This is one of the most commonly used strategies in **technical analysis and algorithmic trading**.

---

## Data Source

Market data is retrieved from:

**Yahoo Finance API** via the `yfinance` Python library.

---

## Use Cases

This tool can be useful for:

* Learning quantitative trading strategies
* Stock market data analysis
* Financial analytics automation
* Algorithmic trading experiments
* CLI-based financial analysis tools

---

## Future Improvements

Possible enhancements include:

* Multiple moving averages
* Backtesting trading strategies
* Performance metrics calculation
* Portfolio simulation
* Financial data visualization

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

