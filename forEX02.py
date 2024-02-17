# Exercícios

"""
1. Calculando % de uma lista
    Faremos algo parecido com "filtar" uma lista. Mais para frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimento atual
    já conseguimos resolver o desafio.

    Digamos que nós tenhamos uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de
    vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.

    Resolveremos de duas formas:
        1. Criando uma lista auxiliar apenas com os vendedores que bateram a meta;
        2. Fazendo o cálculo diretamente na lista que já temos.
"""

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870]
]

listaAuxiliar = []

for item in vendas:
    if item[1] > meta:
        listaAuxiliar.append(item[0])

print(listaAuxiliar)

percentual = len(listaAuxiliar) / len(vendas)
print("Porcentagem de vendedores que bateram a meta: {:.0%}".format(percentual))

# Quem foi o vendedor que mais vendeu?

melhorVendedor = ''
maiorVenda = 0

for venda in vendas:
    if venda[1] > maiorVenda:
        maiorVenda = venda[1]
        melhorVendedor = venda[0]

print("Vendedor: {} | Vendas: {} | Parabéns, você teve o maior número de vendas!".format(melhorVendedor, maiorVenda))

# O código acima está analisando quem foi o melhor vendedor e quantas vendas ele teve, feito da seguinte forma:
"""
    Para cada venda que está dentro da lista vendas faça: 
        Se a venda[1] (que é a informação da quantidade de índice 1, que no caso seria o valor de vendas) for igual a maior venda (no caso, está sendo inicializada com o valor 0) faça:
            A variável maior venda receberá o que foi armazenado na venda[1] que seria a quantidade de vendas, mas a cada vez que for rodar o FOR, se achar um número de vendas maior,
            será substituído então, pois começa com 0, após isso tem um número de 15000, logo após, um número de 27000 e assim por diante, mudando o que está armezado conforme for
            rodando o IF dentro do FOR.
            Para sabermos o nome da pessoa que tem o maior número de vendas, podemos fazer uma variável de melhor vendedor que sua inicialização é vazia (''), pois iremos adicionar
            nessa variável o valor que queremos conforme o decorrer do código. Logo isso, podemos colocar que o melhor vendedor é igual ao venda[0] (que é o nome da pessoa que teve
            maior número de vendas, pois ele estará no loop de saber qual foi o maior número de vendas), assim quando a maior venda estagnar em algum valor, o melhor vendedor também
            parará de ser modificado.
"""
