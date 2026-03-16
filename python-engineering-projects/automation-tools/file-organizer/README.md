# File Organizer Automation Tool

A lightweight Python automation utility that organizes files into folders based on their file extensions.
This project demonstrates practical Python scripting for **file system automation and command-line tools**.

---

## Overview

The **File Organizer** automatically sorts files within a directory by grouping them into folders according to their file type (extension).

For example, all `.pdf` files will be moved into a `pdf/` folder, `.jpg` files into a `jpg/` folder, and so on.
This helps keep directories such as **Downloads** clean and well organized.

This project demonstrates:

* Python file system automation
* Command-line interface (CLI) utilities
* File extension classification
* Logging and structured Python scripting

---

## Features

* Automatically organizes files by extension
* Creates folders dynamically if they do not exist
* Handles files without extensions
* Command-line interface for specifying the target folder
* Logging for tracking file movements

---

## Project Structure

```id="7s6c0r"
file-organizer
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

```bash id="jqxj49"
git clone <repository-url>
cd file-organizer
```

Install dependencies (if required):

```bash id="oqjo3e"
pip install -r requirements.txt
```

> This project uses only Python’s standard library.

---

## Usage

Run the script from the project root directory.

```bash id="luzm9o"
python src/main.py --folder downloads
```

---

## Example

### Before running the script

```id="kmpbdp"
downloads
│
├── file1.pdf
├── image.jpg
├── notes.txt
```

### After running the script

```id="nt0u7v"
downloads
│
├── pdf
│   └── file1.pdf
│
├── jpg
│   └── image.jpg
│
└── txt
    └── notes.txt
```

Example terminal output:

```id="qwh8ju"
2025-01-06 08:42:12 - INFO - Moved file1.pdf → pdf/
2025-01-06 08:42:12 - INFO - Moved image.jpg → jpg/
2025-01-06 08:42:12 - INFO - Moved notes.txt → txt/
```

---

## How It Works

1. The script receives the folder path through a command-line argument.
2. It scans all files within the directory.
3. Each file’s extension is identified.
4. A corresponding folder is created (if it does not already exist).
5. The file is moved into the appropriate folder.

---

## Use Cases

This automation tool can be useful for:

* Organizing a cluttered **Downloads folder**
* Sorting files by type automatically
* Learning Python file system automation
* Practicing CLI tool development

---

## Future Improvements

Possible enhancements include:

* File size filtering
* Custom extension grouping
* Recursive folder organization
* GUI-based interface
* Scheduled automatic organization

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio
