# Todo Manager CLI Tool

A lightweight Python command-line utility that helps users manage daily tasks directly from the terminal.
This project demonstrates practical Python scripting for **task management, CLI tools, and persistent data storage**.

---

## Overview

The **Todo Manager CLI Tool** allows users to create and manage a list of tasks from the command line.
Tasks are stored locally in a JSON file, allowing them to persist between program executions.

This project demonstrates:

* Command-line interface (CLI) tool development
* Persistent task storage using JSON
* Logging and structured Python scripting
* Task management automation
* File handling in Python

---

## Features

* Add tasks from the command line
* View a list of saved tasks
* Persistent task storage using JSON
* Lightweight task management utility
* Logging output for task operations

---

## Project Structure

```text
todo-manager-cli
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
cd todo-manager-cli
```

Install dependencies (if required):

```bash
pip install -r requirements.txt
```

> This project uses only Python's standard library.

---

## Usage

### Add a new task

```bash
python src/main.py add "Finish project documentation"
```

Example output:

```text
2025-08-05 20:10:05 - INFO - Task added successfully
```

---

### Add another task

```bash
python src/main.py add "Prepare meeting notes"
```

Example output:

```text
2025-08-05 20:12:12 - INFO - Task added successfully
```

---

### List tasks

```bash
python src/main.py list
```

Example output:

```text
1. Finish project documentation
2. Prepare meeting notes
```

---

### Add another task later

```bash
python src/main.py add "Review code changes"
```

Example output:

```text
2025-08-05 20:14:21 - INFO - Task added successfully
```

---

## How It Works

1. Tasks are stored in a local JSON file (`tasks.json`).
2. The CLI tool reads tasks from the file when executed.
3. When a new task is added, it is appended to the JSON file.
4. The list command displays all stored tasks.
5. Logging reports task operations.

---

## Use Cases

This CLI tool can be useful for:

* Managing personal tasks
* Learning CLI-based application development
* Practicing file-based data persistence
* Creating lightweight productivity tools
* Automating small daily task lists

---

## Future Improvements

Possible enhancements include:

* Mark tasks as completed
* Delete tasks
* Task priority levels
* Due date reminders
* Export tasks to CSV or JSON

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

