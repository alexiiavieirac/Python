# Usando módulos para ajudar a resolver desafios.

from collections import Counter

"""
Objetivo:
    Muitas vezes algum módulo vai ajudar a gente a resolver um desafio que talvez até conseguíssemos resolver de outra forma.
"""

"""
Exemplo:
    Digamos que você está analisando todas as vendas dos produtos de tecnologia de um e-commerce e quer saber quais foram os 6
    produtos que mais veneram (e suas respectivas quantiaes e vendas) - ou seja, queremos descobrir um top 3 produtos de forma simples.
"""

vendas_tecnologia = {'Notebook Asus': 2450, 'iPhone': 15000, 'Samsung Galaxy': 12000, 'TV Samsung': 10000, 'PS5': 14300,
                     'Tablet': 1720, 'Notebook Dell': 17000, 'iPad': 1000, 'TV Philco': 2500, 'Notebook HP': 1000}

auxiliar = Counter(vendas_tecnologia)
print(auxiliar.most_common(3))
