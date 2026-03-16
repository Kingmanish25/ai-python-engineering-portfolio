# System Resource Monitor

A lightweight Python automation utility that monitors system resource usage such as CPU and memory in real time.
This project demonstrates practical Python scripting for **system monitoring, command-line tools, and automation utilities**.

---

## Overview

The **System Resource Monitor** continuously tracks system performance metrics including **CPU usage and memory consumption**.
It uses the `psutil` library to gather system statistics and displays them at configurable time intervals.

This project demonstrates:

* System monitoring using Python
* Command-line interface (CLI) utilities
* Continuous monitoring loops
* Logging for automation scripts
* Resource usage tracking

---

## Features

* Monitor CPU usage in real time
* Track system memory usage
* Configurable monitoring interval using CLI
* Logging output for system statistics
* Graceful shutdown using `Ctrl + C`

---

## Project Structure

```
system-resource-monitor
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
cd system-resource-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --interval 5
```

This runs the system monitor every **5 seconds**.

---

## Example

Example terminal output:

```
2025-07-16 17:40:10 - INFO - System monitoring started (interval: 5 seconds)
2025-07-16 17:40:11 - INFO - CPU Usage: 12.4%
2025-07-16 17:40:11 - INFO - Memory Usage: 46.1%
2025-07-16 17:40:16 - INFO - CPU Usage: 9.8%
2025-07-16 17:40:16 - INFO - Memory Usage: 45.9%
```

Stopping the monitor:

```
2025-07-16 17:41:02 - INFO - System monitoring stopped by user
```

---

## How It Works

1. The script receives the monitoring interval through a CLI argument.
2. The `psutil` library retrieves system resource statistics.
3. CPU and memory usage are logged to the terminal.
4. The monitoring loop repeats at the specified interval.
5. The script stops safely when the user presses `Ctrl + C`.

---

## Use Cases

This automation tool can be used for:

* Monitoring system performance
* Learning system resource monitoring in Python
* Creating lightweight DevOps monitoring utilities
* Tracking CPU and memory usage during experiments
* Basic server monitoring scripts

---

## Future Improvements

Possible enhancements include:

* Disk usage monitoring
* Network activity tracking
* Export logs to files
* Threshold-based alerts
* Integration with monitoring dashboards

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

