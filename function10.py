# Try e Except

# Como 'testas' erros e tratar exceções:

"""
try:
    o que eu quero tentar fazer
except:
    o que eu vou fazer caso dê erro
"""


def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
    except:
        raise ValueError('E-mail digitado não tem o @, digite novamente.')
    else:
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado' 


email = input('Digite seu e-mail: ')
print(descobrir_servidor(email))

# Como 'printar' um erro em uma function

"""
raise Exception('O erro foi esse')
ou então avisando qual o tippo de erro que teve:
raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse') 
"""

"""
try:
    tente fazer isso.
except ErroEspecifico:
    deu esse erro aqui que era esperado.
except ValurErro:
    deu esse erro.
else:
    caso não dê o erro esperado, rode isso.
finally: (menos utilizado)
    independente do que acontecer, faça isso.
"""

# Passo 1 → mostrar o erro de faturamento — custo se a pessoa digitar texto.
# Passo 2 → colocar um except para trrata o ValueError
# Passo 3 → usar um else paa exibir o print(lucro) e mostrar a diferença que seria de colocar o print(lucro dentor do try)
#            caso o print(lucro levantasse um ValueError, ele ia pula rpara o except também), então muitas vezes é melhor isolar algo

custo = 500
faturamento = input('Faturamento da loja de hoje: R$')

try:
    lucro = int(faturamento) - int(custo)
    print(lucro, int('lucro 500'))
except ValueError:
    print('Coloque apenas o valor do faturamento, sem texto nenhum, apenas números.')
