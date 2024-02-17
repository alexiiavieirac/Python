# 1. Análise de Vendas

# Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
# Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870)
]

# for 'item' in vendas:
# nome, meta_vendas = 'item'
for vendedor, qtde in vendas:
    if qtde >= meta:
        print('Nome: {} / Venda: {}'.format(vendedor, qtde))

print('----------------------------------------------------------------')

# 2. Comparação com Ano Anterior

# Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019,
# para reportar isso para a diretoria.
# A sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

# Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)
# A lógica da tupla é: (produto, vendas2019, vendas2020)

vendas_produtos = [
    ('iPhone', 558147, 951642),
    ('Galaxy', 712350, 244295),
    ('iPad', 573823, 26964),
    ('TV', 405252, 787604),
    ('Máquina de Café', 718654, 867660),
    ('Kindle', 531580, 78830),
    ('Geladeira', 973139, 710331),
    ('Adega', 892292, 646016),
    ('Notebook Dell', 422760, 694913),
    ('Notebook HP', 154753, 539704),
    ('Notebook Asus', 887061, 324831),
    ('Microsoft Surface', 438508, 667179),
    ('Webcam', 237467, 295633),
    ('Caixa de Som', 489705, 725316),
    ('Microfone', 328311, 644622),
    ('Câmera Canon', 591120, 994303)
]

for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020 / vendas2019 - 1
        print('Produto: {}'.format(produto))
        print('Vendas 2019: {}'.format(vendas2019))
        print('Vendas 2020: {}'.format(vendas2020))
        print('Crescimento: {:.1%}'.format(crescimento))
        print('-------------------------')
