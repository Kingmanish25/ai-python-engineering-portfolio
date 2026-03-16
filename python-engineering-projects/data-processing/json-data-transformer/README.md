# JSON Data Transformer

A Python command-line utility that reads JSON data, applies transformations, and saves the transformed output to a new JSON file.
This project demonstrates practical Python scripting for **JSON processing, data transformation, and data pipeline utilities**.

---

## Overview

The **JSON Data Transformer** reads JSON data from an input file, performs transformations on the data, and writes the transformed data to a new JSON file.

In this implementation, the transformation converts all JSON keys to **uppercase**, demonstrating a simple data transformation workflow.

This project demonstrates:

* JSON data processing using Python
* Command-line interface (CLI) tool development
* Data transformation pipelines
* Logging and structured Python scripting
* File-based data workflows

---

## Features

* Transform JSON datasets from the command line
* Convert JSON keys to uppercase
* Save transformed data to a new JSON file
* Logging output for processing steps
* Lightweight JSON data processing utility

---

## Project Structure

```text
json-data-transformer
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
cd json-data-transformer
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
python src/main.py --input data.json --output transformed.json
```

---

## Example

Example input dataset (`data.json`):

```json
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

Run the transformer:

```bash
python src/main.py --input data.json --output transformed.json
```

Example terminal output:

```text
2025-01-20 17:10:05 - INFO - JSON file loaded successfully
2025-01-20 17:10:05 - INFO - Transformed JSON saved to: transformed.json
```

Another dataset example:

```text
2025-05-28 17:12:14 - INFO - JSON file loaded successfully
2025-05-28 17:12:14 - INFO - Transformed JSON saved to: transformed.json
```

---

## Example Output JSON (`transformed.json`)

```json
{
    "NAME": "John",
    "AGE": 30,
    "CITY": "New York"
}
```

---

## How It Works

1. The CLI tool receives input and output JSON file paths.
2. The input JSON file is loaded using Python's `json` module.
3. Keys in the JSON data are transformed to uppercase.
4. The transformed JSON is saved to a new file.
5. Logging reports the processing steps.

---

## Use Cases

This tool can be useful for:

* JSON data transformation workflows
* Data preprocessing pipelines
* API data formatting
* Data engineering utilities
* Learning JSON processing in Python

---

## Future Improvements

Possible enhancements include:

* Transform nested JSON structures
* Apply custom transformation rules
* Convert JSON to other formats
* Batch processing of multiple JSON files
* Data validation features

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

