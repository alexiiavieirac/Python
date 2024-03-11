# List Comprehension com IF para "filtrar" itens

"""
Estrutura:
    lista = [expressão for item in iterable if condição]
"""

# Digamos que eu queria criar uma lista de produtos que bateram a meta:
meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['Vinho', 'Cafeteira', 'Microondas', 'iPhone']

# Fazendo com For tradicional:
produtos_acima_meta = []

for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)

print(produtos_acima_meta)

# Fazendo com List Comprehension:
juntar_listas = list(zip(vendas_produtos, produtos))
print(juntar_listas)

lista_meta = [produto for venda, produto in juntar_listas if venda >= meta]
print(lista_meta)

"""
Outra maneira de ser feito:
    produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
"""
