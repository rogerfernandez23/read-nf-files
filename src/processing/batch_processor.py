import os
import glob
from src.extraction.xml_reader import extract_from_xml

def process_batch(folder):
    xml_files = glob.glob(os.path.join(folder, '*.xml'))

    if not xml_files:
        print(f"Nenhum arquivo XML encontrado na pasta.")
        return
    
    print(f"Encontrados {len(xml_files)} arquivos XML. Iniciando processamento...")

    errs = []
    for file in xml_files:
        try:
            result = extract_from_xml(file)
            if result:
                print(f"Arquivo {file} processado com sucesso.")
            else:
                errs.append((file, "Erro!"))
        except Exception as e:
            errs.append((file, str(e)))

    if errs:
        print("\nResumo de erros:")
        for arq, err in errs:
            print(f"Erro no arquivo {arq}: {err}")
    else:
        print("\nTodos os arquivos foram processados com sucesso!")