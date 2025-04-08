import re

def validator_cnpj(emit_cnpj):
    if emit_cnpj and re.fullmatch(r"\d{14}", emit_cnpj):
        return True
    return False

def validator_value(value):
    return isinstance(value, (int, float)) and value > 0

def validator_duplicity(emit_cnpj, value, register):
    try:
        value = float(value)
        for row in register:
            if (
                row.get("emit_cnpj") == emit_cnpj and 
                float(row.get("value", -1)) == value
            ):
                return True
    except (ValueError, TypeError):
        pass
    return False

    # return any(nota["cnpj"] == cnpj and nota["value"] == value for nota in register)