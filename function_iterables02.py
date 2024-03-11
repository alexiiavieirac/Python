"""
Sort (ou sorted) como function

Descrição:
Até agora no programa, usamos várias vezes o .sort() para ordenar listas.
Mas o método sort tem um parâmetro que nunca foi utilizado.

Obs.: O .sort() modifica a lista original e o sorted() precisa sempre ser atribuída um valor, exemplo: a lista
original e a lista cirada para o sorted.

Obs.: O sort() coloca em ordem conforme a tabela ASCII
"""

produtos = ['Apple TV', 'Mac', 'iPhone X', 'iPhone 11', 'iPad', 'Apple Watch', 'Mac Book', 'AirPods']
produtos.sort()
print(produtos)

# Como faríamos para ordenar corretamente?
produtos.sort(key=str.casefold)
print(produtos)

# Outro exemplo: como ordenar um dicionário de acordo com o valor.
vendas_produtos = {'Vinho': 100, 'Cafeteira': 150, 'Microondas': 300, 'iPhone': 5500}

# Queremos listas da maior quantidade de vendas para a menor, para enviar como report para o diretor, por exemplo.


def segundo_item(tupla):
    return tupla[1]


lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)

print(dict(lista_vendas))