"""
for item in lista:
    if condição:
        faça alguma coisa
    else:
        faça outra coisa
"""

# Inicializamos as variáveis que utilizaremos:
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

qtde_metas = 0

# Usamos o FOR para delimitarmos a quantidade que há de elementos dentro da lista vendas, logo após isso fazemos o IF para
# verificarmos se a quantidade dos elementos que pesquisamos dentro da lista vendas é maior ou igual que a meta estabelecida,
# para cada item que for verdade, a variável qtde_metas adicionará 1 dentro dela, pois ela serve como um contador:
for venda in vendas:
    if venda >= meta:
        qtde_metas += 1

# O código abaixo serve para vermos a quantidade de funcionários que há na loja, sabemos pela quantidade de elementos de nossa lista:
qtde_funcionarios = len(vendas)

# O código abaixo serve para nos mostrarmos o percentual das metas que os funcionários bateram, logo para descobrirmos a quantidade
# pegamos o total de metas batidas (qtde_metas) e dividimos pela quantidade de funcionários (qtde_funcionarios) que há dentro da loja:
percentual = qtde_metas / qtde_funcionarios

# Dentro das chaves {} tem a formatação {:.0%}, que quer dizer: formataremos com 0 casas depois da vígula e sera um percentual:
print("Percentual de Metas Batidas: {:.0%}".format(percentual))
