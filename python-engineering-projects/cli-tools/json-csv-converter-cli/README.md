# JSON to CSV Converter CLI

A lightweight Python command-line tool that converts JSON files into CSV format.
This project demonstrates practical Python scripting for **data format conversion, CLI utilities, and file processing automation**.

---

## Overview

The **JSON to CSV Converter CLI** reads structured JSON data and converts it into a CSV file.
This tool is useful when working with datasets that need to be processed or analyzed in spreadsheet or tabular formats.

This project demonstrates:

* Data transformation using Python
* Command-line interface (CLI) utilities
* JSON parsing and CSV generation
* Logging and structured Python scripting
* File validation and error handling

---

## Features

* Convert JSON files into CSV format
* Command-line interface for input and output files
* Automatic CSV header generation from JSON keys
* Logging output for conversion status
* Input file validation

---

## Project Structure

```text
json-csv-converter-cli
│
├── README.md
├── requirements.txt
│
├── data.json
│
└── src
    └── main.py
```

---

## Installation

Clone the repository and navigate to the project directory.

```bash
git clone <repository-url>
cd json-csv-converter-cli
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
python src/main.py --input data.json --output output.csv
```

---

## Example

Example JSON input:

```json
[
  {"name": "Alice", "age": 25, "city": "New York"},
  {"name": "Bob", "age": 30, "city": "London"},
  {"name": "Charlie", "age": 28, "city": "Toronto"}
]
```

Generated CSV output:

```text
name,age,city
Alice,25,New York
Bob,30,London
Charlie,28,Toronto
```

Example terminal output:

```text
2025-07-16 18:30:10 - INFO - Conversion completed: data.json → output.csv
```

---

## How It Works

1. The script receives input and output file paths via CLI arguments.
2. The JSON file is loaded and validated.
3. The keys of the JSON objects are used as CSV column headers.
4. The data is written to a CSV file using Python's `csv` module.
5. Logging confirms the successful conversion.

---

## Use Cases

This CLI tool can be used for:

* Data preprocessing workflows
* Converting API responses to CSV
* Preparing datasets for analysis
* Automation scripts for data transformation
* Learning file processing with Python

---

## Future Improvements

Possible enhancements include:

* CSV to JSON conversion
* Nested JSON flattening
* Support for large JSON files
* Batch file conversion
* Data validation options

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

