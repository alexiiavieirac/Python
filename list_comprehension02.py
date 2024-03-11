# O que faríamos se quisermos ordenar 2 listas "ordenadas"?

vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['Vinho', 'Cafeteira', 'Microondas', 'iPhone']

# Se formos ordenadar as listas com o sort(), ele não ordenará de uma forma que o preço represente o produto.
# Quando utilizamos o sort, ele olha o primeiro item.

# Zip -> Junta duas listas.

lista_aux = list(zip(vendas_produtos, produtos))
lista_aux.sort(reverse=True)

produtos = [produto for vendas, produto in lista_aux]
print(produtos)