import pandas as pd
import argparse
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def make_excel_report(csv_path):

    try:
        data = pd.read_csv(csv_path)

        print("\nReport Summary")
        print("-------------------")

        print("Total Rows:", len(data))

        print("\nColumn Names:")
        print(data.columns)

        report = {
            "Total Rows": [len(data)],
            "Total Columns": [len(data.columns)]
        }

        report_data = pd.DataFrame(report)

        with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
         report_data.to_excel(writer, sheet_name="Summary", index=False)
         data.to_excel(writer, sheet_name="Data", index=False)

        print("\nExcel report created.")

        logging.info("Report generated successfully.")

    except Exception as error:
        print("Error:", error)
        logging.error(error)

parser = argparse.ArgumentParser(description="CSV Report Generator")

parser.add_argument("file", help="Enter CSV file name")

args = parser.parse_args()

make_excel_report(args.file)