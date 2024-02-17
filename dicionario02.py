mais_vendidos = {'Tecnologia': 'iPhone', 'Refrigeracao': 'Ar Consul 12000 btu', 'Livros': 'O Alquimista', 'Eletrodoméstico': 'Geladeira', 'Lazer': 'Prancha Surf'}
vendas_tecnologia = {'iPhone': 15000, 'Samsung Galaxy': 12000, 'TV Samsung': 10000, 'PS5': 14300, 'Tablet': 1720, 'iPad': 1000, 'TV Philco': 2500, 'Notebook HP': 1000, 'Notebook Dell': 17000, 'Notebook Asus': 2450}

# Qual foi o 'item' mais vendido nas categorias 'Livros' e 'Lazer'?
# Com a chave:
print('livro: {}'.format(mais_vendidos['Livros']))
print('Lazer: {}'.format(mais_vendidos['Lazer']))

# Quanto foi vendido de 'Notebook Asus' e de 'iPad'?
# Com o .get():
print('Vendas de Notebook Asus: {} unidades'.format(vendas_tecnologia.get('Notebook Asus')))
print('Vendas de iPad: {} unidades'.format(vendas_tecnologia.get('iPad')))

# Verificar se 'item' está no dicionário:
# if 'Copo' in vendas_tecnologia:
#    print(vendas_tecnologia['Copo'])
# else:
#    print('Copo não está na lista de produtos de tecnologia.')

# Segunda forma de fazer:
# Se retornar 'None', ele não encontrou.
if vendas_tecnologia.get('Copo') == None:
    print('Copo não está dentro da lista de produtos de tecnologia.')
else:
    print(vendas_tecnologia.get('Copo'))
