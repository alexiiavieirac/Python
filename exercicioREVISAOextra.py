# Exercícios de revisão extras

"""
A seguir, encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos, por exemplo, práticos da realidade:

— Lista de compras;
— Previsão de vendas;
— Relatório de vendas;
— Segmentação de clientes;
— Analisador de texto.

Para cada assunto, encontrará ao menos um exercício. Nos casos onde há mais de um exercício para o mesmo assunto,
será convidado a resolver o mesmo problema de formas diferentes. Isso é proposital, pois o objetivo é que pratique
o que aprendeu e, em simultâneo, aprenda novas formas de resolver um mesmo problema. Por exemplo, usando diferentes
estruturas de dados, ou diferentes formas de iterar sobre uma estrutura de dados, ou, ainda, utilizando funções.

Tente resolver os exercícios sozinho. Se tiver dificuldades, consulte o material do curso e, se ainda assim não conseguir resolver, consulte a solução.
"""

print('Primeira Versão: Lista de Compras')

"""
            Lista de compras

** Primeira versão da lista de compras

Escreva um programa que permita que um usuário crie uma lista de compras.
O usuário deve conseguir adicionar itens, remover itens e visualizar a lista.

Estruture o seu programa da seguinte forma:

1. Crie uma lista vazia para armazenar os itens da lista de compras.
2. Crie um “loop” infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
3. No “loop”, use uma declaração if para executar a tarefa apropriada conforme a escolha do usuário.
4. Se o usuário escolher adicionar um “item”, solicite que ele digite o nome do ‘item’ e adicione-o à lista.
5. Se o usuário escolher remover um “item”, solicite que ele digite o nome do ‘item’ e remova-o da lista.
6. Se o usuário escolher ver a lista, mostre cada ‘item’ da lista na sua própria linha.
7. Se o usuário escolher sair, encerre o “loop” usando break.

Exemplo de saída:

1. Adicionar ‘item’;
2. Remover ‘item’;
3. Ver lista;
4. Sair;
Escolha uma opção: 1;
Digite um ‘item’: banana.

1. Adicionar ‘item’;
2. Remover ‘item’;
3. Ver lista;
4. Sair;
Escolha uma opção: 1;
Digite um ‘item’: maçã.

1. Adicionar ‘item’;
2. Remover ‘item’;
3. Ver lista;
4. Sair;
Escolha uma opção: 3;
['banana', 'maçã'].

1. Adicionar ‘item’;
2. Remover ‘item’;
3. Ver lista;
4. Sair;
Escolha uma opção: 2;
Digite um ‘item’: banana.

1. Adicionar 'item';
2. Remover ‘item’;
3. Ver lista;
4. Sair;
Escolha uma opção: 3;
['maçã'].

1. Adicionar 'item';
2. Remover 'item';
3. Ver lista;
4. Sair;
Escolha uma opção: 4.
"""

# 1. Crie uma lista vazia para armazenar os itens da lista de compras;
# 2. Crie um “loop” infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção;
# 3. No “loop”, use uma declaração if para executar a tarefa apropriada conforme a escolha do usuário;
# 4. Se o usuário escolher adicionar um “item”, solicite que ele digite o nome do ‘item’ e adicione-o à lista;
# 5. Se o usuário escolher remover um “item”, solicite que ele digite o nome do ‘item’ e remova-o da lista;
# 6. Se o usuário escolher ver a lista, mostre cada ‘item’ da lista na sua própria linha;
# 7. Se o usuário escolher sair, encerre o “loop” usando break.

listas_compras = []

while True:
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Ver lista')
    print('4. Sair')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        item = input('Nome do Item: ')
        listas_compras.append(item)
    elif escolha == '2':
        item = input('Nome do Item: ')
        if item in listas_compras:
            listas_compras.remove(item)
    elif escolha == '3':
        print(listas_compras)
    elif escolha == '4':
        break

print('Segunda Versão: Lista de Compras')

"""
Segunda versão da lista de compras

Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
adicionar mais de uma unidade de um ‘item’ na lista de compras. Ou seja, o dicionário
deve armazenar o nome do ‘item’ e a quantidade desejada pelo usuário. Por exemplo,
se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
e 2 como valor. A estrutura do dicionário ficaria assim: {"banana": 2}.

O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.

Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
"Maçã" e "maçã" devem ser considerados o mesmo ‘item’.

Exemplo de saída:

1 Adicionar ‘item’
2 Remover ‘item’
3 Ver lista
4 Sair
Escolha uma opção: 3
{'banana': 1, 'maçã': 3}

"""

# 1. Tratar o menu, trocar para dicionário, tratar as palavras como iguais;
# 2. Fazer um dicionário vazio;
# 3. Fazer o menu;
# 4. Repetir o menu até que o usuário saia dele;
# 5. Se o usuário quiser adicionar algo, tem que ter dois valores;
# 6. Tratar as letras, pois se o usuário digitar letra maiúscula ou minúscula, deve reconhecer igualmente;
# 7. Se ele quiser remover, terá que remover a palavra-chave e a quantidade;
# 8. Se inserir um número errado, terá que rodar o código novamente.

lista_compra = {}

while True:
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Ver lista')
    print('4. Sair')
    escolha_opcao = input('Escolha uma opção: ')

    if escolha_opcao == '1':
        item = input('Nome do Item: ').lower()
        quantidade = int(input('Digite a quantidade: '))
        if item in lista_compra:
            lista_compra[item] += quantidade
        else:
            lista_compra[item] = quantidade
    elif escolha_opcao == '2':
        item = input('Nome do Item: ')
        if item in lista_compra:
            quantidade = int(input('Digite a quantidade: '))
            if quantidade >= lista_compra[item]:
                del lista_compra[item]
            else:
                lista_compra[item] -= quantidade
        else:
            print('Item não achado na lista de compras.')
    elif escolha_opcao == '3':
        for item, quantidade in lista_compra.items():
            print(f'{item}: {quantidade}')
    elif escolha_opcao == '4':
        break
    else:
        print('Opção inválida. Tente novamente.')

print(
    '------------------------------------------------------------------------------------------------------------------------')

print('Primeira Versão: Previsões de Vendas')

"""
Previsão de vendas

Primeira versão da previsão de vendas

Escreva um programa que preveja as vendas totais para cada produto numa empresa.
O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
e o programa deve calcular as vendas previstas para o próximo mês.

Estruture o seu programa da seguinte forma:

1. Crie um dicionário vazio para armazenar as previsões de vendas.
2. Crie um ‘loop’ infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
3. No ‘loop’, use uma declaração if para verificar se o usuário digitou 'sair'.
4. Se o usuário digitar 'sair', encerre o ‘loop’ usando break.
5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
6. Depois que o ‘loop’ for encerrado, use um ‘loop’ for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.

Exemplo de saída:
 
Digite o nome do produto (ou 'sair' para sair): iphone
Digite as vendas do mês atual: 10000
Digite a taxa de crescimento (%): 10

Digite o nome do produto (ou 'sair' para sair): capinha para iphone
Digite as vendas do mês atual: 200
Digite a taxa de crescimento (%): 20

Digite o nome do produto (ou 'sair' para sair): sair
iphone: Previsão de vendas do próximo mês = R$ 11000.00
capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
"""

# 1. Crie um dicionário vazio para armazenar as previsões de vendas;
# 2. Crie um 'loop' infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento;
# 3. No 'loop', use uma declaração if para verificar se o usuário digitou 'sair';
# 4. Se o usuário sair, use o break para quebrar o código;
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calculas vendas previstas e adicione-se ao dicionário;
# 6. Depois do encerramento do loop, use-o para iterar sobre o dicionário e mostrar as previsões de venda para cada produto.

previsoes_vendas = {}

while True:
    nome = input("Nome do Produto (ou escreva sair para sair): ")
    if nome.lower() == 'sair':
        break

    vendas_mes_atual = float(input('Vendas do mês atual: '))
    taxa_crescimento = float(input('Taxa de crescimento (%): '))

    vendas_proximo_mes = vendas_mes_atual * (1 + taxa_crescimento / 100)

    previsoes_vendas[nome] = vendas_proximo_mes

    for nome, vendas_proximo_mes in previsoes_vendas.items():
        print(f'Produto: {nome} / Previsão de Vendas do próximo mês: {vendas_proximo_mes:.1f}%')

print('Segunda Versão: Previsões de Vendas')

"""
Segunda versão da previsão de vendas

Mantenha a funcionalidade do programa anterior, mas agora valide a entrada do usuário.
Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
"Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
"""

# 1. Crie um dicionário vazio para armazenar as previsões de vendas;
# 2. Crie um 'loop' infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento;
# 3. No 'loop', use uma declaração if para verificar se o usuário digitou 'sair';
# 4. Se o usuário sair, use o break para quebrar o código;
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calculas vendas previstas e adicione-se ao dicionário;
# 6. Depois do encerramento do loop, use-o para iterar sobre o dicionário e mostrar as previsões de venda para cada produto;
# 7. Utilizando o try/exceppt e verificando a entrada do usuário:
#   1. Verificar se realmente é um erro de valor, já que pedimos em float.

previsoes = {}

while True:
    nome_produto = input('Nome do Produto (ou escreva sair para sair): ')
    if nome_produto.lower() == 'sair':
        break

    try:
        vendas_atual_mes = float(input('Vendas do mês atual: '))
        taxa_crescimento = float(input('Taxa de Crescimento (%): '))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento.')
        continue

    venda_proximo_mes = vendas_atual_mes * (1 + taxa_crescimento / 100)
    previsoes[nome_produto] = venda_proximo_mes

    for nome_produto, venda_proximo_mes in previsoes.items():
        print(f'Produto: {nome_produto} / Previsão de Vendas do próximo mês: {venda_proximo_mes:.1f}%')

print(
    '------------------------------------------------------------------------------------------------------------------------')

print('Primeira Versão: Relatório de Vendas')

"""
Relatório de vendas

Primeira versão do relatório de vendas

Escreva um programa que calcula o total e a média de vendas para cada vendedor numa empresa.
O usuário deve digitar o nome do vendedor e as suas vendas, e o programa deve manter o controle
do total e da média de vendas para cada vendedor.

Estruture o seu programa da seguinte forma:

1. Crie um dicionário vazio para armazenar os dados de vendas.
2. Crie um ‘loop’ infinito que solicite ao usuário o nome do vendedor e as suas vendas.
3. No ‘loop’, use uma declaração if para verificar se o usuário digitou 'sair'.
4. Se o usuário digitar 'sair', encerre o ‘loop’ usando break.
5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
6. Depois que o ‘loop’ for encerrado, use um ‘loop’ for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.

Exemplo de saída:

Digite o nome do vendedor (ou 'sair' para sair): João
Digite as vendas: 100
Digite o nome do vendedor (ou 'sair' para sair): Maria
Digite as vendas: 200
Digite o nome do vendedor (ou 'sair' para sair): João
Digite as vendas: 300
Digite o nome do vendedor (ou 'sair' para sair): sair
João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0

Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
"""

# Fazer um progama que calcula o total e a média de vendas para cada vendedor da empresa.
#   Criar um dicionário vazio para armazenar os dados de venda.
#   Loop infinito para cumprir as tarefas abaixo:
#       O usuário vai digitar o nome do vendedor.
#       O usuário vai digitar as vendas.
#       Se o usuário digitou 'sair':
#           Pare o programa.
#       Se o usuário digitar qualquer coisa, calcular o total e a média de vendas e adicionar ao dicionário.
#           Conta é a soma das vendas do usuário dividida pela quantidade de vendas totais que fez. (Usaremos sum() para soma total e len() para ler o número total de vendas)
#   Depois que o loop for encerrado, fazer com que apareça os dados iterados no dicionário.

dados_venda = {}

while True:
    nome_vendedor = input('Nome do Vendedor (ou escreva sair para sair): ')
    if nome_vendedor.lower() == 'sair':
        break

    vendas = float(input('Vendas: '))

    if nome_vendedor not in dados_venda:
        dados_venda[nome_vendedor] = [vendas]
    else:
        dados_venda[nome_vendedor].append(vendas)

    for nome_vendedor, vendas in dados_venda.items():
        total_vendas = sum(vendas)
        media_vendas = total_vendas / len(vendas)
        print(f'Nome: {nome_vendedor} / Total de Vendas: R${total_vendas:.1f} / Média de Vendas: R${media_vendas:.1f}')

print('Segunda Versão: Relatório de Vendas')

"""
Segunda versão do relatório de vendas

Mantenha a funcionalidade do programa anterior, mas agora valide a entrada do usuário.
Se o usuário digitar um valor inválido para vendas, mostre a mensagem
"Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
novamente. Tal validação deve ser feita usando try/except.

Além disso, ao invés de armazenar cada venda numa lista para cada vendedor, armazene
o total de vendas e a quantidade de vendas num dicionário. Por exemplo, se o usuário
digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
    {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}

Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
    {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}

Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou numa unidade.

Ao final, mostre o total de vendas e a média de vendas de cada vendedor.

Exemplo de saída:
    Digite o nome do vendedor (ou 'sair' para sair): João
    Digite as vendas: 1000
    Digite o nome do vendedor (ou 'sair' para sair): Maria
    Digite as vendas: 2000
    Digite o nome do vendedor (ou 'sair' para sair): João
    Digite as vendas: 2000
    Digite o nome do vendedor (ou 'sair' para sair): Maria
    Digite as vendas: 3000
    Digite o nome do vendedor (ou 'sair' para sair): sair
    João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
    Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
"""

# Fazer um progama que calcula o total e a média de vendas para cada vendedor da empresa.
#   Criar um dicionário vazio para armazenar os dados de venda.
#   Loop infinito para cumprir as tarefas abaixo:
#       O usuário vai digitar o nome do vendedor.
#           Se o usuário digitou 'sair':
#               Pare o programa.
#   Utilizar o try/except para fazer verificações de erros.
#       O usuário vai digitar as vendas.
#       Caso aconteça um erro, mandar aparecer mensagem com o try/except.
#   Se o usuário digitar qualquer coisa, calcular o total e a média de vendas e adicionar ao dicionário.
#       Conta é a soma das vendas do usuário dividida pela quantidade de vendas totais que fez. (Usaremos sum() para soma total e len() para ler o número total de vendas)
#   Depois que o loop for encerrado, fazer com que apareça os dados iterados no dicionário.

dados_vendas = {}

while True:
    vendedor = input('Nome do Vendedor (ou escreva sair para sair): ')
    if vendedor.lower() == 'sair':
        break

    try:
        vendas_vendedor = float(input('Vendas: '))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número para vendas.')
        continue

    if vendedor not in dados_vendas:
        dados_vendas[vendedor] = {'vendas_totais': vendas_vendedor, 'quantidade_vendas': 1}
    else:
        dados_vendas[vendedor]['vendas_totais'] += vendas_vendedor
        dados_vendas[vendedor]['quantidade_vendas'] += 1

    for vendedor, dados in dados_vendas.items():
        vendas_totais = dados['vendas_totais']
        media_total = vendas_totais / dados['quantidade_vendas']
        print(f'Vendedor: {vendedor} / Total de Vendas: R${vendas_totais:.2f} / Média de Vendas: R${media_total:.2f}')

print('Terceira Versão: Relatório de Vendas')

"""
Terceira versão do relatório de vendas

Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. 
Crie funções para cada uma das operações: solicitar_nome_vendedor, solicitar_vendas e atualizar_dados e print_dados’. 
O programa deve continuar a funcionar da mesma forma, mas agora o código deve estar organizado em funções.
"""


# Fazer um progama que calcula o total e a média de vendas para cada vendedor da empresa.

#   Criar as funções abaixo:
#       Primeira função: solicitar_nome_vendedor:
#           O usuário irá digitar o nome do vendedor;
#           Fazer um if para quebrar o código, caso não queira mais inserir vendedores;

#       Segunda função: solicitar_vendas:
#           Fazer um input das vendas;
#           Utilizar o try/except para fazer verificações de erros.

#       Terceira função: atualizar_dados:
#           Fazer verificação do nome do funcionário;
#           Guardar no dicionário os dados de nome, vendas e quantidade de vendas.

#       Quarta função: print_dados:
#           Se o usuário digitar qualquer coisa, calcular o total e a média de vendas e adicionar ao dicionário.
#           Conta é a soma das vendas do usuário dividida pela quantidade de vendas totais que fez. (Usaremos sum() para soma total e len() para ler o número total de vendas)
#           Depois que o loop for encerrado, fazer com que apareça os dados iterados no dicionário.

#       Quinta função: main():
#           Criar o dicionário dos dados_vendas;
#           Fazer o loop infinito rodar o código inteiro;
#           Fazer com que tenha a verificação, caso o usuário não queira mais continuar escrevendo;
#           Verificar as vendas, caso seja nula;
#           Printar os dados.


def solicitar_nome_vendedor():
    return input('Nome do Vendedor (ou escreva sair para sair): ').lower()


def solicitar_vendas():
    try:
        return float(input('Vendas: '))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número para vendas.')
        return None


def atualizar_dados(dados_vendas2, nome2, vendas2):
    if nome2 not in dados_vendas2:
        dados_vendas2[nome2] = {'total_vendas': vendas2, 'quantidade_vendas': 1}
    else:
        dados_vendas2[nome2]['total_vendas'] += vendas2
        dados_vendas2[nome2]['quantidade_vendas'] += 1


def print_dados(dados_vendas2):
    for nome2, dados2 in dados_vendas2.items():
        total_vendas2 = dados2['total_vendas']
        media_vendas2 = total_vendas2 / dados2['quantidade_vendas']
        print(f'Vendedor: {nome2} / Total de Vendas: R${total_vendas2:.2f} / Média de Vendas: R${media_vendas2:.2f}')


def main():
    dados_vendas2 = {}
    while True:
        nome2 = solicitar_nome_vendedor()
        if nome2 == 'sair':
            break
        vendas2 = solicitar_vendas()
        if vendas2 is None:
            continue
        atualizar_dados(dados_vendas2, nome2, vendas2)
    print_dados(dados_vendas2)


if __name__ == '__main__':
    main()

print(
    '------------------------------------------------------------------------------------------------------------------------')

print('Primeira Versão: Segmentação de Clientes')

"""
Segmentação de clientes

Primeira versão da segmentação de clientes

Escreva um programa que segmenta clientes com base nas suas compras totais.
O usuário deve digitar o nome do cliente e as suas compras totais, e o programa
deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R$1000,
'Prata' para compras de até R$5000 e 'Ouro' para compras acima de R$5000.

Estruture o seu programa da seguinte forma:

1. Crie um dicionário vazio para armazenar os clientes e os seus segmentos.
2. Crie um ‘loop’ infinito que solicite ao usuário o nome do cliente e as suas compras totais.
3. No ‘loop’, use uma declaração if para atribuir o segmento apropriado ao cliente.
4. Se o usuário digitar 'sair' para o nome do cliente, encerre o ‘loop’ usando break.
5. Fora do ‘loop’, use um ‘loop’ for para imprimir o nome e o segmento de cada cliente.

Exemplo de saída:
 
Digite o nome do cliente (ou 'sair' para sair): João
Digite o total de compras: 100
Digite o nome do cliente (ou 'sair' para sair): Maria
Digite o total de compras: 2000
Digite o nome do cliente (ou 'sair' para sair): José
Digite o total de compras: 6000
Digite o nome do cliente (ou 'sair' para sair): sair
João: Segmento do Cliente = Bronze
Maria: Segmento do Cliente = Prata
José: Segmento do Cliente = Ouro
"""

# Criar um programa que segmenta clientes com base nas suas compras totais.
#   Criar um dicionário vazio e implementar os clientes e seus segmentos.
#   Criar um loop infinito e solicitar o nome do cliente e suas compras.
#       Digitar o nome do cliente.
#           Se o usuário quiser sair, usar a verificação e o break.
#       Digitar compras totais.
#       Criar um if para indicar o segmento do cliente conforme as compras.
#           O programa deve atribuir as seguintes coisas para cada cliente:
#               Bronze: compras até 1000
#               Prata: compras até 5000
#               Ouro: compras maiores que 5000
#   Fazer um loop para apresentar o nome e o segmento de cada cliente.

clientes_segmentos = {}

while True:
    nome_cliente = input('Nome do Cliente (ou escreva sair para sair): ')
    if nome_cliente.lower() == 'sair':
        break

    compras_cliente = float(input('Compras do Cliente: R$'))

    if compras_cliente <= 1000:
        segmento = 'Bronze'
    elif compras_cliente <= 5000:
        segmento = 'Prata'
    else:
        segmento = 'Ouro'

    clientes_segmentos[nome_cliente] = segmento

    for nome_cliente, segmento in clientes_segmentos.items():
        print(f'Nome do Cliente: {nome_cliente} / Segmento do Cliente: {segmento}')

print('Segunda Versão: Segmentação de Clientes')

"""
Segunda versão da segmentação de clientes

Mantenha a funcionalidade do programa anterior, mas agora valide a entrada do usuário.
Se o usuário digitar um valor inválido para compras, mostre a mensagem
"Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
novamente. Tal validação deve ser feita usando try/except.

Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os numa
lista de tuplas. Por exemplo:

segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
 
Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
com limite float('inf.')`, que representa o segmento Ouro. Isso significa que, se o valor de
compras for maior que todos os limites, o segmento será Ouro.

Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
ao limite. Se for, armazene o segmento num dicionário. Por exemplo, se o usuário digitar
"João" e "500" para compras, o dicionário deve ficar assim:
{'João': 'Bronze'}
"""

# Criar um programa que segmenta clientes com base nas suas compras totais.
#   Criar uma tupla vazia e implementar primeiro limite de comppras e o segundo é o nome do segmento, mas o ouro terá o limite float('inf.').
#   Criar um dicionário vazio.
#   Criar um loop infinito e solicitar o nome do cliente e suas compras.
#       Digitar o nome do cliente:
#           Se o usuário quiser sair, usar a verificação e o break.
#       Digitar compras totais:
#           Validar a entrada do usuário com o try;
#           Mostrar uma mensagem, caso os valores sejam inseridos errados.
#       Percorrer a lista, para cada tupla, verificar se o valor de compras é menor ou igual ao limite.
#           Se for, armazene em um dicionário.
#   Fazer um loop para apresentar o nome e o segmento de cada cliente.

tupla_segmento = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
dicionario_segmento = {}

while True:
    cliente_nome = input('Nome do Cliente (ou escreva sair para sair): ')
    if cliente_nome.lower() == 'sair':
        break

    try:
        compras_totais = float(input('Total de Compras: R$'))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número para compras.')
        continue

    for limite, segmento in tupla_segmento:
        if compras_totais <= limite:
            dicionario_segmento[cliente_nome] = segmento
            break

for cliente_nome, segmento in dicionario_segmento.items():
    print(f'Nome do Cliente: {cliente_nome} / Segmento do Cliente: {segmento}')

print('Terceira Versão: Segmentação de Clientes')

"""
Terceira versão da segmentação de clientes

Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. 
Crie funções para cada uma das operações: solicitar_nome_cliente, solicitar_total_compras` e `atribuir_segmento` e 
`print_segmento_por_cliente`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções. 
Além disso, normalize que todos os nomes sejam armazenados em letras minúsculas.
"""


# Criar um programa que segmenta clientes com base nas suas compras totais.

#   Criar as funções abaixo:
#       Primeira função: solicitar_nome_cliente()
#           Digitar o nome do cliente e retornar no input.

#       Segunda função: solicitar_total_compras()
#           Digitar compras totais:
#               Validar a entrada do usuário com o try;
#               Mostrar uma mensagem, caso os valores sejam inseridos errados.

#       Terceira função: atribuir_segmento(compras, segmentos)
#          Percorrer a verificação caso ultrapasse o limite e o segmento.
#               Se caso as compras sejam menores que o limite:
#                   O segmento será o devido conforme as compras.

#       Quarta função: print_segmento_por_cliente(clientes)
#           Printar conforme o nome, o limite e o segmento do cliente, utilizando um for.

#       Quinta função: main()
#           Criar uma tupla vazia e implementar primeiro limite de comppras e o segundo é o nome do segmento, mas o ouro terá o limite float('inf.').
#           Criar um dicionário vazio.
#           Fazer a verificação se o cliente deseja sair do loop infinito.
#           Percorrer a lista, para cada tupla, verificar se o valor de compras é menor ou igual ao limite.
#               Se for, armazene em um dicionário.
#           Fazer um loop para apresentar o nome e o segmento de cada cliente.#   Fazer um loop para apresentar o nome e o segmento de cada cliente.

# Utilizar um código específico para rodar a função main():
#   if __name__ == '__main__':
#       main()


def solicitar_nome_cliente():
    return input('Nome do Cliente: ').lower()


def solicitar_total_compras():
    try:
        return float(input('Total de Compras: R$'))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número para compras.')
        return None


def atribuir_segmento(compras, segmentos):
    for limite, segmento in segmentos:
        if compras <= limite:
            return segmento


def print_segmento_por_cliente(cliente):
    for nome, segmento in cliente.items():
        print(f'Nome do Cliente: {nome} / Segmento do Cliente: {segmento}')


def main():
    segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
    clientes = {}
    while True:
        nome = solicitar_nome_cliente()
        if nome == 'sair':
            break

        compras = solicitar_total_compras()
        if compras is None:
            continue

        clientes[nome] = atribuir_segmento(compras, segmentos)

    print_segmento_por_cliente(clientes)


if __name__ == '__main__':
    main()

print(
    '------------------------------------------------------------------------------------------------------------------------')

print('Priemeira Versão: Analisador de Texto')

"""
Analisador de texto

Crie um programa que analise um texto fornecido pelo usuário.
O programa deve contar o número de palavras (independentemente se há repetição ou não), a quantidade de cada palavra e a
quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
Não se preocupe com pontuação e espaços ao contar palavras.

O programa deve conter uma função chamada `analisar_texto` que recebe o texto
como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
frequência de letras.

Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
imprimir:

Contagem de palavras: 8
Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
"""

# Criar um programa que analise um texto fornecido pelo usuário.
# Contar o número das palavras (mesmo que haja repetições), a quantidade de cada palavra e a quantidade de letras.
# Criar uma função:
#   Primeira função: analisar_texto(texto)
#       Retornando uma contagem de palavras, a frequência de palavras e a frequência de letras.


def analisar_texto(texto):
    palavras = texto.split() # Separa com base em espaços
    contagem_palavras = len(palavras) # Lê a quantidade de palavras
    frequencia_palavras = {}
    frequencia_letras = {}

    for palavra in palavras:
        # O .get() serve para verificar se existe essa palavra no dicionário. Se não tiver, atribui 0 e soma 1.
        frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1
        for letra in palavra.lower():
            # O .get() serve para verificar se existe essa letra no dicionário. Se não tiver, atribui 0 e soma 1.
            frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1

    return contagem_palavras, frequencia_palavras, frequencia_letras


texto = input('Digite um texto qualquer: ')
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f'Contagem de Palavras: {contagem_palavras}')
print(f'Frequência de Palavras: {frequencia_palavras}')
print(f'Frequência de Letras: {frequencia_letras}')

"""
Observação importante:

__name__ -> é uma variável especial em Python que contém o nome do módulo atual.

Quando um script Python é executado diretamente, __name__ é definido como '__main__'.

Quando um script Python é importado como um módulo em outro script, __name__ é definido como o nome do próprio módulo.

Portanto, a linha if __name__ == '__main__': verifica se o script está sendo executado diretamente. Se for o caso, ele chama a função main(). 

Isso é feito para evitar a execução de código quando o script é importado como um módulo, garantindo que o código contido em main() 
só seja executado quando o script for executado diretamente.
"""
