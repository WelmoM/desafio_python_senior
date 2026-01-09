# desafio_python_senior

## Desafio Python Sênior – Gerador de Relatório de Vendas Avançado

### Descrição:

Crie uma CLI em Python que processe um arquivo CSV de vendas e gere
relatórios ricos, com foco em qualidade de código, testes e boas práticas.

### Funcionalidades obrigatórias:

1. Leitura de CSV usando bibliotecas padrão (csv, argparse, logging):
Aceitar caminho do arquivo por parâmetro de linha de comando.
2. Cálculos principais:
Total de vendas por produto.
Valor total de todas as vendas.
Produto mais vendido
3. Filtros e formatos de saída:
Parâmetros opcionais para filtrar por data de venda (intervalo).
Saída em texto formatado (tabela) ou JSON (--format text|json).

### Requisitos de qualidade:

Tipagem estática com typing.
Estrutura modular (mínimo 2–3 módulos: parser, core, output).
Tratamento de erros e logs claros (logging).
CLI instalável via setup.py ou pyproject.toml (comando vendas-cli).
Testes unitários (pytest) cobrindo ao menos 80% do código.

### Exemplo de uso:

$ pip install .
$ vendas-cli vendas.csv --format text
$ vendas-cli vendas.csv --format json --start 2025-01-01 --end 2025-03-31
Entrega:
Repositório público no GitHub com código-fonte organizado.
README.md com instruções de instalação e uso.
Arquivo de configuração de testes (pytest.ini ou similar).
Tempo estimado: até 2 horas.