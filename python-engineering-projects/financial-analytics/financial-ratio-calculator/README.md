# Financial Ratio Calculator

A Python command-line utility that calculates important financial ratios from company financial data.
This project demonstrates practical Python scripting for **financial analysis, financial modeling, and CLI-based analytics tools**.

---

## Overview

The **Financial Ratio Calculator** computes key financial performance metrics such as **Profit Margin** and **Debt Ratio** using user-provided financial inputs.

These ratios are widely used in **financial analysis, business evaluation, and investment decision-making**.

This project demonstrates:

* Financial ratio calculations
* Command-line interface (CLI) tool development
* Financial analytics workflows
* Logging and structured Python scripting
* Basic financial modeling utilities

---

## Features

* Calculate company profit margin
* Calculate company debt ratio
* CLI-based financial calculations
* Logging output for financial computations
* Lightweight financial analytics utility

---

## Project Structure

```text
financial-ratio-calculator
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
cd financial-ratio-calculator
```

Install dependencies (if required):

```bash
pip install -r requirements.txt
```

> This project uses only Python's standard library.

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --revenue 100000 --profit 20000 --assets 50000 --liabilities 20000
```

---

## Example

Run the financial ratio calculator:

```bash
python src/main.py --revenue 100000 --profit 20000 --assets 50000 --liabilities 20000
```

Example terminal output:

```text
2025-01-22 18:10:05 - INFO - Financial ratios calculated successfully

Financial Ratios:

Profit Margin : 20.00%
Debt Ratio    : 40.00%
```

Another example run:

```text
2025-06-14 18:12:14 - INFO - Financial ratios calculated successfully

Financial Ratios:

Profit Margin : 15.50%
Debt Ratio    : 35.20%
```

---

## Financial Ratios Explained

### Profit Margin

Profit margin measures how much profit a company generates relative to its revenue.

Formula:

```
Profit Margin = Profit / Revenue
```

A higher profit margin indicates better profitability.

---

### Debt Ratio

Debt ratio measures the proportion of a company's assets that are financed by liabilities.

Formula:

```
Debt Ratio = Liabilities / Assets
```

A higher debt ratio indicates higher financial leverage.

---

## Use Cases

This tool can be useful for:

* Business financial analysis
* Financial modeling practice
* Learning financial analytics with Python
* Building financial CLI tools
* Evaluating company financial performance

---

## Future Improvements

Possible enhancements include:

* Additional financial ratios
* Financial performance dashboards
* CSV-based financial analysis
* Financial trend analysis
* Integration with financial datasets

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
