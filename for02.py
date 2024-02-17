"""
for i in range(5):
    print(i)

range(5) é na verdade uma lista do tipo: [0, 1, 2, 3, 4] (Índice)

Da forma feita acima podemos ver que o i corresponde ao índice de cada item que a lista contém, quando passa pelo índice 0,
ele pega o elemento que corresponde a tal índice e mostra na tela. Podemos fazer isso de uma forma mais direta, assim:

for item in lista:
    print(item)

Agora eu pego o FOR, falo que o item está dentro da lista que contém os elementos que quero mostrar na tela, e agora o FOR rodará
apenas na quantidade certa de elementos que a lista contém, mas podemos entender que dessa forma o FOR não trabalha com o índice, mas sim
com os elementos propriamente ditos dentro da lista.
"""

produtos = ['Coca', 'Pepsi', 'Guarana', 'Sprite', 'Fanta']

# Podemos traduzir da seguinte forma: "Produtos é minha lista e o produto é cada item que contém dentro da lista.".
for produto in produtos:
    print(produto)

# ----------------------------------------------------------------------------------------------------------------------
print("___________________________")

texto = 'lekacvieira@gmail.com'

# Nesse caso, o texto é uma String, então cada letra é um caractere diferente, logo quando colocarmos dentro de um FOR
# para mostrar, aparecerá letra por letra, pois cada letra é um caractere distinto:
for caractere in texto:
    print(caractere)
