import os
import shutil
from datetime import datetime

def create_dir():
    for folder in ["processados/xml", "processados/pdf", "processados/erros"]:
        os.makedirs(folder, exist_ok=True)

def move_dir(file_path, type):
    destiny = os.path.join("processados", type, os.path.basename(file_path))
    shutil.move(file_path, destiny)

def move_error(file_path):
    destiny = os.path.join("processados/erros", name_generate(file_path))
    shutil.move(file_path, destiny)

def name_generate(file_path):
    name = os.path.basename(file_path)
    name, ext = os.path.splitext(name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{name}_{timestamp}{ext}"