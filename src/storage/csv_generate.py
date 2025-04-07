import csv
import os

def generate_file(road):
    if not os.path.exists(road):
        with open(road, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cnpj', 'value'])

def save_file(cnpj, value, road="data/registros.csv"):
    generate_file(road)

    with open(road, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cnpj, value])

def read_file(road="data/registros.csv"):
    if not os.path.exists(road):
        return []
    
    with open(road, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [{"cnpj": row["cnpj"], "value": float(row["value"])}
        for row in reader
        ]