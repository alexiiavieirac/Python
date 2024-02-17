# Métodos úteis de dicionários

# items() dos dicionários

# itens_dicionario = dicionario.items()
#   Ou
# for item in dicionario.items()
#   cada item do dicionario em formato de tupla

vendas_tecnologia = {'iPhone': 15000, 'Samsung Galaxy': 12000, 'TV Samsung': 10000, 'PS5': 14300, 'Tablet': 1720, 'iPad': 1000, 'TV Philco': 2500, 'Notebook HP': 1000, 'Notebook Dell': 17000, 'Notebook Asus': 2450}

# itens_dicionario = vendas_tecnologia.items()
# print(itens_dicionario)

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

print('-----------------------------------------------')

for produto, qtde in vendas_tecnologia.items():
    if qtde > 5000:
        print('{}: {} unidades'.format(produto, qtde))

print('-----------------------------------------------')

# Listas importantes a partir do Dicionário:

# Métodos Importantes:

# .keys() -> uma 'lista' com todas as chaves do dicionário;
# .values() -> uma 'lista' com todos os valores do dicionário.

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()

print(chaves)
print(valores)

print('-----------------------------------------------')

# Para organizar em ordem alfabética:

lista_chaves = list(chaves)
lista_chaves.sort()

for chave in lista_chaves:
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

