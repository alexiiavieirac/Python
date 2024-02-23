# Docstring e Annotations

# Estrutura — São ferramentas para organização:

# Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função e também pode ser que precisemos usar essa mesma função
# semana, meses ou até anos depois da sua criação.

# Docstring → diz o que a função faz, quais valores ela tem como argumento e o que significa cada valor;
# Annotations → diz quais devem os argumentos e o que a função retornará.

# Docstring:


# def. minha_funçao(arg1, arg2, ...):
#    ''' O que a função faz

#    Parameters:
#        arg1 (int.): o que é o argumento 1;
#        arg2 (str): o que é o argumento 2;
#        ...

#    Returns:
#        texto (str): o que a função retorna como resposta
#    '''
# código da função


def minha_soma(num1, num2, num3):
    """ Faz a soma de 3 númerros inteiros e devolve como resposta um número inteiro

    Parameters:
        num1 (int): primeiro número a ser somado
        num2 (int.): segundo número a ser somado
        num3 (int.): terceiro número a ser somado

    Returns:
        soma (int.): o valor da soma dos 3 núemros dados como argumento
    """
    return num1 + num2 + num3


# Annotations:

# def. minha_funcao(arg1: isso, arg2: aquilo) -> o que a função retorna:
#   ...
#   return ...

def minha_sum(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3
