import os
import json
import shutil
from jinja2 import Template

from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_ID = "1Xxs0KaEaD3XgQdrlNxbg25qwG2YvoBdoRJsIdDZIjvw"
SHEET_RANGE = 'Sheet1!A2:H100'

build_dir = "build"
os.mkdir(build_dir)

for f in ["about.html", "calendar.html", "favicon.ico", "script.js", "sitemap.xml", "style.css", "theme.css", "CNAME"]:
  shutil.copy(f, build_dir)

service_account_info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_SECRET"])
creds = service_account.Credentials.from_service_account_info(service_account_info)

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_RANGE).execute()
values = result.get('values', [])

rows = []

for row in values:
    event_name, date, theme, dress_code, prices, ticket_status, event_url, ticket_url = row
    if event_name == "":
      break
    print(event_name, date, theme, dress_code, prices, ticket_status, event_url, ticket_url)
    rows.append({
      "event_name": event_name,
      "date": date,
      "theme": theme,
      "dress_code": dress_code,
      "prices": prices,
      "ticket_status": ticket_status,
      "event_url": event_url,
      "ticket_url": ticket_url,
      "class": ""
    })
    
template = Template(open('index.html').read())
rendered = template.render(rows=rows)

with open(os.path.join(build_dir, "index.html"), "w") as f:
  f.write(rendered)
