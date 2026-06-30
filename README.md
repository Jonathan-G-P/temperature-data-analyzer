# Temperature Data Analyzer

A Python application that automates the analysis of temperature measurements stored in CSV files. The program computes statistical metrics, detects abnormal temperature events, generates reports, and visualizes the collected data.

---

## Overview

Industrial systems often generate large amounts of temperature measurements that must be analyzed to ensure safe operation. This project automates that process by reading temperature data from a CSV file and producing statistics, alarm reports, and graphical visualizations.

The project demonstrates practical applications of Python for engineering data analysis using Pandas and Matplotlib.

---

## Features

- Read temperature measurements from a CSV file.
- Calculate:
  - Maximum temperature
  - Minimum temperature
  - Average temperature
  - Standard deviation
- Detect warning events (>35 °C)
- Detect critical events (>40 °C)
- Generate automatic text reports.
- Plot temperature trends with highlighted warning and critical zones.

---

## Technologies Used

- Python 3
- Pandas
- Matplotlib
- Math

---

## Input Data

The application expects a CSV file with the following format:

```csv
Timestamp,Temperature
2026-06-01 08:00,24.5
2026-06-01 08:01,24.7
2026-06-01 08:02,25.0
```

---

## Output

The program generates:

- **Stats.txt**
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Standard deviation

- **Alarm Report.txt**
  - Warning events
  - Critical events

It also displays a graph showing:

- Temperature over time
- Warning zone
- Critical zone

---

## Project Structure

```
temperature-data-analyzer/
│
├── data.csv
├── temperature_data_analyzer.py
├── Stats.txt
├── Alarm Report.txt
├── images/
│   └── Graph.png
└── README.md
```

---

## Example Graph

<img width="1000" height="400" alt="Graph" src="https://github.com/user-attachments/assets/428dced0-c900-4946-bb27-90bf0a76433a" />

```markdown
![Temperature Graph](images/graph.png)
```

---

## Future Improvements

- Export reports to PDF.
- Interactive graphical interface.
- Automatic CSV selection.
- Real-time serial communication with Arduino.
- Support for multiple sensors.
- Detection of anomalies using statistical methods.

---

## Author

**Jonathan G. P.**

Electronic Engineering Student

Tecnológico de Costa Rica
