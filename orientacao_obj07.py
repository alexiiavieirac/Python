# Mais edições de Gráfico com MatplotLib -> More Plot edits with MatplotLib

import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.plot(meses, vendas)
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()


"""
Português:
    Podemos mudar a forma das linhas do gráfico, podemos vê-las na documentação do Python, assim conseguimos utilizar 
    conforme o que pecisamos.
    Podemos mudar a cor das linhas do gráfico.
    
English:
    We can change the shape of the graph lines, we can see them in the Python documentation, so we can use
    according to what we need.
    We can change the color of the graph lines.
"""

# Mudando a linha para marcadores: -> Changing the line to bullets:
plt.plot(meses, vendas, color='gray')
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()

# Dispersão: -> Scatter:
plt.scatter(meses, vendas)
plt.show()

# Barras: -> Bars:
plt.bar(meses, vendas)
plt.show()

# Múltiplos Gráficos no mesmo 'plot': -> Multiple Graphs on the same 'plot':
plt.figure(1, figsize=(15, 3))
plt.subplot(1, 3, 1)
plt.plot(meses, vendas)
plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)
plt.subplot(1, 3, 3)
plt.bar(meses, vendas)
plt.show()
