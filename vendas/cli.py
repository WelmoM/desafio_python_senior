import argparse
import logging
from datetime import datetime
from .parser import carregar_vendas
from .processor import (
    filtro_por_data,
    vendas_totais_por_produto,
    valor_total,
    produto_mais_vendido,
)
from .output import render_json, render_text


logging.basicConfig(level=logging.INFO)

def parse_date(value: str):
    return datetime.strptime(value, "%Y-%m-%d").date()

def main():
    parser = argparse.ArgumentParser(description="Relatórios de vendas")
    parser.add_argument("csv_path", help="Caminho para o arquivo CSV")
    parser.add_argument("--start-date", type=parse_date)
    parser.add_argument("--end-date", type=parse_date)
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
    )

    args = parser.parse_args()

    vendas = carregar_vendas(args.csv_path)
    vendas = filtro_por_data(vendas, args.start_date, args.end_date)

    totals = vendas_totais_por_produto(vendas)
    revenue = valor_total(vendas)
    most_sold = produto_mais_vendido(vendas)

    if args.format == "json":
        print(render_json(totals, revenue, most_sold))
    else:
        print(render_text(totals, revenue, most_sold))

if __name__ == "__main__":
    main()
