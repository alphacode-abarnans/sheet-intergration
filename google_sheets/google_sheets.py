import os
import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# The scope defines what level of access is requested from the user's account.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1V-d4fd0QcTJhZ6ZHnf1psNnMBfSQ_bQSiOaEJQrCorU'  # Replace with your Google Sheets ID
RANGE_NAME = 'Sheet1!A1:D10'  # Example range

def get_google_sheet_data():
    """Shows basic usage of the Sheets API."""
    creds = None

    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds, _ = google.auth.load_credentials_from_file('token.json')

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Call the Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Read data from the spreadsheet
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    return values
