# Lambda Expressions

"""
Objetivo:
    -> As lambdas expressions são funções anônimas (sem nome) que tem uma linha de código e são atribuidas a uma
       variável, como se a variável virasse uma função;
    -> Elas normalmente são usadas para fazer uma única ação, mas em Python usamos, principalmente, dentro de métodos
       como argumento, para não precisarmos criar uma função só para isso;
    -> Outra aplicação deles está em criar um "gerador de funções".

Obs.: Não é obrigatório utilizá-la, até porque tudo que fazemos com ela, fazemos com funções normais. Mas, é importante
      saber entender quando encontrar e saber usar a medida que você for se acostumando e vendo necessidade.

Estrutura:
    minha_fun~]ap = lambda parametro: expressao
"""

# Exemplo mais simples:


"""
def minha_funcao(num):
    return num * 2


print(minha_funcao(5))
"""

numero = lambda num: num * 2
print(numero(5))

# Exemplo útil: Vamos usar lambda expressions para criar uma função que calcula o preço dos produtos acrescido do
# imposto.
imposto = 0.3


def preco_imposto(preco):
    return preco * (1 + 0.3)


preco_imposto2 = lambda preco: preco * (1 + imposto)
print(preco_imposto2(100))