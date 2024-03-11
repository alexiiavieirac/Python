# Ordem dos Argumentos

"""
Estrutura:

-> Sempre os positionals arguments vêm antes e depois os keywwords arguments;
-> Semprre os argumentos individuais vêm antes e depois os 'múltiplos'.

def. minha_funcao(arg1, arg2, arg3, *args, k=kwarg1, k2=kwarg2, **kwargs):
    ...
"""


def minha_soma(*numeros, num1):
    soma = 0
    for numero in numeros:
        soma += numero
    soma += num1
    return soma


print(minha_soma(2, 5, 1, num1=5))
