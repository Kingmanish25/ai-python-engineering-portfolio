# Wikipedia Data Extractor

A Python command-line utility that extracts text content from Wikipedia articles.
This project demonstrates practical Python scripting for **web scraping, knowledge extraction, and automated content retrieval from web pages**.

---

## Overview

The **Wikipedia Data Extractor** retrieves content from a Wikipedia page and extracts the first few paragraphs of the article.

This project demonstrates:

* Web scraping using Python
* HTML parsing with BeautifulSoup
* Command-line interface (CLI) tool development
* Logging and error handling
* Automated information extraction from web pages

---

## Features

* Extract text from Wikipedia articles
* Retrieve article content automatically
* CLI-based web scraping tool
* Logging output for scraping operations
* Lightweight knowledge extraction utility

---

## Project Structure

```text
wikipedia-data-extractor
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
cd wikipedia-data-extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --limit 5
```

---

## Example

Run the Wikipedia data extractor:

```bash
python src/main.py --limit 5
```

Example terminal output:

```text
2025-02-20 18:10:05 - INFO - Fetching Wikipedia page: https://en.wikipedia.org/wiki/Web_scraping

Wikipedia Extracted Content:

1. Web scraping is data scraping used for extracting data from websites.

2. The software may directly access the World Wide Web using the HTTP protocol...

3. Web scraping can be done manually by a user or automatically by software...

4. Web scraping is used in many industries for data collection and research.

5. Automated scraping tools are widely used for building datasets.
```

Another example run:

```text
2025-09-06 18:12:14 - INFO - Fetching Wikipedia page: https://en.wikipedia.org/wiki/Python_(programming_language)

Wikipedia Extracted Content:

1. Python is a high-level, general-purpose programming language.

2. Python's design philosophy emphasizes code readability.

3. Python supports multiple programming paradigms including procedural, object-oriented and functional programming.

4. Python is widely used in data science, artificial intelligence, and automation.

5. The Python Software Foundation manages the development of Python.
```

---

## How It Works

1. The script sends an HTTP request to the specified Wikipedia page.
2. The HTML content of the page is retrieved.
3. BeautifulSoup parses the HTML structure.
4. Paragraph elements are extracted from the article.
5. The selected paragraphs are displayed in the terminal.

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* HTML parsing
* CLI utilities
* Logging systems

---

## Use Cases

This tool can be useful for:

* Extracting information from Wikipedia articles
* Learning web scraping techniques
* Content extraction automation
* Data collection for research
* Building knowledge datasets

---

## Future Improvements

Possible enhancements include:

* Extract article headings
* Export extracted text to files
* Scrape multiple Wikipedia pages
* Create structured datasets from Wikipedia
* Integrate with NLP pipelines

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
