import os
import glob
from src.extraction.pdf_reader import extract_data_pdf
from google.sheets_writer import refresh_sheets_csv

def pdf_process(folder):
    file_pdf = glob.glob(os.path.join(folder, '*.pdf'))

    if not file_pdf:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return None
    
    print(f"Encontrados {len(file_pdf)} arquivos PDF. Iniciando processamento...")

    errs = []
    for file in file_pdf:
        try:
            result = extract_data_pdf(file)
            if result:
                print(f"Processado com sucesso: {file}")
            else:
                errs.append((file, "Erro desconhecido"))
        except Exception as e:
                errs.append((file, str(e)))

    
    if errs:
        print("Erros encontrados durante o processamento:")
        for arq, err in errs:
            print(f"Arquivo: {arq}, Erro: {err}")

    else:
         print("\nTodos os PDFs foram processados com sucesso!")
            

    refresh_sheets_csv()
        