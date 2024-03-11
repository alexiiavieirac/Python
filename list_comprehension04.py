# List Comprehension com IF para escolher o resultado final

"""
Estrutura:
    lista = [item if condição else outro_resultado for item in iterable]

Digamos que eu esteja analisando os vendedores de uma loja e queira criar uma lista para enviar para o RH com o bônus de
cada vendedor.
O bônus é dado por 10% do valor de vendas dele, caso ele tenha batido a meta.
"""

meta = 1000
vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900,
                  'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90,
                  'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880,
                  'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300,
                  'Sandra': 450, 'Luis': 800}

# Fazenddo pelo For:
bonus = []

for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)
print(bonus)

# Fazendo pelo List Comprehension:
# Leitura: O bônus será uma lista, que cada item será vendedores_dic[item] * 0.1, mas somente SE o vendedores_dic[item]
# > meta, caso contrário será 0, e isso para cada item que há dentro de vendedores_dic.
bonus = [vendedores_dic[item] * 0.1 if vendedores_dic[item] > meta else 0 for item in vendedores_dic]
print(bonus)

"""
Fazendo apenas a modificação de Dicionário para Lista e mostrando os vendedores que bateram a meta (sem bonificação):
lista_vendedores = vendedores_dic.items()
lista_vendedores = list(lista_vendedores)
print(lista_vendedores)

bonificacao_vendedores = [nome for nome, valor in lista_vendedores if valor > meta]
print(bonificacao_vendedores)
"""
