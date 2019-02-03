import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPES)

gs = gspread.authorize(creds)

workSheet = gs.open_by_key("1bd1-RmF6QmJTiaxla74WEwtCQTh6xIWqulF_3UA_E2k").get_worksheet(0)

# Prints "Cell cannot be found" if my keyboard smash does not exist in isibels document
try:
    workSheet.find("xffaa")
except gspread.exceptions.CellNotFound:
    print("Cell cannot be found")

