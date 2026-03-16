# Scheduled Task Automation Tool

A lightweight Python automation utility that runs tasks at fixed time intervals.
This project demonstrates practical Python scripting for **task scheduling, command-line tools, and automation workflows**.

---

## Overview

The **Scheduled Task Automation Tool** allows users to execute tasks repeatedly at specified time intervals.
It uses the `schedule` library to manage periodic execution of functions and provides a simple CLI interface for configuring the scheduling interval.

This project demonstrates:

* Python task scheduling
* Command-line interface (CLI) utilities
* Logging for automation scripts
* Continuous task execution loops

---

## Features

* Schedule tasks to run at fixed time intervals
* Command-line argument to configure interval
* Logging output for task execution
* Graceful shutdown using `Ctrl + C`
* Lightweight automation workflow

---

## Project Structure

```text
scheduled-task-automation
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
cd scheduled-task-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --interval 10
```

This schedules a task that runs every **10 seconds**.

---

## Example

Example terminal output:

```text
2025-07-16 16:25:10 - INFO - Task scheduled every 10 seconds
2025-07-16 16:25:20 - INFO - Scheduled task running
2025-07-16 16:25:30 - INFO - Scheduled task running
2025-07-16 16:25:40 - INFO - Scheduled task running
```

Stopping the scheduler:

```text
2025-07-16 16:26:12 - INFO - Scheduler stopped by user
```

---

## How It Works

1. The script receives the execution interval through a CLI argument.
2. The `schedule` library registers a task that runs every specified interval.
3. A loop continuously checks for pending scheduled jobs.
4. When the interval is reached, the task function executes.
5. Logging records task execution events.

---

## Use Cases

This automation tool can be used for:

* Running periodic maintenance scripts
* Automated monitoring checks
* Scheduled data processing tasks
* Simple DevOps automation
* Learning task scheduling in Python

---

## Future Improvements

Possible enhancements include:

* Support for scheduling tasks at specific times (daily / weekly)
* Multiple scheduled jobs
* Logging to files
* Email or webhook notifications
* Integration with external automation workflows

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

