import os
import json

from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_ID = "1Xxs0KaEaD3XgQdrlNxbg25qwG2YvoBdoRJsIdDZIjvw"
SAMPLE_RANGE_NAME = 'Sheet1!A1:2'

build_dir = "build"
os.mkdir(build_dir)
  
service_account_info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_SECRET"])
credentials = service_account.Credentials.from_service_account_info(service_account_info)

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
