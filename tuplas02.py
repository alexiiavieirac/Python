vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for item in enumerate(vendas):
    i, venda = item
    print(i)
    print(venda)
    # print('{} vendeu {} unidades.'.format(funcionarios[i], venda))
