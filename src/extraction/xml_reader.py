import xml.etree.ElementTree as ET
from ..processing.validator import validator_cnpj, validator_value, validator_duplicity
from ..storage.csv_generate import read_file, save_file

def register_exists():
    return read_file()

def extract_from_xml(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Define namespace da NF-e
        ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}

        # Extração dos Dados Necessários
        datetime_emit = root.find(".//ns:ide/ns:dEmi", ns)
        datetime_emit = datetime_emit.text if datetime_emit is not None else None

        emit_cnpj = root.find(".//ns:emit/ns:CNPJ", ns)
        emit_cnpj = emit_cnpj.text if emit_cnpj is not None else None

        emit_name = root.find(".//ns:emit/ns:xNome", ns)
        emit_name = emit_name.text if emit_name is not None else None

        dest_cnpj = root.find(".//ns:dest/ns:CNPJ", ns)
        dest_cnpj = dest_cnpj.text if dest_cnpj is not None else None

        dest_name = root.find(".//ns:dest/ns:xNome", ns)
        dest_name = dest_name.text if dest_name is not None else None

        value = root.find(".//ns:total/ns:ICMSTot/ns:vNF", ns)
        value = float(value.text) if value is not None else None

        # Validações de Campos
        if not validator_cnpj(emit_cnpj):
            raise ValueError(f"CNPJ inválido: {emit_cnpj}")
        
        if not validator_value(value):
            raise ValueError(f"Valor total não encontrado no XML: {value}")

        register = read_file()
        if validator_duplicity(emit_cnpj, value, register):
            raise ValueError(f"Nota duplicada!")
        

        save_file({
            "DataHoraEmissao": datetime_emit,
            "CNPJEmitente": emit_cnpj,
            "NomeEmitente": emit_name,
            "CNPJDestinatario": dest_cnpj,
            "NomeDestinatario": dest_name,
            "ValorTotal": value
        })

        return {
            "DataHoraEmissao": datetime_emit,
            "CNPJEmitente": emit_cnpj,
            "NomeEmitente": emit_name,
            "CNPJDestinatario": dest_cnpj,
            "NomeDestinatario": dest_name,
            "ValorTotal": value
        }
    
    except ET.ParseError as e:
        print(f"XML malformado: {e}")
        return None
    except ValueError as e:
        print(f"Erro de validação: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
    

if __name__ == "__main__":
    xml_file = 'road/file-nota-fiscal.xml'
    data = extract_from_xml(xml_file)
    if data:
        print("--- Dados extraídos ---")
        for key, value in data.items():
            print(f"{key}: {value}")