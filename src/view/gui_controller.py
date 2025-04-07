import os
import tkinter as tk
from tkinter import scrolledtext, filedialog
from ..processing.batch_pdf_processor import pdf_process
from ..processing.batch_xml_processor import process_batch


LOG_DIR = 'logs'

def select_folder():
    return filedialog.askdirectory(
        title = "Selecione o arquivo",
    )

def process_xml():
    folder = select_folder()
    if folder:
        process_batch(folder)
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

def execute():

    global text_area

    top = tk.Tk()
    top.title("Leitor de Notas Fiscais")
    top.geometry("500x400")



    tk.Button(top, text="Processar XML", command=process_xml, width=20).pack(pady=5)
    tk.Button(top, text="Processar PDF", command=process_pdf, width=20).pack(pady=5)
    tk.Button(top, text="Abrir Logs", command=open_logs, width=20).pack(pady=5)

    text_area = scrolledtext.ScrolledText(top, width=60, height=15)
    text_area.pack(pady=10)

    refresh_logs()
    top.mainloop()