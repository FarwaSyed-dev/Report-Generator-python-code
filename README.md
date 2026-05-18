
# report_generator code
Generates a summary report from a CSV file using pandas.

# What It Does
1. Reads a CSV file jobs.csv
2. Prints total rows and column names to the terminal
3. Exports a summary to `report.xlsx`
4. Logs actions and errors to `app.log`

# Requirements
Python 3.14
Install pandas openpyxl

pip install pandas openpyxl

# How to run
Open a terminal in the project folder and run:

  python report_generator.py jobs.csv

# Output

Terminal: Shows "Report Summary" , total rows, and column names
report.xlsx: Excel file with total rows and total columns, In this workbook, we will get two worksheets `data` and `summary`
app.log: Log file with timestamps for success and errors
