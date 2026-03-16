# Large File Processor

A Python command-line utility designed to efficiently process large text files without loading the entire file into memory.
This project demonstrates practical Python scripting for **large dataset processing, streaming data workflows, and memory-efficient file handling**.

---

## Overview

The **Large File Processor** reads large files line-by-line and processes data at configurable intervals.
Instead of loading the entire file into memory, it uses a streaming approach, making it suitable for processing large log files or datasets.

This project demonstrates:

* Memory-efficient file processing
* Streaming data processing techniques
* Command-line interface (CLI) tool development
* Logging and structured Python scripting
* Handling large datasets in Python

---

## Features

* Process large files efficiently
* Stream file data line-by-line
* Configurable processing interval
* CLI-based file processing
* Logging output for processing steps
* Lightweight large file processing utility

---

## Project Structure

```text
large-file-processor
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
cd large-file-processor
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
python src/main.py --input bigfile.txt --interval 1000
```

---

## Example

Example input file (`bigfile.txt`):

```text
record_1
record_2
record_3
record_4
record_5
...
record_1000
record_1001
record_1002
```

Run the processor:

```bash
python src/main.py --input bigfile.txt --interval 1000
```

Example terminal output:

```text
2025-02-02 17:10:05 - INFO - Starting large file processing
2025-02-02 17:10:05 - INFO - Processing line 1000: record_1000
2025-02-02 17:10:05 - INFO - Processing line 2000: record_2000
```

Another example run:

```text
2025-07-14 17:12:14 - INFO - Starting large file processing
2025-07-14 17:12:14 - INFO - Processing line 1000: record_1000
2025-07-14 17:12:14 - INFO - Processing line 2000: record_2000
2025-07-14 17:12:14 - INFO - Processing line 3000: record_3000
```

---

## How It Works

1. The CLI tool receives the input file and processing interval.
2. The file is opened in streaming mode.
3. Lines are read one by one using an iterator.
4. Every *N* lines (based on interval), the processor logs progress.
5. Logging provides insight into processing progress.

---

## Use Cases

This tool can be useful for:

* Processing large log files
* Streaming data pipelines
* Memory-efficient dataset processing
* Monitoring file processing progress
* Learning large-file handling techniques

---

## Future Improvements

Possible enhancements include:

* Parallel file processing
* Progress percentage tracking
* Output file generation
* Support for CSV and JSON large files
* Real-time log monitoring

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

