# System Health Monitoring Tool

## Overview
This project is a Python-based system monitoring tool that tracks CPU, memory, and network performance. It uses modular design and custom exception handling to detect system issues, handle errors, and generate structured reports.

## Features
- Monitors CPU, memory, and network usage
- Detects threshold violations for system resources
- Implements custom exceptions for:
  - Service failures
  - Data corruption
  - Connection timeouts
- Generates formatted system health reports
- Logs results to a file with fail-safe error handling

## Technologies Used
- Python
- Custom modules
- File handling
- Exception handling

## How It Works
1. Each system component (CPU, memory, network) is checked using dedicated modules.
2. Data is compared against predefined thresholds.
3. Errors are handled using custom exception classes.
4. Results are compiled into a report and logged.

## Example Output
SYSTEM HEALTH REPORT  
------------------------------  
CPU: OK  
MEMORY: OK  
NETWORK: OK  

## Author
Chloe Williamson
