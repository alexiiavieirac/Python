# Exercícios

"""
1. Criando um Registro de Hóspedes
    Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas.
    Seu sistema deve conseguir:

    1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de um input);
    2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o CPF e o nome de cada pessoa, a fim de registrá-la no quarto
        (2 inputs para cada pessoa, 1 para o CPF e outro para o nome);
    3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o CPF da pessoa, assim:
"""

qtde_pessoas = int(input("Quantidade de pessoas que ficarão hospedadas: "))
quarto = []

for i in range(qtde_pessoas):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    hospedes = ["Nome: {} | CPF: {}".format(nome, cpf)]
    quarto.append(hospedes)

print(quarto)

print("______________________________________________________________________________________________________________")

"""
2. Análise de Vendas
    Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
    
    Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que venderam.
"""

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870]
]

for item in vendas:
    if item[1] >= meta:
        print("Vendedor {} bateu a meta. Fez {} vendas.".format(item[0], item[1]))

print("______________________________________________________________________________________________________________")

"""
3. Comparação com o Ano Anterior
    Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019,
    para reportar isso para a diretoria.
    
    Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.
    
    Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020 / vendas_produto2019 - 1)
    
    Dica: Lembre do enumerate, ele pode facilitar seu "For"
"""

produtos = ['iPhone', 'Galaxy', 'iPad', 'TV', 'Máquina de Café', 'Kindle', 'Geladeira', 'Adega', 'Notebook Dell', 'Notebook HP', 'Notebook ASUS', 'Microsoft Surface', 'Webcam', 'Caixa de Som', 'Microfone', 'Câmera Canon']
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print("Produto: {} | Venda 2019: R${:,} | Venda 2020: R${:,} | Porcentagem de Crescimento: {:.1%}".format(produto, vendas2019[i], vendas2020[i], crescimento))
