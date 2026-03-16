# Network Automation Vendor Management

This project demonstrates **network automation using Python** to manage devices from multiple network vendors.

The system automates:

* device connectivity
* configuration deployment
* network monitoring tasks

It simulates a real-world **network automation platform used by DevOps and network engineering teams.**

---

# Project Overview

Managing large network infrastructures manually can be time-consuming and error-prone.

This project automates network operations including:

* connecting to network devices
* deploying configuration updates
* running monitoring commands

The automation pipeline allows engineers to manage network devices programmatically.

---

# Features

The system provides the following capabilities:

### Device Connectivity

Automated SSH connections to network devices using Netmiko.

---

### Configuration Management

Deploy configuration updates to devices automatically.

Example configurations include:

* interface creation
* IP configuration
* description updates

---

### Monitoring Automation

The system runs monitoring commands such as:

* interface status checks
* device version information

This enables automated network health checks.

---

# Project Structure

```
network-automation-vendor-management
│
├── screenshots
│   └── img.jpg
│
├── src
│   ├── automation_controller.py
│   ├── config_manager.py
│   ├── device_connector.py
│   └── monitoring.py
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone <repository-url>
cd network-automation-vendor-management
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

Run the automation controller:

```
python src/automation_controller.py
```

The system will:

1. Connect to network devices
2. Apply configuration updates
3. Execute monitoring commands

---

# Technologies Used

* Python
* Netmiko
* Paramiko
* Network automation frameworks

---

# Applications

This project demonstrates techniques used in:

* network automation
* infrastructure automation
* DevOps networking
* multi-vendor device management

---

# Future Improvements

Possible enhancements include:

* network inventory management
* configuration rollback
* automated network compliance checks
* integration with monitoring tools
* REST API based automation

---

# Author

Manish Rathi
AI & Python Engineering Portfolio

