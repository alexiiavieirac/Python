# Principalm aplicação de Lambda Expressions

# Usar lambda como argumento de alguma outra função, como map e filter.
preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000,
                    'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

# Map(): Pega uma tupla e aplica uma função para cada item da tupla.

# Queremos saber o preço de cada produto adicionando o valor do imposto de 30% sobre o valor do produto.
# Fazendo por function:


def calcular_preco(preco):
    return preco * 1.3


preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
print(preco_com_imposto)

# Fazendo por lambda:
preco_imposto = list(map(lambda preco: preco * 1.3, preco_tecnologia.values()))
print(preco_imposto)

# Filter(): Filtra um iterable (lista, dicionário etc).
# Estrutura: filter(função, iterable) -> retorna como resposta todos os itens do iterable onde a função é True.

# Queremos apenas os produtos que custam acima de 2000.

# Fazendo por function:


def maior2000(item):
    return item[1] > 2000


produtos_acima = dict(list(filter(maior2000, preco_tecnologia.items())))
print(produtos_acima)

# Fazendo por lambda:
maior_preco = dict(list(filter(lambda item: item[1] > 2000, preco_tecnologia.items())))
print(maior_preco)