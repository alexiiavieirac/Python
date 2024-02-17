# Estrutura:
# dicionario = {chave: valor, chave: valor, chave: valor...}

# Vantagens e Desvantagens:
# Não devem ser usados para pegar itens numa determinada ordem;
# Podem ter valores heterogéneos (vários tipos de valores em um mesmo dicionário: inteiros, strings, listas etc);
# Chaves são únicas obrigatórias;
# Mais intuitivos de trabalhar.

mais_vendidos = {'Tecnologia': 'iPhone', 'Refrigeracao': 'Ar Consul 12000 btu', 'Livros': 'O Alquimista', 'Eletrodoméstico': 'Geladeira', 'Lazer': 'Prancha Surf'}
vendas_tecnologia = {'iPhone': 15000, 'Samsung Galaxy': 12000, 'TV Samsung': 10000, 'PS5': 14300, 'Tablet': 1720, 'iPad': 1000, 'TV Philco': 2500, 'Notebook HP': 1000, 'Notebook Dell': 17000, 'Notebook Asus': 2450}

# Qual foi o 'item' mais vendido nas categorias 'Livros' e 'Lazer'?
livro = mais_vendidos['Livros']
lazer = mais_vendidos['Lazer']
print('Livro: {}'.format(livro))
print('Lazer: {}'.format(lazer))

# Quanto foi vendido de 'Notebook Asus' e de 'iPad'?
notebookasus = vendas_tecnologia['Notebook Asus']
ipad = vendas_tecnologia['iPad']
print('Vendas de Notebook Asus: {} unidades'.format(notebookasus))
print('Vendas de iPad: {} unidades'.format(ipad))
