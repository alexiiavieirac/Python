# Adicionar, remover e modificar itens no dicionário

# Adicionar itens:
# dicionario = {}
# dicionario[chave] = valor -> Pegar e adicionar os valores. (Nessa chave coloque esse valor, e é mais útil quando são poucos valores para atribuir)
# Ou:
# dicionario.update({chave: valor, chave: valor}) -> Mais útil quando são dois valores ou mais para ser atribuídos.

lucro_1tri = {'Janeiro': 100000, 'Fevereiro': 120000, 'Março': 90000}
lucro_2tri = {'Abril': 88000, 'Maio': 89000, 'Junho': 120000}

# Adicionando um 'item':
print(lucro_1tri)
# lucro_1tri['Abril'] = 88000
# print(lucro_1tri)

# Adicionando vários 'itens' ou um dicionário a outro:
# Está atualizando o dicionário do lucro_1tri para um novo, que seria os dois dicionários juntos:
lucro_1tri.update(lucro_2tri)
# Podemos fazer dessa forma, ou assim: lucro_1tri.update({'Abril': 88000, 'Maio': 89000, 'Junho': 120000})
print(lucro_1tri)

# Adicionando um 'item' já existente (manualmente ou pelo 'update'):
# OBS: só pode existir apenas uma chave com valores diferentes.
lucro_1tri['Janeiro'] = 88000
# lucro_1tri.update({'Janeiro': 88000})
print(lucro_1tri)

# Para modificar, basta adicionarmos um valor a uma chave já existente, pois só podemos ter uma chave com valores diversos na mesma.

# Modificar:
lucro_fev = 85000

lucro_1tri['Fevereiro'] = lucro_fev
print(lucro_1tri)

# Remover:

# del dicionario[chave] -> OBS: del dicionario é diferente de dicionario.clear()
# Ou
# valor = dicionario.pop(chave)

armazenar_junho = lucro_1tri.pop('Junho')
# del lucro_1tri['Junho']
print(lucro_1tri)
print(armazenar_junho)

# O Clear limpa o dicionário inteiro:
lucro_1tri.clear()
print(lucro_1tri)

# Del pode ser usado para listas, mas com o índice:
funcionarios = ['Aléxia', 'Vieira', 'Coelho', 'Iris', 'Tamasiro']
del funcionarios[0]
print(funcionarios)
