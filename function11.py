# Quantidade Indefinidas de Argumentos:

# Utilidade:
# Quando quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

"""
Estrutura:

*args parra positional arguments → agumentos vêm em formato de tupla

Def. minha_funcao(*agrrs):
    ...

**kwargs parar keyword arguments → argumentos vêm em formato de dicionário

Def. minha_funcao(**kwwargs):
    ...
"""


def soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


print(soma(10, 20, 30, 40, 50, 60, 70, 80, 90))


def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco


print(preco_final(1000, desconto=0.1, garantia_extra=100, imposto=0.3))
