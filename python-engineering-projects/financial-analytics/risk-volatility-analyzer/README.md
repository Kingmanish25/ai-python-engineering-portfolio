# Risk Volatility Analyzer

A Python command-line utility that measures financial risk by calculating the volatility of stock returns.
This project demonstrates practical Python scripting for **financial risk analysis, quantitative finance concepts, and market data analytics**.

---

## Overview

The **Risk Volatility Analyzer** downloads historical stock market data and calculates the volatility of returns.
Volatility is one of the most widely used risk metrics in finance and is commonly used in **portfolio management, quantitative trading, and risk modeling**.

This project demonstrates:

* Financial risk analysis using Python
* Market data retrieval using Yahoo Finance
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* Quantitative finance calculations

---

## Features

* Download historical stock data
* Calculate daily returns
* Measure daily volatility
* Compute annualized volatility
* Provide risk classification
* CLI-based financial risk analysis

---

## Project Structure

```text id="rma0eb"
risk-volatility-analyzer
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

```bash id="0pr71t"
git clone <repository-url>
cd risk-volatility-analyzer
```

Install dependencies:

```bash id="oel1ea"
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash id="1yhu2f"
python src/main.py --ticker AAPL --period 3mo
```

---

## Example

Run the volatility analyzer:

```bash id="2v6fsq"
python src/main.py --ticker AAPL --period 3mo
```

Example terminal output:

```text id="0y5r6c"
2025-03-06 18:10:05 - INFO - Downloading market data for AAPL

Risk & Volatility Analysis:

Ticker: AAPL
Daily Volatility: 0.0152
Annualized Volatility: 0.2410

Risk Level: MEDIUM
```

Another example run:

```text id="hsm9hy"
2025-09-12 18:12:14 - INFO - Downloading market data for AAPL

Risk & Volatility Analysis:

Ticker: AAPL
Daily Volatility: 0.0285
Annualized Volatility: 0.4520

Risk Level: HIGH
```

---

## Financial Concepts Explained

### Daily Returns

Daily return represents the percentage change in stock price from one day to the next.

Formula:

```text id="vkvpld"
Return = (Price_today - Price_yesterday) / Price_yesterday
```

In the script this is calculated using:

```python id="s3v5zu"
data["Close"].pct_change()
```

---

### Volatility

Volatility measures the variability of asset returns.

Formula:

```text id="5g4p3a"
Volatility = Standard deviation of returns
```

Higher volatility indicates **higher financial risk**.

---

### Annualized Volatility

Annualized volatility converts daily volatility into yearly volatility.

Formula:

```text id="p9xyk0"
Annualized Volatility = Daily Volatility × √252
```

Where **252** represents the number of trading days in a year.

---

## Risk Classification

This tool categorizes risk levels based on annualized volatility:

| Volatility | Risk Level  |
| ---------- | ----------- |
| < 20%      | Low Risk    |
| 20% – 40%  | Medium Risk |
| > 40%      | High Risk   |

---

## Use Cases

This tool can be useful for:

* Financial risk analysis
* Quantitative finance projects
* Portfolio risk evaluation
* Market volatility analysis
* Learning financial analytics with Python

---

## Future Improvements

Possible enhancements include:

* Portfolio volatility analysis
* Multiple asset risk comparison
* Risk-adjusted return metrics
* Financial data visualization
* Monte Carlo risk simulations

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

