import json

def render_text(
    valor_por_produto: dict[str, float],
    valor_total: float,
    produto_mais_vendido: str | None,
) -> str:
    lines = []
    lines.append("VENDAS POR PRODUTO")
    lines.append("-" * 40)

    for product, total in valor_por_produto.items():
        lines.append(f"{product:<20} R$ {total:>10.2f}")

    lines.append("-" * 40)
    lines.append(f"TOTAL GERAL:     R$ {valor_total:>.2f}")
    lines.append(f"PRODUTO MAIS VENDIDO: {produto_mais_vendido or 'N/A'}")

    return "\n".join(lines)

def render_json(
    valor_por_produto: dict[str, float],
    valor_total: float,
    produto_mais_vendido: str | None,
) -> str:
    return json.dumps(
        {
            "valor_por_produto": valor_por_produto,
            "valor_total": valor_total,
            "produto_mais_vendido": produto_mais_vendido,
        },
    )
