import xml.etree.ElementTree as ET
from src.processing.validator import validate_cnpj, validate_value, validator_duplicity
from src.storage.csv_generate import read_file, save_file

def register_exists():
    return [
        {"CNPJ": "12345678000195", "Valor_Total": 1500.75}
    ]

def extract_from_xml(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}

        cnpj = root.find(".//ns:emit/ns:CNPJ", ns)
        cnpj = cnpj.text if cnpj is not None else None

        value = root.find(".//ns:total/ns:ICMSTot/ns:vNF", ns)
        value = float(value.text) if value is not None else None

        if not validate_cnpj(cnpj):
            raise ValueError(f"CNPJ inválido: {cnpj}")
        
        if not validate_value(value):
            raise ValueError(f"Valor inválido: {value}")

        registers = read_file()
        if validator_duplicity(cnpj, value, registers):
            raise ValueError(f"Nota duplicada!")
        

        save_file(cnpj, value)

        return {"CNPJ": cnpj, "Valor Total": value}
    
    except Exception as e:
        print(f"Erro ao processar XML: {e}")
        return None
    

if __name__ == "__main__":
    xml_file = 'road/file-nota-fiscal.xml'
    data = extract_from_xml(xml_file)
    if data:
        print(f"CNPJ: {data['CNPJ']}, Valor Total: {data['Valor Total']}")