import re

def validator_cnpj(emit_cnpj):
    if emit_cnpj and re.fullmatch(r"\d{14}", emit_cnpj):
        return True
    return False

def validator_value(value):
    return isinstance(value, (int, float)) and value > 0

def validator_duplicity(emit_cnpj, value, register):
    for row in register:
        cnpj = row.get("Emitente CNPJ", "")
        val = row.get("Valor Total", "").replace(",", "").replace(".", "")

        try:
            val_float = float(val)
        except ValueError:
            continue
        
        if cnpj == emit_cnpj and abs(val_float - value) < 0.01:
            return True
        
    return False