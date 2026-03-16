# URL Status Checker CLI Tool

A lightweight Python command-line utility that checks the HTTP status code of a given URL.
This project demonstrates practical Python scripting for **web automation, CLI tools, and network request handling**.

---

## Overview

The **URL Status Checker CLI Tool** allows users to quickly verify whether a website or API endpoint is reachable by checking its HTTP response status code.

This project demonstrates:

* Command-line interface (CLI) tool development
* HTTP request handling using Python
* Basic network diagnostics
* Logging and structured Python scripting
* Error handling for network requests

---

## Features

* Check HTTP status codes for any URL
* CLI-based URL input
* Timeout protection for network requests
* Logging output for request results
* Error handling for unreachable URLs

---

## Project Structure

```
url-status-checker-cli
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
cd url-status-checker-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --url https://example.com
```

---

## Example

Check the status of a website:

```bash
python src/main.py --url https://example.com
```

Example terminal output:

```
2025-10-28 20:10:05 - INFO - URL checked: https://example.com
2025-10-28 20:10:05 - INFO - Status code: 200
```

---

## How It Works

1. The CLI tool receives a URL as a command-line argument.
2. A GET request is sent using the `requests` library.
3. The HTTP response status code is captured.
4. Logging displays the result in the terminal.

---

## Use Cases

This CLI tool can be useful for:

* Checking website availability
* Monitoring API endpoints
* Quick network diagnostics
* DevOps automation scripts
* Learning HTTP request handling with Python

---

## Future Improvements

Possible enhancements include:

* Checking multiple URLs at once
* Exporting results to CSV or JSON
* Measuring response time
* Scheduled URL monitoring
* Status alerts for failed requests

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

