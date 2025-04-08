import csv
import os
from datetime import datetime

def generate_file(road):
    if not os.path.exists(road):
        with open(road, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cnpj', 'value'])

def save_file(data):
    file_exists = False

    try:
        with open('data/registros.csv', mode='r', newline='', encoding='utf-8') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open('data/registros.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(
                ["DataHoraEmissao", "CNPJEmitente", "NomeEmitente",
                "CNPJDestinatario", "NomeDestinatario", "ValorTotal"]
                )
        writer.writerow([
            data.get('DataHoraEmissao', ''),
            data.get('CNPJEmitente', ''),
            data.get('NomeEmitente', ''),
            data.get('CNPJDestinatario', ''),
            data.get('NomeDestinatario', ''),
            data.get('ValorTotal', '')
        ])

# def save_file(cnpj, value, road="data/registros.csv"):
#     generate_file(road)

#     with open(road, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([cnpj, value])

def read_file(road="data/registros.csv"):
    if not os.path.exists(road):
        return []
    
    try:
        with open(road, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []