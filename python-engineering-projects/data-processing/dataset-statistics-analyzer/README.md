# Dataset Statistics Analyzer

A Python command-line utility that analyzes CSV datasets and generates descriptive statistics.
This project demonstrates practical Python scripting for **data exploration, dataset analysis, and data pipeline utilities**.

---

## Overview

The **Dataset Statistics Analyzer** reads a CSV dataset and generates summary statistics such as mean, standard deviation, minimum, maximum, and percentiles for numeric columns.

Dataset statistics are essential for understanding the distribution of data before performing further analysis or machine learning.

This project demonstrates:

* Dataset analysis using **Pandas**
* Command-line interface (CLI) tool development
* Data exploration workflows
* Logging and structured Python scripting
* File-based data processing

---

## Features

* Analyze numeric columns in CSV datasets
* Generate descriptive statistics automatically
* Save dataset statistics to a CSV file
* Logging output for dataset details
* Lightweight data exploration utility

---

## Project Structure

```
dataset-statistics-analyzer
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
cd dataset-statistics-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --input data.csv --output statistics.csv
```

---

## Example

Example input dataset (`data.csv`):

```
age,salary,experience
25,50000,2
30,65000,5
28,58000,3
40,82000,10
35,72000,7
```

Run the analyzer:

```bash
python src/main.py --input data.csv --output statistics.csv
```

Example terminal output:

```
2025-02-18 17:10:05 - INFO - Dataset loaded successfully
2025-02-18 17:10:05 - INFO - Rows: 5, Columns: 3
2025-02-18 17:10:05 - INFO - Dataset statistics saved to: statistics.csv
```

Another dataset example:

```
2025-07-09 17:12:14 - INFO - Dataset loaded successfully
2025-07-09 17:12:14 - INFO - Rows: 1200, Columns: 8
2025-07-09 17:12:14 - INFO - Dataset statistics saved to: statistics.csv
```

---

## Example Output File (`statistics.csv`)

```
,count,mean,std,min,25%,50%,75%,max
age,5,31.6,5.5,25,28,30,35,40
salary,5,65400,12000,50000,58000,65000,72000,82000
experience,5,5.4,3.0,2,3,5,7,10
```

---

## How It Works

1. The CLI tool receives input and output dataset paths.
2. The CSV dataset is loaded using **Pandas**.
3. Descriptive statistics are calculated for numeric columns.
4. The statistics report is saved to a CSV file.
5. Logging displays dataset information.

---

## Use Cases

This tool can be useful for:

* Exploratory data analysis
* Understanding dataset distributions
* Preparing datasets for machine learning
* Data pipeline validation
* Quick dataset inspection

---

## Future Improvements

Possible enhancements include:

* Visualizing dataset distributions
* Generating HTML reports
* Detecting outliers
* Handling large datasets with chunk processing
* Supporting Excel datasets

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

