import string
from collections import Counter

"""
Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras
(independentemente se há repetição ou não), a quantidade de cada palavra e a quantidade de cada letra. Ignore
maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas). Faça o devido tratamento para
pontuação e espaços ao contar palavras.

O programa deve conter uma função chamada analisar_texto que recebe o texto como parâmetro e retorna a contagem de
palavras, a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada.

Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:
Contagem de palavras: 8
Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2,
'd': 1, 'é': 1, 'v': 1, 'a': 1})

Dica: Use o módulo string para obter uma lista de caracteres de pontuação. Exemplo:
import string
print(string.punctuation)

Dica: Use o módulo collections para obter um contador de palavras e letras. Exemplo:
from collections import Counter
print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
print(Counter('abacba'))
"""

"""
# Mostra as pontuações:
print(string.punctuation)

# Mostra todas as letras (maiúsculas e minúsculas):
print(string.ascii_letters)

# Mostra somente letras minúsculas:
print(string.ascii_lowercase)

# Mostra somente letras maiúsculas:
print(string.ascii_uppercase)

# Mostra somente os números (0 ao 9):
print(string.digits)
"""

"""
Faz a contagem das letras que existam, independentemente se são strings ou listas:
print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
print(Counter('abacba'))
"""

# Solução simples:


def analisar_texto(texto):
    """
    Analisa o texto fornecido e calcula a contagem de palavras, a frequência de palavras e
    frequência de letras.

    :parameter
    texto: str
        Texto a ser analisado

    :returns
    tuple
        Contagem de palavras, frequência de palavras e frequência de letras
    """

    # Retirar os pontos:
    tratamento = str.maketrans("", "", string.punctuation)
    texto_tratado = texto.translate(tratamento)

    # Para 'cortar' por palavras e espaçamentos a frase:
    palavras = texto_tratado.split()

    # Para contar o comprimento da frase:
    contagem_palavras = len(palavras)

    # Quantidade de vezes que aparecem as palavras em nosso código:
    frequencia_palavras = Counter(palavras)

    # Quantidade de letras utilizadas:
    frequencia_letras = Counter(texto_tratado.lower())

    return contagem_palavras, frequencia_palavras, frequencia_letras


texto = "Olá mundo! Este é um teste. Olá novamente."

contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")

"""
str.maketrans() -> Ele transforma o que precisamos, no caso, transformou as vogais em números:
1ª: Principal variável | 2ª: Qual queremos mudar | 3ª: Qual queremos remover (talvez)

vogais = "aeiou"
numeros = "12345"
remover = "a"

guia_troca = str.maketrans(vogais, numeros, remover)
print(guia_troca)

Resultado: {97: None, 101: 50, 105: 51, 111: 52, 117: 53}
Está "none", pois eu removi o a.


letras_minusculas = string.ascii_lowercase

print(letras_minusculas.translate(guia_troca))

Resultado: bcdd2fgh3jklmn4pqrst5vwxyz
Possui números, pois eu pedi para modificar as vogais em números.
"""

