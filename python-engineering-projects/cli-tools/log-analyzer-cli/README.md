# Log Analyzer CLI Tool

A lightweight Python command-line utility that analyzes log files and counts the number of error entries.
This project demonstrates practical Python scripting for **log processing, CLI utilities, and automation workflows**.

---

## Overview

The **Log Analyzer CLI Tool** reads a log file and identifies how many error messages are present.
It is useful for quickly analyzing system logs, application logs, or server logs.

This project demonstrates:

* Log file analysis using Python
* Command-line interface (CLI) utilities
* Error detection in log files
* Logging and structured Python scripting
* Basic log monitoring automation

---

## Features

* Analyze log files from the command line
* Count occurrences of **ERROR** messages
* Logging output for analysis results
* Input file validation
* Lightweight log analysis utility

---

## Project Structure

```
log-analyzer-cli
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
cd log-analyzer-cli
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
python src/main.py --file log.txt
```

---

## Example

Example log file:

```
INFO Server started
INFO User login successful
ERROR Database connection failed
INFO Request processed
ERROR Timeout occurred
ERROR Failed to load configuration
```

Example terminal output:

```
2025-07-18 19:10:05 - INFO - Total ERROR entries: 3
```

Another example run with a different log file:

```
2025-07-18 19:18:14 - INFO - Total ERROR entries: 1
```

Example run after updating logs:

```
2025-07-18 19:24:22 - INFO - Total ERROR entries: 4
```

---

## How It Works

1. The script receives the log file path through a CLI argument.
2. It reads all lines from the log file.
3. Each line is checked for the keyword **ERROR**.
4. The total number of error entries is calculated.
5. Logging outputs the final count.

---

## Use Cases

This CLI tool can be used for:

* Monitoring application logs
* Debugging system errors
* Quick log analysis during development
* DevOps automation scripts
* Learning log processing with Python

---

## Future Improvements

Possible enhancements include:

* Support for multiple log levels (INFO, WARNING, ERROR)
* Filtering logs by date or keyword
* Generating summary reports
* Real-time log monitoring
* Exporting analysis results

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

