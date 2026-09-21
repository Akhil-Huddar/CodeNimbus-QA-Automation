from datetime import datetime
from pathlib import Path
import gspread
PROJECT_ROOT = Path(__file__).parent.parent
CREDENTIALS_FILE = PROJECT_ROOT / "credentials.json"
SHEET_NAME = "CodeNimbus QA Automation Test Results"
def log_test_result(test_case_name, status, execution_time, error_reason=""):
    client = gspread.service_account(filename=str(CREDENTIALS_FILE))
    worksheet = client.open(SHEET_NAME).sheet1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([timestamp, test_case_name, status, execution_time, error_reason])
    print("\nGoogle Sheets: Test result logged successfully.")
