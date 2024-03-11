# Gerador de Senhas:

import string
import random

"""
Escreva um programa que gere uma senha aleatória com um determinado comprimento. A senha deve conter uma mistura de
letras, números e caracteres especiais. O comprimento da senha deve ser fornecido pelo usuário. Se o comprimento for
menor que 4, imprima uma mensagem de erro e peça ao usuário para fornecer um novo comprimento.

A senha deve ser aleatória, então cada vez que o usuário executar o programa, uma nova senha deve ser gerada.
Obrigatoriamente, a senha deve conter pelo menos uma letra, um número e um caractere especial. A senha não pode conter
espaços em branco.

O programa deve conter uma função chamada `gerar_senha` que recebe o comprimento da senha como parâmetro e retorna a
senha gerada. Se o comprimento for inválido, a função deve retornar None.

Exemplo de saída:
    Digite o comprimento da senha: 10
    8Zn$*2q9X

- Dica: use a biblioteca random e a função shuffle para embaralhar os caracteres da senha;
- Dica: use a função choice, dessa mesma biblioteca, para escolher um caractere aleatório de uma string;
- Dica: use a biblioteca string para obter uma lista de caracteres válidos para a senha.
"""

# "".join() -> Serve para juntar, então você pega uma lista e junta, um exemplo. E o "" serve para delimitar o que
# será passado para separar o que há dentro da lista.

print("Funções da biblioteca String:")
# Mostra todas as letras do alfabeto (maiúsculas e minúsculas):
print(string.ascii_letters)

# Mostra os dígitos (0 ao 9):
print(string.digits)

# Mostra todos os caracteres especiais:
print(string.punctuation)

print("-----------------------------------------------------------------------------")

print("Funções da biblioteca Random:")
# Random é basicamente números embaralhados e choice é escolha, então aparecerá um número qualquer (0 ao 9):
print(random.choice(string.digits))

# Choices, talvez podemos pedir mais números, pois nos retorna uma lista contendo strings:
print(random.choices(string.digits, k=10))

# Shuffle, serve para embaralhar uma lista que já tem caracteres definidos:
escolha = random.choices(string.digits, k=5)
print(escolha)
random.shuffle(escolha)
print(escolha)
print("-----------------------------------------------------------------------------")

# Estou juntando sem espaços todas as strings: letras, dígitos e pontuações:
possibilidades = "".join([string.ascii_letters, string.digits, string.punctuation])
print(possibilidades)

# Retorna uma lista com a quantidade de números que declare, no caso, k=3:
temporario = random.choices(possibilidades, k=3)
print(temporario)

# Append serve para adicionar um caractere em uma lista, por exemplo, mas se quisermos adicionar uma outra lista de
# caracteres, ele adicionará a lista e fará lista dentro de lista, ao invés de só adicionar o que estava dentro:
temporario.append("a")
print(temporario)

# Extend serve para adicionar uma lista de caracteres dentro de uma outra lista, mas não colocando a lista em si, mas
# sim, somente o que contém dentro da lista que queremos adicionar:
temporario.extend(["c", "d"])
print(temporario)

print("-----------------------------------------------------------------------------")

"""
Passo a passo de como fazer o código:

1º: Pedir ao usuário digitar o comprimento que terá sua respectiva senha.

2º: Definir uma função para gerar a senha:
    2.1: Fazer a validação se caso a senha for menor do que o tamanho minímo, no caso, 4 dígitos:
        2.1.1: Se for menor mostrar uma mensagem de erro.
        
    2.2: Se caso for maior que 4 dígitos, deveremos fazer:
        2.2.1: A variável senha, será igual a uma lista onde deverá conter o que precisaremos utilizar, como os métodos
               random.choice para letters, digits e punctuation, assim conseguiremos pegar quais caracteres usaremos.
               senha = [random.choice(string.ascii_letters), random.choice(string.digits), 
               random.choice(string.punctuation)]
               
        2.2.2: Nos retornará uma lista de caracteres que precisamos, e para tirarmos da lista e colocarmos em uma única
               string, podemos utilizar o método "".join(), que serve para juntar uma lista.
               possibilidades = "".join([string.ascii_letters, string.digits, string.punctuation])
               
        2.2.3: Como temos somente 3 dígitos colocados na lista de senha, devemos fazer com que o programa entenda a 
               quantidade de números para a senha que o usuário deseja, então podemos pegar o método extend, que serve
               para adicionar mais elementos conforme o número escolhido de tamanho pelo usuário, mas lembrando que 
               temos 3 caracteres definidos (letters, digits e punctuation), então devemos pegar o tamanho que o 
               usuário escolheu e tirar a quantidade de caracteres já definidos, no caso, tamanho-3.
               senha.extend(random.choices(possibilidade, k=tamanho-3))
               
        2.2.4: Para que a senha gerada não seja um único padrão de visualização, sendo letters, digits e punctuation,
               podemos utilizar o método random.shuffle() para fazer com que a senha embaralhe após ser gerada.
               random.shuffle(senha)
               
        2.2.5: Por fim, podemos retornar um "".join(senha), fazendo com que não retorne uma lista, mas sim uma string.
        
3º: Chamar a função de gerar senha e mostrar o resultado para o usuário.
"""


def gerar_senha(tamanho):
    if tamanho < 4:
        print("O tamanho da senha deve ser maior que 4. Tente novamente.")
    else:
        senha = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        possibilidade = "".join([string.ascii_letters, string.digits, string.punctuation])
        senha.extend(random.choices(possibilidade, k=tamanho-3))

        random.shuffle(senha)

        return "".join(senha)


tamanho = int(input("Digite o comprimento da senha: "))
print(gerar_senha(tamanho))
