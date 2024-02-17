"""
for i in range(5):
    print(i)

Esse i é na verdade o índice que começa do 0 e vai até o 4.
"""

# Inicializando as listas:
produtos = ['Coca', 'Pepsi', 'Guarana', 'Sprite', 'Fanta']
producao = [15000, 12000, 13000, 5000, 250]

"""
# Fazendo um FOR para que pegue o índice de cada elemento, sendo que na lista contém 5 elementos (range(5)), logo depois printamos
# na tela, passando como parâmetro o nome da variável da lista e o índice em que se encontra, no caso, a variável i:
for i in range(5):
    print("{}: {} unidades.".format(produtos[i], producao[i]))
"""

# Para automatizarmos o FOR feito acima, faremos a seguinte mudança:
tamanhoLista = len(produtos)

for i in range(tamanhoLista):
    print("{}: {} unidades.".format(produtos[i], producao[i]))
