# Exercícios

# 1. Exercício 'menos prático' para treinar manipulação de dicionário
# Dessa vez, vamos apenas treinar a manipulação de dicionário. Transforme as listas abaixo num único dicionáiro no formato:

# dicionário = {
#   produto: (vendas2019, vendas2020),
#   produto2: (vendas2019, vendas2020),
#   produto3: (vendas2019, vendas2020) }

# Apesar de parecer 'menos prático' esse é um procedimento que precisamos acostumar-nos a fazer, visto que algumas funções precisam de dicionários para funcionar e saber
# transformar listas em dicionários é uma habilidade muito útil.

# Obs.: Lembre do zip para juntas listas.
# Obs.: Repare que cada ‘item’ das vendas é, na verdade, uma lista. Então é provável que precise fazer esse código em 2 etapas.

produtos = ['iPhone', 'Galaxy', 'iPad', 'TV', 'Máquina de Café', 'Kindle', 'Geladeira', 'Adega', 'Notebook Dell', 'Notebook HP', 'Notebook Asus', 'Microsoft Surface', 'Webcam', 'Caixa de Som', 'Microfone', 'Câmera Canon']
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

# Zip para juntar duas listas e list para colocar a junção do zip para uma lista que possamos ver:
vendas = list(zip(vendas2019, vendas2020))
print(vendas)

# Usamos o dict para transformarmos a lista zipada num dicionário:
vendas_produtos = dict(zip(produtos, vendas))
print(vendas_produtos)

print('-------------------------------------------------------------------')

# EXERCÍCIOS EXTRAS:

# Exercício 1

# Crie um sistema de consulta de preços.
# O seu sistema deve:
# — Pedir para o usuário o nome de um produto;
# — Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta;
# — Ex: O produto celular custa R$1500;
# — Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente.

print('Exercício 1:')

precos1 = {"Celular": 1500, "Camera": 1000, "Fone de Ouvido": 800, "Monitor": 2000}

produto_procurado = input('Produto procurado: ')
# produto_procurado = produto_procurado.lower()

if produto_procurado in precos1:
    precos01 = precos1[produto_procurado]
    print(f'Produto: {produto_procurado} / Preço: R${precos01}')
else:
    print('Não há nenhum produto com esse nome. Tente novamente.')

print('-------------------------------------------------------------------')

# Exercício 2

# Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto.
# Se ele responder sim, o programa deve pedir o nome do produto e o preço do produto e cadastrar no dicionário de preços.
# Em seguida do cadastro bem-sucedido, o programa deve printar o dicionário de precos atualizado.

print('Exercício 2:')

precos = {"Celular": 1500, "Camera": 1000, "Fone de Ouvido": 800, "Monitor": 2000}

produto_procurado = input('Produto procurado: ')

if produto_procurado in precos:
    preco = precos[produto_procurado]
    print(f'Produto: {produto_procurado} / Preços: R${preco}')
else:
    opcao = input(f'Quer cadastrar o produto {produto_procurado}? (S/N) ')
    if opcao.lower() == 's':
        preco = input(f'Preço do {produto_procurado}: R$')
        precos[produto_procurado] = preco
        print(precos)
    else:
        print('Não há nenhum produto com esse nome. Tente novamente.')

print('-------------------------------------------------------------------')

# Exercício 3

# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos.
# Calcule o novo valor dos produtos com base nas seguintes regras:
# — Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço serão 110% do preço atual);
# — Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%;
# — Preços acima de 2.000 vão ter reajuste de 20%.

print('Exercício 3:')

precos2 = {"Celular": 1500, "Camera": 1000, "Fone de Ouvido": 800, "Monitor": 3000}

for produtos in precos2:
    preco_produto = precos2[produtos]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f'Produto: {produtos} / Novo preço: R${novo_preco:.2f}')

print('-------------------------------------------------------------------')

# Exercício 4

# — Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços.
# — Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final.

print('Exercício 4:')

precos2 = {"Celular": 1500, "Camera": 1000, "Fone de Ouvido": 800, "Monitor": 3000}
novos_precos = {}

for produtos in precos2:
    preco_produto = precos2[produtos]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f'Produtos: {produtos} / Novo preço: R${novo_preco:.2f}')
    novos_precos[produtos] = novo_preco

total_antigo = sum(precos2.values())
total_novo = sum(novos_precos.values())
reajuste = total_novo - total_antigo

print(f'O reajuste foi de R${reajuste:.2f}')

print('-------------------------------------------------------------------')

# Exercício 5

# — Uma empresa está analisando os resultados de vendas do 1.º semestre de 2022 e 2023.
# — Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
# — Após calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022.

print('Exercício 5:')

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    print(f'Em {mes}, a variação percentual foi de: {percentual:.1%}')

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 - total_22

print(f'Crescimento Real: {crescimento:.1f}')

print('-------------------------------------------------------------------')

# Exercício 6

# No final da reunião de apresentação dos números, o seu chefe perguntou:
# — E se nos meses de 2023 que nós vendemos menos do que 2022 nós tivéssemos pelo menos empatado com 2022 (ou seja, se nos meses de
# 2023 em que as vendas foram menores que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022).
# — Qual teria sido o nosso crescimento de 2023 frente a 2022?

print('Exercício 6:')

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    if percentual < 0:
        vendas_23[mes] = valor_22
    print(f'Em {mes}, a variação percentual foi de: {percentual:.1f}')

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 - total_22

print(f'Crescimento Real: {crescimento:.1f}')
