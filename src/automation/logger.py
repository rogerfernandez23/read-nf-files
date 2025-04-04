import os
from datetime import datetime

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