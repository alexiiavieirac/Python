"""
Exercício: List Comprehension

1. Tirando informações de listas e dicionários
    Digamos que você está analisando as vendas de produtos de uma empresa de varejo.
    Essa lista tem: (produto, vendas de 2019, vendas de 2020) pra cada produto.
    Crie uma lista com as vendas de 2019.
"""

vendas_produtos = [('iPhone', 558147, 951642), ('Galaxy', 712350, 244295), ('iPad', 573823, 26964),
                   ('TV', 405252, 787604), ('Máquina de Café', 718654, 867660), ('Kindle', 531580, 78830),
                   ('Geladeira', 973139, 710331), ('Adega', 892292, 646016), ('Notebook Dell', 422760, 694913),
                   ('Notebook HP', 154753, 539704), ('Notebook Asus', 887061, 324831),
                   ('Microsoft Surface', 438508, 667179), ('Webcam', 237467, 295633),
                   ('Caixa de Som', 489705, 725316), ('Microfone', 328311, 644622), ('Câmera Canon', 591120, 994303)]

# Precisamos fazer um Unpacking, só que somente se forem tuplas:
lista_vendas2019 = [vendas2019 for produto, vendas2019, vendas2020 in vendas_produtos]
print(lista_vendas2019)

# Agora, qual o maior valor de vendas de 2019?
print(max(lista_vendas2019))

# E se eu quisesse descobrir o produto que mais vendeu em 2019? Temos duas formas de fazer, refazendo o list
# comprehension ou consultando a lista original.
lista_vendas_produtos2019 = [(vendas2019, produto) for produto, vendas2019, vendas2020 in vendas_produtos]
print(max(lista_vendas_produtos2019))

# Obs: foi proposital colocar o vendas2019 na frente, pois o max() olha primeiro o número.
