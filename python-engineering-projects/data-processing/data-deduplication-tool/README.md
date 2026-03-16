# Data Deduplication Tool

A Python command-line utility that removes duplicate records from CSV datasets.
This project demonstrates practical Python scripting for **data cleaning, dataset preprocessing, and data pipeline utilities**.

---

## Overview

The **Data Deduplication Tool** reads a CSV dataset, detects duplicate rows, and removes them to produce a clean dataset.
Duplicate records are common in real-world datasets, and removing them is an essential step in data preprocessing.

This project demonstrates:

* Dataset preprocessing with Python
* Data deduplication using **Pandas**
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* File-based data processing pipelines

---

## Features

* Remove duplicate rows from CSV datasets
* Command-line interface for dataset processing
* Export cleaned datasets to a new CSV file
* Logging output for dataset statistics
* Lightweight data cleaning utility

---

## Project Structure

```text
data-deduplication-tool
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
cd data-deduplication-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --input data.csv --output deduplicated_data.csv
```

---

## Example

Example input dataset (`data.csv`):

```text
id,name,city
1,Alice,New York
2,Bob,London
2,Bob,London
3,Charlie,Toronto
4,David,Berlin
4,David,Berlin
```

Run the deduplication tool:

```bash
python src/main.py --input data.csv --output deduplicated_data.csv
```

Example terminal output:

```text
2025-03-10 17:10:05 - INFO - Original rows: 6
2025-03-10 17:10:05 - INFO - Rows after deduplication: 4
2025-03-10 17:10:05 - INFO - Deduplicated dataset saved to: deduplicated_data.csv
```

Another dataset example:

```text
2025-06-10 17:12:14 - INFO - Original rows: 2500
2025-06-10 17:12:14 - INFO - Rows after deduplication: 2310
2025-06-10 17:12:14 - INFO - Deduplicated dataset saved to: deduplicated_data.csv
```

---

## How It Works

1. The CLI tool receives input and output dataset paths.
2. The CSV dataset is loaded using **Pandas**.
3. Duplicate rows are detected and removed.
4. The cleaned dataset is exported to a new CSV file.
5. Logging reports dataset statistics.

---

## Use Cases

This tool can be useful for:

* Data preprocessing workflows
* Cleaning datasets before machine learning training
* Removing duplicate records from data pipelines
* Preparing datasets for analytics
* Learning Python-based data engineering utilities

---

## Future Improvements

Possible enhancements include:

* Deduplicate based on specific columns
* Generate duplicate reports
* Support large datasets with chunk processing
* Integration with ETL pipelines
* Export summary statistics

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

