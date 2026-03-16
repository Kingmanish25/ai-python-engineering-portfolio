# Weather CLI Tool

A lightweight Python command-line utility that retrieves real-time weather information for a specified city.
This project demonstrates practical Python scripting for **CLI utilities, web API consumption, and automation workflows**.

---

## Overview

The **Weather CLI Tool** fetches weather information for a given city using the public service **wttr.in**.
It allows users to quickly check weather conditions directly from the terminal.

This project demonstrates:

* Command-line interface (CLI) tool development
* HTTP request handling using Python
* Fetching weather information from web services
* Logging and structured Python scripting
* Error handling for network operations

---

## Features

* Retrieve weather information for any city
* CLI-based city input
* Uses a lightweight weather API (`wttr.in`)
* Logging output for weather queries
* Timeout protection for network requests
* Error handling for connection issues

---

## Project Structure

```text
weather-cli-tool
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
cd weather-cli-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the project root directory.

```bash
python src/main.py --city London
```

---

## Example

Check weather for London:

```bash
python src/main.py --city London
```

Example terminal output:

```text
2025-01-12 18:10:05 - INFO - Weather data for London
London: ☁️ +9°C
```

---

Check weather for New York:

```bash
python src/main.py --city "New York"
```

Example output:

```text
2025-03-25 18:12:14 - INFO - Weather data for New York
New York: ☀️ +15°C
```

---

Check weather for Tokyo:

```bash
python src/main.py --city Tokyo
```

Example output:

```text
2025-06-10 18:14:22 - INFO - Weather data for Tokyo
Tokyo: 🌧 +22°C
```

---

Check weather for Paris:

```bash
python src/main.py --city Paris
```

Example output:

```text
2025-09-05 18:16:11 - INFO - Weather data for Paris
Paris: 🌤 +19°C
```

---

## How It Works

1. The CLI tool receives the city name as a command-line argument.
2. A request is sent to the `wttr.in` weather service.
3. The service returns a short formatted weather response.
4. The response is displayed in the terminal.
5. Logging provides feedback about the request status.

---

## Use Cases

This CLI tool can be useful for:

* Quickly checking weather conditions
* Learning API-based automation with Python
* Practicing CLI tool development
* Building terminal productivity tools
* Automating weather checks in scripts

---

## Future Improvements

Possible enhancements include:

* Display multi-day weather forecasts
* Support multiple cities at once
* Show temperature trends
* Export weather data to files
* Add weather alerts

---

## Author

**Manish Rathi**
AI & Python Engineering Portfolio

