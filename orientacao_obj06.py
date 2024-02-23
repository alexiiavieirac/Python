# Exibindo Gráficos no Python

import matplotlib.pyplot as plt

"""
Importância:
    Para exploração e visualização de dados, nada melhor que usar gráficos para isso. Apesar do Python ser programação,
    gráficos facilitam muito em qualquer projeto que trabalhe com dados.

Estrutura:
    Usaremos o módulo Matplotlib.pyplot, que é o módulo mais usado no Python. Existem outros, como o Seaborn e o Plotly,
    caso queira ver ou usar.
"""

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 122, 1500, 2000, 1433, 2100, 2762]
meses = ['Jan', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)])
plt.show()

# Adicionar um Label no eixo X e Y

# Mudar o nome dos meses

# Ajeitando o Eixo
