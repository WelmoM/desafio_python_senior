from vendas.parser import carregar_vendas
from datetime import date

def test_carregar_vendas(tmp_path):
    csv_content = """date,produto,quantidade,preco
2026-01-01,Notebook,2,3500.00
2026-01-02,Mouse,5,150.00
"""

    csv_file = tmp_path/"produtos.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    vendas = carregar_vendas(str(csv_file))

    assert len(vendas) == 2

    assert vendas[0].date == date(2026, 1, 1)
    assert vendas[0].produto == "Notebook"
    assert vendas[0].qtdy == 2
    assert vendas[0].preco == 3500.00
