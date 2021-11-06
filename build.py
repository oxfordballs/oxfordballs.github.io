import os

from datetime import datetime

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

print(os.listdir())

build_dir = "build"
os.mkdir(build_dir)

with open(os.path.join(build_dir, "index.html"), "w") as f:
  f.write("hello world")
  f.write(datetime.now().isoformat())
