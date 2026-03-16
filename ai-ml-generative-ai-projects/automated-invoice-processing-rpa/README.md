# Automated Invoice Processing (RPA + AI)

This project implements an **automated invoice processing system** using Python.
It demonstrates how Robotic Process Automation (RPA) and AI-based document extraction can be used to process financial documents automatically.

The system extracts structured data from invoice PDFs, validates the extracted information, stores it in a database, and generates processing analytics.

The project simulates a real-world **intelligent document processing pipeline used in enterprise finance systems**.

---

# Project Overview

Manual invoice processing is slow, expensive, and error-prone.

This project demonstrates how automation can be used to:

* Read invoice PDF documents
* Extract structured invoice data
* Validate extracted information
* Store invoice records in a database
* Generate processing analytics

The system is designed as a **modular automation pipeline**, similar to enterprise invoice automation solutions.

---

# System Architecture

The automation pipeline follows a structured workflow.

```
Invoice PDF
     ↓
PDF Text Extraction
     ↓
AI Invoice Data Extraction
     ↓
Data Validation
     ↓
Database Storage
     ↓
Visualization / Analytics
```

Each step is implemented as an independent module.

---

# Project Structure

```
automated-invoice-processing-rpa
│
├── data
│   └── invoices
│       ├── invoice_INV_001.pdf
│       ├── invoice_INV_002.pdf
│       └── invoice_INV_003.pdf
│
├── screenshots
│   └── img.png
│
├── src
│   ├── automation_workflow.py
│   ├── invoice_reader.py
│   ├── pdf_parser.py
│   ├── ai_extractor.py
│   ├── validation_engine.py
│   └── database_writer.py
│
├── requirements.txt
└── README.md
```

---

# Module Description

## automation_workflow.py

Main pipeline controller.

Responsibilities:

* Executes the invoice processing workflow
* Orchestrates the automation pipeline
* Generates processing visualization

---

## invoice_reader.py

Responsible for locating and loading invoice files.

Capabilities:

* Detect invoice PDFs in the data directory
* Prepare files for parsing

---

## pdf_parser.py

Extracts raw text content from PDF invoices.

Capabilities:

* PDF text extraction
* Document preprocessing

---

## ai_extractor.py

Extracts structured invoice fields using AI-style parsing.

Extracted fields include:

* Invoice Number
* Supplier
* Invoice Date
* Buyer
* Total Amount
* Tax

---

## validation_engine.py

Validates extracted invoice information.

Validation checks include:

* Required fields present
* Valid invoice number
* Valid invoice amount

---

## database_writer.py

Stores validated invoice data into a local database.

Capabilities:

* Create database tables
* Insert invoice records
* Maintain invoice history

---

# Example Invoice Data Extracted

Example extracted fields:

```
Invoice Number: INV-001
Supplier: Carmen Nixon
Invoice Date: 10-09-1982
Buyer: Todd Anderson
Total Amount: 157.36
Tax: 26.23
```

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd automated-invoice-processing-rpa
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

Run the automation pipeline:

```
python src/automation_workflow.py
```

The pipeline will:

1. Load invoice PDF files
2. Extract invoice data
3. Validate extracted information
4. Store invoices in a database
5. Generate processing visualization

---

# Output

Processed invoices are stored in:

```
invoices.db
```

Visualization output is generated automatically:

```
screenshots/img.png
```

The visualization shows invoice amounts processed during the automation workflow.

---

# Technologies Used

* Python
* PDF parsing
* OCR
* Data validation
* SQLite database
* Automation pipelines

---

# Applications

This project demonstrates techniques used in:

* Robotic Process Automation (RPA)
* Intelligent document processing
* Financial document extraction
* Enterprise accounting automation
* AI-powered document workflows

---

# Future Improvements

Possible enhancements include:

* LLM-based invoice extraction
* Named Entity Recognition for invoices
* Integration with ERP systems
* Web dashboard for invoice monitoring
* Multi-format invoice processing

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

