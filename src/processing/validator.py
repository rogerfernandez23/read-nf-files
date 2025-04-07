import re

def validator_cnpj(cnpj):
    if cnpj and re.fullmatch(r"\d{14}", cnpj):
        return True
    return False

def validator_value(value):
    return isinstance(value, (int, float)) and value > 0

def validator_duplicity(cnpj, value, register):
    return any(nota["cnpj"] == cnpj and nota["value"] == value for nota in register)