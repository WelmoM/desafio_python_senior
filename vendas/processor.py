from collections import defaultdict
from datetime import date
from typing import Iterable
from .model import Venda

def filtro_por_data(
    vendas: Iterable[Venda],
    start: date | None,
    end: date | None,
) -> list[Venda]:
    result = []
    for venda in vendas:
        if start and venda.date < start:
            continue
        if end and venda.date > end:
            continue
        result.append(venda)
    return result

def vendas_totais_por_produto(vendas: Iterable[Venda]) -> dict[str, float]:
    totals = defaultdict(float)
    for venda in vendas:
        totals[venda.produto] += venda.total
    return dict(totals)

def valor_total(vendas: Iterable[Venda]) -> float:
    return sum(venda.total for venda in vendas)

def produto_mais_vendido(vendas: Iterable[Venda]) -> str | None:
    quantities = defaultdict(int)
    for venda in vendas:
        quantities[venda.produto] += venda.qtdy

    if not quantities:
        return None

    return max(quantities.items(), key=lambda item: item[1])[0]
