import pdfplumber
import re
from ..automation.parse_nfse_text import parse_nfse_text
from ..processing.validator import validator_cnpj, validator_value, validator_duplicity
from ..storage.csv_generate import read_file, save_file
from ..automation.logger import register_detailed

def extract_data_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            texts = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    texts.append(page_text)
            text = "\n".join(texts)            
            
        data = parse_nfse_text(text)

        if not validator_cnpj(data["emit_cnpj"]) or not validator_cnpj(data["dest_cnpj"]):
            raise ValueError("CNPJ inválido!")
            
        # if not validator_value(data["value"]):
        #     raise ValueError("Valor inválido!")
            
        registers = read_file()
        if validator_duplicity(data["emit_cnpj"], data["value"], registers):
            raise ValueError("Duplicidade encontrada!")
            
        save_file(
            data["emit_cnpj"],
            data["emit_name"],
            data["dest_cnpj"],
            data["dest_name"],
            data["value"],
            data["datetime"]
        )

        register_detailed(
            path_log="data/registros.csv",
            file="PDF Extraído",
            success=True,
            emit_cnpj=data["emit_cnpj"],
            emit_name=data["emit_name"],
            dest_cnpj=data["dest_cnpj"],
            dest_name=data["dest_name"],
            value=data["value"],
            emission_date=data["datetime"],
            error_msg="Erros",
        )

        return {
            "DataHoraEmissao": data["datetime"],
            "CNPJEmitente": data["emit_cnpj"],
            "NomeEmitente": data["emit_name"],
            "CNPJDestinatario": data["dest_cnpj"],
            "NomeDestinatario": data["dest_name"],
            "ValorTotal": data["value"]
        }
        
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None