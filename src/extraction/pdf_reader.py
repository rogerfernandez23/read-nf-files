import pdfplumber
import re
from src.processing.validator import validator_cnpj, validator_value, validator_duplicity
from src.storage.csv_generate import read_file, save_file

def extract_data_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extratct_text() for page in pdf.pages)

            cnpj_match = re.search(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", text)
            cnpj = re.sub(r"\D", "", cnpj_match.group()) if cnpj_match else None

            value_match = re.search(r"(?i)(valor\s+total[^\d]*)\s*(\d+[.,]\d{2})", text)
            value_text = value_match.group(2).replace(".", "").replace(",", ".") if value_match else None
            value_total = float(value_text) if value_text else None

            if not validator_cnpj(cnpj):
                raise ValueError("CNPJ inválido!")
            
            if not validator_value(value_total):
                raise ValueError("Valor inválido!")
            
            registers = read_file()
            if validator_duplicity(cnpj, value_total, registers):
                raise ValueError("Duplicidade encontrada!")
            
            save_file(cnpj, value_total)

            return {"CNPJ": cnpj, "Valor Total": value_total}
        
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None
