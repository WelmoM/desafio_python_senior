import csv
import logging
from datetime import datetime
from .model import Venda
from pathlib import Path

logger = logging.getLogger(__name__)

def arquivo_existe(path_arquivo: str) -> bool:
    file_path = Path(path_arquivo)
    
    return bool(file_path.is_file())

def carregar_vendas(path_arquivo: str) -> list[Venda]:
    vendas = []

    if not arquivo_existe(path_arquivo):
        logging.error(" Arquivo %s não existe", path_arquivo)
        exit()
    
    logger.info("Lendo arquivo CSV: %s", path_arquivo)
    
    with open(path_arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        colunas = reader.fieldnames
        if not colunas:
            logging.error("Sem colunas nomeadas no Arquivo CSV")
            exit()

        if ("date" not in colunas) or ("produto" not in colunas) or ("quantidade" not in colunas) or ("preco" not in colunas):
            logging.error("Faltando Colunas no Arquivo CSV")
            exit()

        for row in reader:
            venda = Venda(
                date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
                produto=row["produto"],
                qtdy=int(row["quantidade"]),
                preco=float(row["preco"]),
            )
            vendas.append(venda)

    logger.info("Total de registros carregados: %d", len(vendas))
    return vendas