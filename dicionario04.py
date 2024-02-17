# For nos Dicionáios

# Estrutura:

# for chave in dicionario:
#   faça algo

vendas_tecnologia = {'iPhone': 15000, 'Samsung Galaxy': 12000, 'TV Samsung': 10000, 'PS5': 14300, 'Tablet': 1720, 'iPad': 1000, 'TV Philco': 2500, 'Notebook HP': 1000, 'Notebook Dell': 17000, 'Notebook Asus': 2450}

# For:
for chave in vendas_tecnologia:
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

# Usamos para somar os itens que há dentro das chaves outra variável:
total_notebooks = 0

for chave in vendas_tecnologia:
    if 'Notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]

print('{} total de vendas de Notebook.'.format(total_notebooks))
