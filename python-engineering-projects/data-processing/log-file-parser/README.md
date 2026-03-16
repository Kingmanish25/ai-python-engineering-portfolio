# Log File Parser

A Python command-line utility that parses log files and extracts error entries for further analysis.
This project demonstrates practical Python scripting for **log processing, data extraction, and system monitoring workflows**.

---

## Overview

The **Log File Parser** reads server log files and extracts lines containing error messages.
Filtered logs are saved to a new output file, allowing developers or system administrators to quickly analyze issues.

This project demonstrates:

* Log file parsing with Python
* Command-line interface (CLI) tool development
* Error detection in log data
* Logging and structured Python scripting
* File-based data processing

---

## Features

* Extract error entries from log files
* Command-line interface for log parsing
* Save filtered logs to a new file
* Logging output for parsing statistics
* Lightweight log analysis utility

---

## Project Structure

```text
log-file-parser
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
cd log-file-parser
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
python src/main.py --input server.log --output error_logs.txt
```

---

## Example

Example input log file (`server.log`):

```text
INFO Server started
INFO User login successful
ERROR Database connection failed
INFO Request processed
ERROR Timeout occurred
WARNING Disk space low
ERROR Failed to load configuration
```

Run the parser:

```bash
python src/main.py --input server.log --output error_logs.txt
```

Example terminal output:

```text
2025-02-11 17:10:05 - INFO - Total ERROR entries found: 3
2025-02-11 17:10:05 - INFO - Filtered log saved to: error_logs.txt
```

Another example run:

```text
2025-08-19 17:12:14 - INFO - Total ERROR entries found: 15
2025-08-19 17:12:14 - INFO - Filtered log saved to: error_logs.txt
```

---

## Example Output File (`error_logs.txt`)

```text
ERROR Database connection failed
ERROR Timeout occurred
ERROR Failed to load configuration
```

---

## How It Works

1. The CLI tool receives the input log file and output file path.
2. The log file is opened and processed line-by-line.
3. Lines containing the keyword **ERROR** are detected.
4. Matching lines are written to the output file.
5. Logging reports the number of detected error entries.

---

## Use Cases

This tool can be useful for:

* Server log monitoring
* Debugging application errors
* DevOps log analysis
* Extracting critical error messages
* Learning log processing techniques in Python

---

## Future Improvements

Possible enhancements include:

* Filtering multiple log levels (ERROR, WARNING, INFO)
* Date-based log filtering
* Generating log analysis reports
* Real-time log monitoring
* Support for large log datasets

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

