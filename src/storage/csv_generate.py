import csv
import os
from datetime import datetime

def generate_file(road):
    if not os.path.exists(road):
        with open(road, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cnpj', 'value'])

def save_file(emit_cnpj, emit_name, dest_cnpj, dest_name, value, datetime):
    file_exists = os.path.isfile('data/registros.csv')

    with open('data/registros.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists:
                writer.writerow([
                    "Data de Emissão",
                    "Emitente CNPJ",
                    "Emitente Nome",
                    "Recebedor CNPJ",
                    "Recebedor Nome",
                    "Valor Total"
                ])

        writer.writerow([
                datetime,
                emit_cnpj,
                emit_name,
                dest_cnpj,
                dest_name,
                value,
            ])

def read_file(road="data/registros.csv"):
    if not os.path.exists(road):
        return []
    
    with open(road, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)