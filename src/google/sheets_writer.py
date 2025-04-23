import gspread
import csv
from google.oauth2.service_account import Credentials

CREDENTIALS = "./credentials.json"
SHEET = "Notas Processadas"

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def auth(tab_name="Logs"):
    creds = Credentials.from_service_account_file(CREDENTIALS, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheets = client.open(SHEET)
    tabs = sheets.worksheet(tab_name)
    return tabs

def refresh_sheets_csv(file_csv="data/registros.csv"):
    tabs = auth()

    with open(file_csv, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    tabs.clear()
    tabs.update('A1', data)

    print("Planilha atualizada com sucesso!")