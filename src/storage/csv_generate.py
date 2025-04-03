import csv
import os

def generate_file(road):
    if not os.path.exists(road):
        with open(road, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['CNPJ', 'Value'])

def save_file(cnpj, value, road="registros.csv"):
    generate_file(road)

    with open(road, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cnpj, value])

def read_file(road="registros.csv"):
    if not os.path.exists(road):
        return []
    
    with open(road, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]