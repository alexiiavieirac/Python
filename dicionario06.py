# Transformando Listas em Dicionários e Function zip

# Estrutura:

# Dicionário com valores padroes:
# dicionario = dict.fromkeys(lista_chaves, valor_padrao)

# Dicionário a partir de listas de tuplas:
# dicionario = dict(lista_tuplas)

# Dicionário a partir de duas listas:
# 1. Transformar listas em listas de tuplas com método zip;
# 2. Transformar em dicionário.

# listas_tuplas = zip(lista 1, lista 2)
# dicionario = dict(lista_tuplas)

produtos = ['iPhone', 'Samsung Galaxy', 'TV Samsung', 'PS5', 'Tablet', 'iPad', 'TV Philco', 'Notebook HP', 'Notebook Dell', 'Notebook Asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

listas_tuplas = zip(produtos, vendas)

dicionario_vendas = dict(listas_tuplas)
print(dicionario_vendas)

print('-----------------------------------------------')

# Fazendo por listas:

indice = produtos.index('iPad')
print('Vendemos {} iPads.'.format(vendas[indice]))

# Fazendo por dicionários:
print('Vendemos {} iPads.'.format(dicionario_vendas['iPad']))
