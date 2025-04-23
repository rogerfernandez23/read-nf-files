import os
from datetime import datetime
from ..google.sheets_writer import auth

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def start_logging(type):
    """
    Cria um arquivo de log com o timestamp para o tipo especificado (xml ou pdf).
    """

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = f"log_{type}_{timestamp}.log"
    folder = os.path.join(LOG_DIR, name)
    
    with open(folder, "w", encoding="utf-8") as f:
        f.write(f"Iniciando processamento de {type.upper()} - {timestamp}\n")
        f.write("=" * 60 + "\n")
    return folder

def register_sheets(file, status, emit_cnpj, emit_name, dest_cnpj, dest_name, value, emission_date, error_msg=""):
    try:
        sheet = auth("Registros")

        sheet.append_row([
            file,
            status,
            emit_cnpj or '',
            emit_name or '',
            dest_cnpj or '',
            dest_name or '',
            str(value) if value else '',
            emission_date or '',
            error_msg,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])
    except Exception as e:
        print(f"Erro ao registrar na planilha: {e}")

def register_detailed(path_log, file, success, emit_cnpj=None, emit_name=None, dest_cnpj=None, dest_name=None, value=None, emission_date=None, error_msg=""):
    status = "Sucesso" if success else "Erro"
    msg = f"{status} - {file}\n"

    if success:
        msg += f"  Emitente: {emit_name} ({emit_cnpj})\n"
        msg += f"  Destinatário: {dest_name} ({dest_cnpj})\n"
        msg += f"  Valor: {value}\n"
        msg += f"  Emissão: {emission_date}\n"
    else:
        msg += f"  Erro: {error_msg}\n"

    with open(path_log, "a", encoding="utf-8") as f:
        f.write(msg + "-" * 60 + "\n")

    register_sheets(
        file=file,
        status=status,
        emit_cnpj=emit_cnpj,
        emit_name=emit_name,
        dest_cnpj=dest_cnpj,
        dest_name=dest_name,
        value=value,
        emission_date=emission_date,
        error_msg=error_msg
    )
    
    with open(path_log, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            value_float = float(str(value).replace('.', '').replace(',', '.'))
        except Exception:
            value_float = 0.0
        formated_value = f"{value_float:.2f}".replace('.', ',')

        if success:
            f.write(
                f"{timestamp} - SUCESSO - {file} | Emissão: {emission_date} | "
                f"Emitente: {emit_name} ({emit_cnpj}) | "
                f"Recebedor: {dest_name} ({dest_cnpj}) | "
                f"Valor: R$ {formated_value}\n"
            )
        else:
            f.write(
                f"{timestamp} - ERRO - {file} | {error_msg} | Emissão: {emission_date} | "
                f"Emitente: {emit_name or 'Desconhecido'} ({emit_cnpj or '---'}) | "
                f"Recebedor: {dest_name or 'Desconhecido'} ({dest_cnpj or '---'}) | "
                f"Valor: R$ {formated_value}\n"
            )

def register_log(path_log, file, status, message=""):
    """
    Escreve entrada no log.
    :param caminho_log: Caminho do arquivo de log.
    :param arquivo: Nome do arquivo processado.
    :param status: 'Sucesso' ou 'Erro'.
    :param mensagem: Mensagem adicional (erro)
    """

    with open(path_log, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {status} - {file} {('- ' + message) if message else ''}\n")

    
def end_logging(path_log):
    """
    Finaliza o log.
    :param caminho_log: Caminho do arquivo de log.
    """
    
    with open(path_log, "a", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Finalizado em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")