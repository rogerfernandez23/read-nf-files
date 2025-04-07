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

        cnpj = root.find(".//ns:emit/ns:CNPJ", ns)
        cnpj = cnpj.text if cnpj is not None else None

        value = root.find(".//ns:total/ns:ICMSTot/ns:vNF", ns)
        value = float(value.text) if value is not None else None

        if not validator_cnpj(cnpj):
            raise ValueError(f"CNPJ inválido: {cnpj}")
        
        if not validator_value(value):
            raise ValueError(f"Valor total não encontrado no XML: {value}")

        register = read_file()
        if validator_duplicity(cnpj, value, register):
            raise ValueError(f"Nota duplicada!")
        

        save_file(cnpj, value)

        return {"cnpj": cnpj, "value": value}
    
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
        print(f"CNPJ: {data['CNPJ']}, Valor Total: {data['Valor Total']}")