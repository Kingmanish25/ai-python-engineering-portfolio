# Email Automation Sender

A lightweight Python automation utility for sending emails through an SMTP server.
This project demonstrates practical Python scripting for **email automation, CLI tool development, and secure credential handling**.

---

## Overview

**Email Automation Sender** is a command-line Python tool that allows users to send emails directly from the terminal.
It connects to an SMTP server (such as Gmail) using a secure TLS connection and sends messages automatically.

This project demonstrates practical engineering concepts such as:

* SMTP-based email automation in Python
* Command-line interface (CLI) utilities
* Secure credential management using environment variables
* Logging and basic error handling
* Writing clean and modular Python scripts

---

## Features

* Send emails directly from the command line
* Secure SMTP connection using TLS encryption
* Environment variable–based credential management
* Simple CLI interface for receiver, subject, and message body
* Logging to track successful or failed email delivery

---

## Project Structure

```
email-automation-sender
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
cd email-automation-sender
```

Install dependencies (if required):

```bash
pip install -r requirements.txt
```

> This project primarily uses Python's standard library.

---

## Environment Setup

Before running the script, configure the required environment variables.

### Windows (CMD)

```
set EMAIL_SENDER=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
```

### Windows (PowerShell)

```
$env:EMAIL_SENDER="your_email@gmail.com"
$env:EMAIL_PASSWORD="your_app_password"
```

⚠️ **Important:**
For Gmail accounts, you should use a **Google App Password** instead of your normal account password.

---

## Usage

Run the script from the project root directory:

```
python src/main.py --receiver receiver@email.com --subject "Test Email" --body "Hello from Python automation"
```

---

## Example

```
python src/main.py --receiver user@email.com --subject "Test Email" --body "This is an automated email"
```

Example output:

```
2025-06-12 10:20:10 - INFO - Email sent successfully
```

---

## How It Works

1. The script reads the sender credentials from environment variables.
2. Command-line arguments provide the receiver email, subject, and message body.
3. The program establishes a secure SMTP connection using TLS.
4. The email is sent using Python's built-in `smtplib` module.
5. Logging confirms whether the email was delivered successfully.

---

## Use Cases

This automation tool can be used for:

* Automated email notifications
* System monitoring alerts
* DevOps automation scripts
* Scheduled email tasks
* Learning Python SMTP automation

---

## Future Improvements

Potential enhancements for this tool include:

* Support for multiple recipients
* HTML email formatting
* File attachment support
* Email scheduling
* Integration with job schedulers or task queues

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
