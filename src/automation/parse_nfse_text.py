import re

def extract_match(pattern, text, group=1):
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(group) if match else None

def parse_nfse_text(text):
    datetime_match = re.search(r"\d{2}/\d{2}/\d{4}\s*\d{2}:\d{2}:\d{2}", text)
    datetime = datetime_match.group() if datetime_match else None

    emit_cnpj_match = re.search(r"Emitente.*?(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})", text, re.DOTALL | re.IGNORECASE)
    emit_name_match = re.search(r"Emitente[^\n]*\n([^\n]+)", text, re.IGNORECASE)
    emit_cnpj = re.sub(r"\D", "", emit_cnpj_match.group(1)) if emit_cnpj_match else None
    emit_name = emit_name_match.group(1).strip() if emit_name_match else None

    dest_cnpj_match = re.search(r"Tomador.*?(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})", text, re.DOTALL | re.IGNORECASE)
    dest_name_match = re.search(r"Tomador[^\n]*\n([^\n]+)", text, re.IGNORECASE)
    dest_cnpj = re.sub(r"\D", "", dest_cnpj_match.group(1)) if dest_cnpj_match else None
    dest_name = dest_name_match.group(1).strip() if dest_name_match else None

    value = extract_match(r"valor\s*(?:total|líquido)?.*?(\d{1,3}(?:\.\d{3})*,\d{2})", text)

    return {
        "datetime": datetime,
        "emit_cnpj": emit_cnpj,
        "emit_name": emit_name,
        "dest_cnpj": dest_cnpj,
        "dest_name": dest_name,
        "value": value
    }
