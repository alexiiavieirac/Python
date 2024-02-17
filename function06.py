# Valores padrões para os argumentos

# Estrutura
# Nesse caso, não é obrigatório a passar o valor para usar a função, pode usar o valor padrão.

# def minha_funcao(argumento = valor_padrao):
#   ...
#   return ...

# Como vimos, o sort() paar listas tem um argumento padrão. O reverse=False é padrão, então a ordem é crescente. Caso o usuário queira fazer em ordem decrescente, o reverse fica igual a True.

produtos = ['Apple TV', 'Mac', 'iPhone X', 'iPad', 'Apple Watch', 'Mac Book', 'Airpods']

produtos.sort()
print(produtos)

produtos.sort(reverse=True)
print(produtos)

# Vamos criar uma função que padronize códigos de produtos. O 'default' será padronizar os códigos para letras minúsculas (dado por 'm'), mas se o usuário quiser pode padronizar maiúscula, dado por M.

print('--------------------------------------')


def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


cod_produtos = ['  ABC12  ', 'abc34', 'AbC56']
print(padronizar_codigos(cod_produtos, 'm'))

print('--------------------------------------')

lista = [10, 20, 30]

for item2 in lista:
    item2 += 5
    lista[0] = item2

print(lista)
