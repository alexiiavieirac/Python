"""
Exercício 1

Crie um sistema de cadastro de produtos em uma lista de produtos.
Seu sistema deve:
- Pegar o usuário qual produto vai ser cadastrado por meio de um input;
- Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto;
- Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente";
- Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa.
"""

produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# Perguntar para o cliente o produto que ele deseja cadastrar:
novoProd = input("Digite o prodruto para cadastrar: ")
# Colocar a primeira letra do produto cadastrado em letra minúscula:
novoProd = novoProd.lower()

# Essa verificação serve para ver se existe o nome do novo produto dentro da lista de produtos que eu tinha anteriormente, se tiver produto repetido uma mensagem aparecerá, caso contrário
# ele colocará o nome do produto que foi cadastrado com sucesso, adicionará o produto a lista com o comando .append() e mostrará a lita com o produto que foi adicionado:
if novoProd in produtos:
    print("Produto já existe na lista, tente novamente.")
else:
    print("Produto {} adicionado com sucesso.".format(novoProd))
    produtos.append(novoProd)
    print(produtos)

""" 
Exercício 2

Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto;
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta:
       - Ex: O produto celular custa R$1500.
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente.
"""

precos = [1500, 1000, 800, 2000]

# Perguntaremos qual o produto que deseja consultar:
nomeProd = input("Informe o nome do produto: ")
# Colocar a primeira letra do produto consultado em letra minúscula:
nomeProd = nomeProd.lower()

# Pergutaremos qual o valor do preço do produto que foi cadastro e procurado:
valorProd = input("Informe o valor do produto: R$")
# Serve para adicionar o novo preço do produto na lista de preços que foi feita anteriormente:
precos.append(valorProd)

# Essa verificação serve para ver o novo produto cadastrado dentro da lista de produtos, e se for verdade, pegaremos o índice do produto que adicionamos/procuramos e assim
# pegaremos a lista do preço e procuraremos qual é o índice referente ao produto que anteriormente procuramos, no fim, mostraremos o nome do produto e o preço, caso não esteja certo, mostraremos a mensagem de erro:
if nomeProd in produtos:
    i = produtos.index(nomeProd)
    preco = precos[i]
    print("Produto: {} | Preço: R${}".format(nomeProd, preco))
else:
    print("Produto não existe no sistema.")

""" 
Exercício 3

Crie um sistema de consulta de bônus dos funcionários
Seu sistema deve conter:
- Pegar o valor de vendas do funcinoário por meio de um input
- Calcular o bônus do funcionário de acordo com a seguinte regra:
      - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida;
      - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000;
      - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus.
- Printar no final o valor do bônus do funcionário.
"""

# Perguntaremos ao funcionário quantas vendas que ele fez:
vendas = float(input("Quantidaes vendidas: "))

# Essa verificação serve para ver se o funcionário vendeu a quantidade que era desejado. Caso fosse maior que 1000, seu bônus seria a quantidade de vendas vezes 2;
# Caso excedesse 5000 vendas, seu bônus seria a quantidade de vendas vezes 2, adicionado com um preço fixo, que é 1000;
# Por fim, se vendesse menos que 1000, não receberia bonificação:
if vendas > 1000:
    bonus = vendas * 2
elif vendas > 5000:
    bonus = vendas * 2 + 1000
else:
    bonus = 0

print("Bônus do funcionário: {}".format(bonus))

""" 
Exercício 4

Crie um programa que consiga descobrir qual dos vendedores vendeu mais.
As vendas dos vendedores são listas com a quantidade vendida por cada vendedor.
"""

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]

vendas_vendedor1 = sum(vendas[0])
vendas_vendedor2 = sum(vendas[1])

if vendas_vendedor1 > vendas_vendedor2:
    print("Vendedor 1 vendeu mais.")
else:
    print("Vendedor 2 vendeu mais.")
