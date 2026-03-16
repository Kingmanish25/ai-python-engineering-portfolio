# Password Generator CLI Tool

A lightweight Python command-line utility that generates secure random passwords.
This project demonstrates practical Python scripting for **security utilities, CLI tools, and automation workflows**.

---

## Overview

The **Password Generator CLI Tool** allows users to generate strong random passwords directly from the command line.
The tool uses Python's built-in libraries to create passwords composed of letters, digits, and special characters.

This project demonstrates:

* Secure password generation using Python
* Command-line interface (CLI) utilities
* Randomized string generation
* Logging and structured Python scripting
* Input validation for CLI tools

---

## Features

* Generate secure random passwords
* Configurable password length
* Includes letters, digits, and special characters
* CLI-based password generation
* Logging output for generated passwords
* Input validation for minimum password length

---

## Project Structure

```text
password-generator-cli
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
cd password-generator-cli
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
python src/main.py --length 16
```

---

## Example

Generate a password with length 12:

```bash
python src/main.py --length 12
```

Example output:

```text
2025-07-27 20:10:05 - INFO - Generated password: 9&dK!3a@FzP1
```

Generate a longer password:

```bash
python src/main.py --length 16
```

Example output:

```text
2025-07-27 20:12:14 - INFO - Generated password: P@7k!9Qx#2LmT1
```

Generate another password:

```bash
python src/main.py --length 20
```

Example output:

```text
2025-07-27 20:14:22 - INFO - Generated password: 4$Lp@Z9!mQ7&hK2T#sX
```

---

## How It Works

1. The script receives the desired password length via a CLI argument.
2. A character pool is created using letters, digits, and special characters.
3. Random characters are selected from the pool.
4. A secure password string is generated.
5. Logging displays the generated password.

---

## Use Cases

This CLI tool can be useful for:

* Generating strong passwords
* Security testing and development
* Creating credentials for applications
* Learning Python randomization techniques
* Practicing CLI tool development

---

## Future Improvements

Possible enhancements include:

* Option to exclude special characters
* Password strength scoring
* Saving generated passwords securely
* Generating multiple passwords at once
* Integration with password managers

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
