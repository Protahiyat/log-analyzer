# Log Analyzer 🕵️‍♀️

A beginner-friendly log analysis script built in Python to simulate a basic log review process.

## 🔍 What It Does

- Reads and processes log files (`auth.log`)
- Flags potentially suspicious log entries (like failed logins, root access attempts, etc.)
- Generates a clean, readable alert report (`output.txt`)

This is a foundational exercise to get comfortable with analyzing system logs — something every SOC analyst and security nerd will need down the road.

## 📁 Files

- `log_analyzer.py` — The main Python script
- `auth.log` — The sample system log input
- `output.txt` — The output report showing flagged activity
- `incident_report.txt` — A mini incident summary based on the findings

## ⚙️ How to Run

```bash
python3 log_analyzer.py
