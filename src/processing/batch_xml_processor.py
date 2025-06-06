import os
import glob

from ..storage.csv_generate import read_file
from ..extraction.xml_reader import extract_from_xml
from ..integration.reports import create_dir, move_dir, move_error
from ..google.sheets_writer import refresh_sheets_csv
from ..automation.logger import start_logging, register_log, end_logging
from .validator import validator_duplicity

def process_batch(file):
    create_dir()
    file_path = start_logging("xml")
    xml_files = [
    f for f in glob.iglob(os.path.join(file, '*'))
    if f.lower().endswith('.xml')
    ]

    if not xml_files:
        print(f"Nenhum arquivo XML encontrado na pasta.")
        return
    
    print(f"Encontrados {len(xml_files)} arquivos XML. Iniciando processamento...")

    register = read_file()
    errs = []
    for file in xml_files:
        try:
            result = extract_from_xml(file)
            if result:
                emit_cnpj, value = result['CNPJEmitente'], result['ValorTotal']
                if validator_duplicity(emit_cnpj, value, register):
                    register_log(file_path, file, "Ignorado", "Nota já existente na planilha")
                    print(f"Nota já processada: {file}")
                else:
                    move_dir(file, "xml")
                    register_log(file_path, file, "Sucesso")
                    print(f"Arquivo {file} processado com sucesso.")
            else:
                move_error(file)
                register_log(file_path, file, "Erro", "Erro ao processar o arquivo.")
                errs.append((file, "Erro!"))
        except Exception as e:
            move_error(file)
            register_log(file_path, file, "Erro", str(e))
            errs.append((file, str(e)))

    if errs:
        print("\nResumo de erros:")
        print(errs)
        for arq, err in errs:
            print(f"Erro no arquivo {arq}: {err}")
    else:
        print("\nTodos os arquivos foram processados com sucesso!")

    refresh_sheets_csv()
    print("Planilha atualizada com sucesso!")

    end_logging(file_path)