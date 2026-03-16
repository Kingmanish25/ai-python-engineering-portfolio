# Job Listing Scraper

A Python command-line utility that scrapes job listings from a webpage and extracts job titles, companies, and locations.
This project demonstrates practical Python scripting for **web scraping, job market data extraction, and automated data collection**.

---

## Overview

The **Job Listing Scraper** retrieves job postings from a job listing website and extracts structured information including job title, company name, and location.

This project demonstrates:

* Web scraping using Python
* HTML parsing with BeautifulSoup
* Command-line interface (CLI) tool development
* Logging and error handling
* Structured data extraction

---

## Features

* Extract job titles
* Extract company names
* Extract job locations
* CLI-based web scraping tool
* Logging output for scraping operations
* Lightweight job listing data scraper

---

## Project Structure

```text id="8stt37"
job-listing-scraper
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

```bash id="a2kq0m"
git clone <repository-url>
cd job-listing-scraper
```

Install dependencies:

```bash id="5exvmt"
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash id="x1vceq"
python src/main.py --limit 10
```

---

## Example

Run the job listing scraper:

```bash id="dz5jj9"
python src/main.py --limit 10
```

Example terminal output:

```text id="3pgcr9"
2025-02-03 18:10:05 - INFO - Fetching job listings from https://realpython.github.io/fake-jobs/

Job Listings:

1. Python Developer
   Company : Example Corp
   Location: Remote

2. Data Scientist
   Company : DataWorks
   Location: New York

3. Backend Engineer
   Company : Tech Solutions
   Location: San Francisco
```

Another example run:

```text id="ntwn30"
2025-08-18 18:12:14 - INFO - Fetching job listings from https://realpython.github.io/fake-jobs/

Job Listings:

1. Machine Learning Engineer
   Company : AI Systems
   Location: London

2. Software Engineer
   Company : DevWorks
   Location: Berlin

3. Data Analyst
   Company : Insight Labs
   Location: Toronto
```

---

## How It Works

1. The script sends an HTTP request to the job listing website.
2. The HTML content of the page is retrieved.
3. BeautifulSoup parses the HTML structure.
4. Job details such as title, company, and location are extracted.
5. The extracted information is displayed in the terminal.

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

* Collecting job market data
* Learning web scraping techniques
* Building recruitment analytics tools
* Monitoring job postings
* Data collection for job market analysis

---

## Future Improvements

Possible enhancements include:

* Export job listings to CSV or JSON
* Scrape multiple pages
* Add keyword-based job filtering
* Build job trend analysis tools
* Integrate with job search automation systems

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
