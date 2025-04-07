import os
import glob

from ..extraction.pdf_reader import extract_data_pdf
from ..integration.reports import create_dir, move_dir, move_error
from ..google.sheets_writer import refresh_sheets_csv
from ..automation.logger import start_logging, register_log, end_logging
from .validator import validator_duplicity

def pdf_process(folder):
    create_dir()
    file_path = start_logging("pdf")
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
                cnpj, value = result['cnpj'], result['value']
                if validator_duplicity(cnpj, value):
                    register_log(file_path, file, "Ignorado", "Nota já existente na planilha")
                    print(f"Nota já processada: {file}")
                else:
                    move_dir(file, "pdf")
                    register_log(file_path, file, "Sucesso")
                    print(f"Processado com sucesso: {file}")
            else:
                move_error(file)
                register_log(file_path, file, "Erro desconhecido")
                errs.append((file, "Erro desconhecido"))
        except Exception as e:
                move_error(file)
                register_log(file_path, file, "Erro", str(e))
                errs.append((file, str(e)))

    
    if errs:
        print("Erros encontrados durante o processamento:")
        for arq, err in errs:
            print(f"Arquivo: {arq}, Erro: {err}")

    else:
         print("\nTodos os PDFs foram processados com sucesso!")
            

    # refresh_sheets_csv()
    # print("Planilha atualizada com sucesso!")
    
    end_logging(file_path)