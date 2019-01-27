from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#Permissions
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES);

creds = flow.run_local_server("localhost", 8080)
