This repository contains a Python script to extract browsing history from Google Chrome and export it to an Excel file.

# Features
Extracts URLs, titles, and visit dates from Chrome history.
Exports data to an Excel file (chrome_history.xlsx).
Supports Windows, macOS, and Linux.

# Requirements
Python 3.x
pandas library
openpyxl library

# Installation
Clone this repository or download the script:

```
git clone https://github.com/yourusername/chrome-history-exporter.git
cd chrome-history-exporter
```

Install the required libraries:

```
pip install pandas openpyxl
```

# Usage
Ensure Google Chrome is closed.
Run the script:
```
python main.py
```
The script will create an Excel file named chrome_history.xlsx in the current directory.

# Notes
Make sure you have the appropriate permissions to access Chrome's history database.
Chrome should be closed to avoid conflicts with the history database.

# Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or bugs.
