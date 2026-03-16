# CSV Data Cleaner

A Python command-line tool that cleans CSV datasets by removing rows containing missing values.
This project demonstrates practical Python scripting for **data preprocessing, CLI utilities, and data pipeline workflows**.

---

## Overview

The **CSV Data Cleaner** is a lightweight data-processing utility that reads a CSV file, removes rows containing missing values, and saves the cleaned dataset to a new CSV file.

This project demonstrates:

* Data cleaning with Python
* CSV data processing using **Pandas**
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* File validation and dataset preprocessing

---

## Features

* Remove rows with missing values
* Process CSV datasets from the command line
* Export cleaned datasets to a new CSV file
* Logging output for dataset statistics
* Lightweight data preprocessing utility

---

## Project Structure

```text
csv-data-cleaner
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
cd csv-data-cleaner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --input data.csv --output cleaned_data.csv
```

---

## Example

Example input dataset (`data.csv`):

```text
name,age,city
Alice,25,New York
Bob,,London
Charlie,28,Toronto
David,35,
Emma,29,Berlin
```

Run the cleaner:

```bash
python src/main.py --input data.csv --output cleaned_data.csv
```

Example terminal output:

```text
2025-02-15 18:10:05 - INFO - Original rows: 5
2025-02-15 18:10:05 - INFO - Rows after cleaning: 3
2025-02-15 18:10:05 - INFO - Cleaned data saved to: cleaned_data.csv
```

Another dataset run:

```text
2025-04-15 18:12:11 - INFO - Original rows: 1200
2025-04-15 18:12:11 - INFO - Rows after cleaning: 1120
2025-04-15 18:12:11 - INFO - Cleaned data saved to: cleaned_data.csv
```

---

## How It Works

1. The CLI tool receives input and output file paths.
2. The CSV dataset is loaded using **Pandas**.
3. Rows containing missing values are removed.
4. The cleaned dataset is saved to a new CSV file.
5. Logging reports dataset statistics.

---

## Use Cases

This tool can be useful for:

* Data preprocessing pipelines
* Cleaning datasets before machine learning training
* Removing incomplete records
* Preparing datasets for analytics workflows
* Learning Python-based data processing

---

## Future Improvements

Possible enhancements include:

* Filling missing values instead of dropping rows
* Column-specific cleaning rules
* Outlier detection
* Batch dataset cleaning
* Data quality reports

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
