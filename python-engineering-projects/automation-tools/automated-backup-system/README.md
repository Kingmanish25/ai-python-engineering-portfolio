# Automated Backup System

A lightweight Python automation tool that creates timestamped backups of a specified directory.
This utility is designed to demonstrate practical Python scripting for file system automation and backup management.

---

## Overview

The Automated Backup System copies all contents from a source folder into a backup directory while creating a unique timestamp for each backup.
This prevents overwriting previous backups and allows maintaining a history of folder states.

This project demonstrates:

* Python file system automation
* CLI-based utility design
* Timestamp-based backup versioning
* Modular Python scripting

---

## Features

* Creates **timestamped backups** to avoid overwriting previous copies
* Supports **custom source and destination directories** via command-line arguments
* Automatically **creates the backup directory if it does not exist**
* Provides **logging output** for backup status

---

## Project Structure

```
automated-backup-system
│
├── README.md
├── requirements.txt
│
├── data/
│   └── sample files for testing
│
├── backup/
│   └── generated backups
│
└── src/
    └── main.py
```

---

## Installation

Clone the repository and navigate to the project folder.

```bash
git clone <repository-url>
cd automated-backup-system
```

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script using the command line:

```bash
python src/main.py --source data --destination backup
```

### Example

```bash
python src/main.py --source data --destination backup
```

Example output:

```
2026-03-16 13:42:11 - INFO - Backup created successfully: backup/backup_20260316_134211
```

---

## How It Works

1. The script receives the **source folder** and **backup destination** as CLI arguments.
2. It validates that the source folder exists.
3. A **timestamp is generated** to uniquely identify the backup.
4. The source folder is copied to the backup directory using `shutil.copytree`.
5. A log message confirms the backup creation.

---

## Use Cases

This automation tool can be used for:

* Local file backup automation
* Periodic backup scripting
* Learning Python file system operations
* Basic DevOps and scripting utilities

---

## Future Improvements

Possible enhancements:

* Add **scheduled backups**
* Support **ZIP compressed backups**
* Add **file exclusion rules**
* Implement **backup cleanup policies**

---

## Author

Manish Rathi
AI & Python Engineering Portfolio
