# Portfolio Performance Tracker

A Python command-line utility that analyzes stock portfolio performance and calculates investment returns.
This project demonstrates practical Python scripting for **portfolio analytics, financial data analysis, and investment performance tracking**.

---

## Overview

The **Portfolio Performance Tracker** analyzes a stock portfolio using investment and current market values.
It calculates profit and return percentages for each asset and summarizes the overall portfolio performance.

This project demonstrates:

* Portfolio performance analysis
* Financial analytics using **Pandas**
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* Investment return calculations

---

## Features

* Analyze portfolio investment performance
* Calculate profit for each asset
* Compute return percentage for each investment
* Display portfolio summary statistics
* CLI-based financial analytics tool

---

## Project Structure

```text id="tdz1k0"
portfolio-performance-tracker
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

```bash id="a41nx7"
git clone <repository-url>
cd portfolio-performance-tracker
```

Install dependencies:

```bash id="xnvbby"
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash id="3dz5ph"
python src/main.py --input portfolio.csv
```

---

## Example

Example portfolio dataset (`portfolio.csv`):

```text id="ts2mue"
Stock,Investment,Current_Value
AAPL,1000,1200
MSFT,1500,1700
GOOG,1200,1400
```

Run the portfolio analyzer:

```bash id="q31kth"
python src/main.py --input portfolio.csv
```

Example terminal output:

```text id="v96w1q"
2025-02-14 18:10:05 - INFO - Portfolio data loaded successfully

Portfolio Performance:

Stock  Investment  Current_Value  Profit  Return_%
AAPL      1000         1200        200      20.00
MSFT      1500         1700        200      13.33
GOOG      1200         1400        200      16.67

Portfolio Summary:

Total Investment : 3700.00
Current Value    : 4300.00
Total Profit     : 600.00
```

Another example run:

```text id="cllsqk"
2025-08-21 18:12:14 - INFO - Portfolio data loaded successfully

Portfolio Performance:

Stock  Investment  Current_Value  Profit  Return_%
TSLA      2000         2500        500      25.00
NVDA      1800         2100        300      16.67
AMZN      1500         1650        150      10.00

Portfolio Summary:

Total Investment : 5300.00
Current Value    : 6250.00
Total Profit     : 950.00
```

---

## Financial Metrics Explained

### Profit

Profit represents the difference between current asset value and initial investment.

Formula:

```text id="y1g8ul"
Profit = Current Value - Investment
```

---

### Return Percentage

Return percentage shows the performance of an investment relative to its initial cost.

Formula:

```text id="85hxbi"
Return % = (Profit / Investment) × 100
```

---

## Use Cases

This tool can be useful for:

* Tracking portfolio performance
* Evaluating investment returns
* Financial analytics learning projects
* Investment portfolio analysis
* CLI-based financial tools

---

## Future Improvements

Possible enhancements include:

* Real-time stock price integration
* Portfolio diversification analysis
* Risk metrics calculation
* Portfolio visualization dashboards
* Automated portfolio reports

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

