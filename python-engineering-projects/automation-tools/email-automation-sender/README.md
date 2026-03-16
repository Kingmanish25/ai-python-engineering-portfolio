# Email Automation Sender

A lightweight Python automation tool that sends emails using the SMTP protocol.
This project demonstrates practical Python scripting for email automation and command-line utilities.

---

## Overview

The Email Automation Sender allows users to send emails directly from the command line using Python.
It connects to an SMTP server (such as Gmail) and sends messages securely using TLS encryption.

This project demonstrates:

* Python SMTP email automation
* Command-line interface (CLI) utilities
* Secure credential management using environment variables
* Logging and error handling

---

## Features

* Send emails directly from the command line
* Secure SMTP connection using TLS
* Uses environment variables for email credentials
* Simple CLI interface for specifying receiver, subject, and message
* Logging for successful or failed email delivery

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

---

## Setup Environment Variables

Before running the script, set the following environment variables.

### Windows (CMD)

```bash
set EMAIL_SENDER=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
```

### Windows (PowerShell)

```bash
$env:EMAIL_SENDER="your_email@gmail.com"
$env:EMAIL_PASSWORD="your_app_password"
```

---

## Usage

Run the script using the command line.

```bash
python src/main.py --receiver receiver@email.com --subject "Test Email" --body "Hello from Python automation"
```

---

## Example

```bash
python src/main.py --receiver user@email.com --subject "Test Email" --body "This is an automated email"
```

Example output:

```
2025-06-12 10:20:10 - INFO - Email sent successfully
```

---

## How It Works

1. The script reads the sender email and password from environment variables.
2. It accepts receiver, subject, and body as command-line arguments.
3. It establishes a secure SMTP connection using TLS.
4. The email is sent using Python’s `smtplib` module.
5. Logging reports whether the email was sent successfully.

---

## Use Cases

This tool can be used for:

* Email automation scripts
* Notification systems
* Monitoring alerts
* DevOps automation utilities
* Learning SMTP email automation in Python

---

## Future Improvements

Possible enhancements:

* Support multiple recipients
* Add HTML email support
* Attach files to emails
* Email scheduling functionality
* Integration with task schedulers

---

## Author
Manish Rathi
AI & Python Engineering Portfolio
