import os
import gspread
from google.oauth2.service_account import Credentials

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Path to your service account JSON file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), "service_account.json")

# Authenticate with Google Sheets
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Your Google Sheet ID
SPREADSHEET_ID = "1BW5N7krrZTg-PyzCsvZbOfnJMnTwNN2c3CU4qQeEZc8"

# Open the sheet
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Select first sheet


# Get Data
def get_google_sheet_data():
    return sheet.get_all_values()


# Add Data (Create)
def add_google_sheet_data(new_row):
    sheet.append_row(new_row)


# Update Data (Edit)
def update_google_sheet_data(row_number, updated_data):
    for col, value in enumerate(updated_data, start=1):
        sheet.update_cell(row_number, col, value)


# Delete Data
def delete_google_sheet_data(row_number):
    sheet.delete_rows(row_number)
