# List Comprehension - O que é e qual a importância?

"""
Descrição:
    List Comprehension é uma forma de iterar pelos elementos das listas de maneira "mais direta", com
    mais "Cara de Python".
    Em resumo:: é como se você fizesse um "for" em uma linha de código.

Estrutura:
    lista = [expressão for item in iterable]
"""

preco_produtos = [100, 150, 300, 5500]
produtos = ['Vinho', "Cafeteira", "Microondas", "iPhone"]

# Digamos que o imposto sobre os produtos é de 30%, ou seja, 0.3. Como eu faria pra criar uma lista com os valores de
# imposto de cada produto?

impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)

"""
impostos = []
for item in preco_produtos:
    impostos.append(item * 0.3)
print(impostos)


# Para usar na função:


def calcular_imposto(preco, imposto):
    return preco * imposto


imposto = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
"""
