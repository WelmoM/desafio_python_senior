from datetime import date
from vendas.model import Venda
from vendas.processor import (
    filtro_por_data,
    vendas_totais_por_produto,
    valor_total,
    produto_mais_vendido,
)

def criar_venda(
    data_venda: date,
    produto: str,
    qtdy: int,
    preco: float,
) -> Venda:
    return Venda(
        date=data_venda,
        produto=produto,
        qtdy=qtdy,
        preco=preco,
    )


def test_filtro_datas_sem_vendas():
    vendas = [
        criar_venda(date(2024, 1, 1), "A", 1, 10.0),
        criar_venda(date(2024, 1, 2), "B", 2, 20.0),
    ]

    result = filtro_por_data(vendas, None, None)

    assert result == vendas


def test_filtro_so_por_inicio():
    vendas = [
        criar_venda(date(2024, 1, 1), "A", 1, 10.0),
        criar_venda(date(2024, 1, 3), "B", 2, 20.0),
    ]

    result = filtro_por_data(vendas, start=date(2024, 1, 2), end=None)

    assert len(result) == 1
    assert result[0].produto == "B"


def test_filtro_por_inicio_fim():
    vendas = [
        criar_venda(date(2024, 1, 1), "A", 1, 10.0),
        criar_venda(date(2024, 1, 2), "B", 2, 20.0),
        criar_venda(date(2024, 1, 3), "C", 3, 30.0),
    ]

    result = filtro_por_data(
        vendas,
        start=date(2024, 1, 2),
        end=date(2024, 1, 2),
    )

    assert len(result) == 1
    assert result[0].produto == "B"


def test_vendas_totais_produto():
    vendas = [
        criar_venda(date.today(), "A", 2, 10.0),
        criar_venda(date.today(), "A", 1, 10.0),
        criar_venda(date.today(), "B", 1, 20.0),
    ]

    result = vendas_totais_por_produto(vendas)

    assert result == {
        "A": 30.0,
        "B": 20.0,
    }


def test_total_revenue():
    vendas = [
        criar_venda(date.today(), "A", 2, 10.0),
        criar_venda(date.today(), "B", 1, 20.0),
    ]

    assert valor_total(vendas) == 40.0


def test_most_sold_product():
    vendas = [
        criar_venda(date.today(), "A", 5, 10.0),
        criar_venda(date.today(), "B", 2, 20.0),
    ]

    assert produto_mais_vendido(vendas) == "A"


def test_most_sold_product_empty():
    assert produto_mais_vendido([]) is None
