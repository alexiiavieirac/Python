vendas = [
    ('20/08/2020', 'iPhone X', 'Azul', '128GB', 350, 4000),
    ('20/08/2020', 'iPhone X', 'Prata', '128GB', 1500, 4000),
    ('20/08/2020', 'iPad', 'Prata', '256GB', 127, 6000),
    ('20/08/2020', 'iPad', 'Prata', '128GB', 98, 5000),
    ('21/08/2020', 'iPhone X', 'Azul', '128GB', 397, 4000),
    ('21/08/2020', 'iPhone X', 'Prata', '128GB', 1017, 4000),
    ('21/08/2020', 'iPad', 'Prata', '256GB', 50, 6000),
    ('21/08/2020', 'iPad', 'Prata', '128GB', 4000, 5000)
]

# Qual foi o fatuamento de iPhone no dia 20/08/2020?

faturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidade, valor_unitario = item #O item é cada valor da tupla.
    if produto == 'iPhone X' and data == '20/08/2020':
        faturamento += unidade * valor_unitario

print(f'Faturamento: R${faturamento}')

print('----------------------------------------------------------------')

# Qual foi o produto mais vendida (em unidades) no dia 21/08/2020?

produto_mais_vendido = ''
qtde_produto_mais_vendido = 0
cor_produto_mais_vendido = ''
capacidade_produto_mais_vendido = ''

for item in vendas:
    data, produto, cor, capacidade, unidade, valor_unitario = item
    if data == '21/08/2020':
        if unidade > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidade
            cor_produto_mais_vendido = cor
            capacidade_produto_mais_vendido = capacidade

print('Informação do Produto mais vendido no dia 21/08/2020:')
print('Produto: {}'.format(produto_mais_vendido))
print('Quantidade: {}'.format(qtde_produto_mais_vendido))
print('Cor: {}'.format(cor_produto_mais_vendido))
print('Capacidade: {}'.format(capacidade_produto_mais_vendido))
