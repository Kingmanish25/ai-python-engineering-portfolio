# Folder Sync Tool

A lightweight Python automation utility that synchronizes files between two folders.
This project demonstrates practical Python scripting for **file synchronization, command-line tools, and automation utilities**.

---

## Overview

The **Folder Sync Tool** copies files from a source directory to a destination directory while preserving file metadata.
It ensures that files from one folder are replicated into another folder, making it useful for **basic backup and synchronization tasks**.

This project demonstrates:

* Python file system automation
* Command-line interface (CLI) utilities
* Folder synchronization logic
* Logging and structured Python scripting

---

## Features

* Synchronizes files between two folders
* Automatically creates destination folder if it does not exist
* Preserves file metadata using `shutil.copy2`
* Command-line interface for specifying source and destination folders
* Logging to track file copy operations

---

## Project Structure

```
folder-sync-tool
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
cd folder-sync-tool
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
python src/main.py --source source_folder --destination destination_folder
```

---

## Example

### Source folder

```
source_folder
│
├── report.txt
├── image.jpg
```

### Destination folder after synchronization

```
destination_folder
│
├── report.txt
└── image.jpg
```

Example terminal output:

```
2025-07-16 14:10:32 - INFO - Copied report.txt → destination_folder
2025-07-16 14:10:32 - INFO - Copied image.jpg → destination_folder
2025-07-16 14:10:32 - INFO - Folder synchronization completed
```

---

## How It Works

1. The script receives **source** and **destination** folder paths as command-line arguments.
2. It validates that the source folder exists.
3. The destination folder is created automatically if it does not exist.
4. Each file from the source folder is copied to the destination folder using `shutil.copy2`.
5. Logging displays the status of each copied file.

---

## Use Cases

This automation tool can be useful for:

* Simple local folder backups
* Synchronizing files between directories
* File replication scripts
* Learning Python file automation
* Practicing CLI-based Python utilities

---

## Future Improvements

Possible enhancements include:

* Two-way folder synchronization
* File change detection
* Recursive directory synchronization
* Automatic scheduled synchronization
* Progress indicators for large file transfers

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

