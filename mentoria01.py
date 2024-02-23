# 23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00
# ou em galões de 3,6 litros, que custam R$25,00.

"""
Informe ao usuário as quantidades de tinta a serem compradas e os respetivos preços em 3 situações:

Dica1: lembre dos operadores // e % mostrados em exercícios anteriores
Dica2: numero // 10 vai dar como resposta a parte inteira da divisão do número por 10.
Dica3: numero % 10 vai dar o resto da divisão do número por 10.
"""

# 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)

"""
# Calcular quantas latas e quanto custa comprar a tinta
    # Descobrir a área que será pintada
    # Calcular a quantidade de litros de tinta que iremos usar (area / 6)
    # Saber quantas latas irei utilizar 
        # Calcular quantas latas (litros / 18)
        # Se der um número 'quebrado' de latas, faça:
            # Adicione 1 lata
        # Caso contrário
            # De a quantidade de latas
    # Calcular o preço das latas (latas * 80)
"""


def pegar_area_usuario():
    area1 = int(input('Área em metros quadrados a ser pintada: '))
    return area1


def calcular_litros_precisam(area1):
    litros1 = area1 / 6
    return litros1


def calcular_latas(litros1):
    latas1 = litros1 / 18
    if int(latas1) != latas1:
        latas1 = int(latas1) + 1
    return latas1


def calcular_preco(latas1):
    preco1 = latas1 * 80
    return preco1


area1 = pegar_area_usuario()
litros1 = calcular_litros_precisam(area1)
latas1 = calcular_latas(litros1)
preco1 = calcular_preco(latas1)


print(f'Latas: {latas1}')
print(f'Preço: R${preco1}')

print('--------------------------------------------------------')

# 2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)

"""
# Calcular a quantidade de galões que utilizaremos para pintar uma parede
    # Descobrir a área a ser pintada
    # Calcular a quantidade de litros que iremos utilizar (area / 6)
    # Saber a quantidade de galões que precisaremos utilizar (arredondando para cima)
        # Calcular quantos galões por divisão inteira (litros % 3.6)
        # Caso não seja:
            # Galões = int(litros / 3.6) + 1
        # Se não:
            # Galões = litros / 3.6
    # Calcular o preço dos galões (galões * 25)
"""

area2 = int(input('Área em metros quadrados a ser pintada: '))
litros2 = area2 / 6

if litros2 % 3.6 > 0:
    galoes2 = int(litros2 / 3.6) + 1
else:
    galoes2 = litros2 / 3.6

preco2 = galoes2 * 25

print(f'Galões: {galoes2}')
print(f'Preço: R${preco2}')

print('--------------------------------------------------------')

"""
# Calcular o menor preço possível de latas e galões para pintar uma parede
    # Descobrir a áres em metros quadrados que será pintada
    # Calcular a quantidade de litros que será utilizada (área / 6)
    # Vê quantas latas e galões irá precisar
        # Calcular quantas latas inteiras vamos usar
        # Quanto sobrara de litros de tinta
        # Se sobrar tinta:
            # Quantos galões precisaremos para a sobra
    # Calcular o preço
        # Quantidade de latas inteiras * 80
        # Se quantidade de galões * 25 > do que mais uma lata inteira que custa 80:
            # Preço anterior + 80
        # Caso contrário
            # Preço anterior + quantidade de galões * 25
"""
# A variável latas e galões está sendo iniciada aqui em cima, pois a variável galões está somente sendo criada quando falta algum litro, caso não falte, dará erro.
# Latas = 0
galoes = 0

area = int(input('Área em metros quadrados a ser pintada: '))

litros = area / 6

latas = int(litros / 18)

litros_faltam = litros % 18

if litros_faltam > 0:
    if litros_faltam % 3.6 > 0:
        galoes = int(litros_faltam / 3.6) + 1
    else:
        galoes = litros_faltam / 3.6

preco_latas = latas * 80
preco_galoes = galoes * 25

if preco_galoes > 80:
    latas = latas + 1
    preco_latas = latas * 80
    galoes = 0
    preco_galoes = 0

preco_final = preco_galoes + preco_latas

print(f'Latas: {latas}')
print(f'Galões: {galoes}')
print(f'Preço Final: R${preco_final}')

print('--------------------------------------------------------')

"""
Exercício feito em outro módulo e aula.

# Enviar um relatório com as vendas do dia anterior para o meu chefe as 9h da manhã
    # Pegar uma base de dados com as vendas do dia anterior
        # Entrar no sistema
        # Navegar até o local da base de dados
        # Exportar a base de dados
    # Calcular as vendas do dia anterior
        # Importar a base de dados para o Python
        # Consolidar as vendas
        # Calcular o indicador de vendas
    # Enviar um e-mail para o meu chefe
        # Entrar no e-mail
            # Abrir o navegador
            # Digitar gmai.com na barra de navegação
            # Dar enter
        # Criar um novo e-mail
            # Clicar no botão novo e-mail 
        # Preencher com as informações de vendas
        # Enviar o e-mail
"""
