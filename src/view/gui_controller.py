import os
import tkinter as tk
from tkinter import scrolledtext, filedialog
from src.processing.batch_pdf_processor import pdf_process
from src.processing.batch_xml_processor import xml_process

LOG_DIR = 'logs'

def select_folder():
    return filedialog.askdirectory()

def process_xml():
    folder = select_folder()
    if folder:
        xml_process(folder)
        refresh_logs()

def process_pdf():
    folder = select_folder()
    if folder:
        pdf_process(folder)
        refresh_logs()
        
def open_logs():
    os.system(f'explorer "{LOG_DIR}"' if os.name == 'nt' else f'xdg-open "{LOG_DIR}"')

def refresh_logs():
    text_area.delete('1.0', tk.END)
    logs_file = sorted(os.listdir(LOG_DIR), reverse=True)

    if logs_file:
        with open(os.path.join(LOG_DIR, logs_file[0]), 'r', encoding='utf-8') as f:
            text_area.insert(tk.END, f.read())
    else:
        text_area.insert(tk.END, "Nenhum log encontrado.\n")

'''
Criação da Interface
'''

top = tk.Tk()
top.title("Leitor de Notas Fiscais")
top.geometry("500x400")

tk.button(top, text="Processar XML", command=process_xml, width=20).pack(pady=5)
tk.button(top, text="Processar PDF", command=process_pdf, width=20).pack(pady=5)
tk.button(top, text="Abrir Logs", command=open_logs, width=20).pack(pady=5)

text_area = scrolledtext.ScrolledText(top, width=60, height=15)
text_area.pack(pady=10)

refresh_logs()

top.mainloop()