# Blog Content Scraper

A Python command-line utility that scrapes blog post titles from a website.
This project demonstrates practical Python scripting for **web scraping, HTML parsing, and automated content extraction**.

---

## Overview

The **Blog Content Scraper** retrieves blog post titles from a website and displays them in the terminal.

The tool uses **HTTP requests and HTML parsing** to extract structured information from web pages.

This project demonstrates:

* Web scraping using Python
* HTML parsing with BeautifulSoup
* Command-line interface (CLI) tool development
* Logging and error handling
* Automated content extraction workflows

---

## Features

* Fetch webpage content
* Parse HTML structure
* Extract blog post titles
* CLI-based scraping tool
* Logging output for scraping process
* Lightweight web scraping utility

---

## Project Structure

```text
blog-content-scraper
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
cd blog-content-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --url https://blog.python.org/
```

---

## Example

Run the scraper:

```bash
python src/main.py --url https://blog.python.org/
```

Example terminal output:

```text
2025-01-12 18:10:05 - INFO - Fetching blog content from https://blog.python.org/

Latest Blog Posts:

1. Python 3.13 Release Announcement
2. Python Language Summit 2025
3. Python Security Updates
4. Python Packaging Improvements
```

Another example run:

```text
2025-08-05 18:12:14 - INFO - Fetching blog content from https://blog.python.org/

Latest Blog Posts:

1. Python Community Highlights
2. Python Documentation Updates
3. Python Developer Survey Results
4. Python Ecosystem Improvements
```

---

## How It Works

1. The script sends an HTTP request to the target blog URL.
2. The HTML content of the page is retrieved.
3. BeautifulSoup parses the HTML structure.
4. Blog post titles are extracted using CSS selectors.
5. The extracted titles are displayed in the terminal.

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* HTML Parsing
* CLI utilities
* Logging systems

---

## Use Cases

This tool can be useful for:

* Extracting blog content
* Learning web scraping techniques
* Automating content monitoring
* Data collection from websites
* Building web data pipelines

---

## Future Improvements

Possible enhancements include:

* Scraping blog post links
* Exporting results to CSV or JSON
* Scraping multiple pages
* Scheduled scraping jobs
* Integrating with data analysis pipelines

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
