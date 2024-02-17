produtos  = ["iPhone", "iPad", "AirPod", "MacBook"]
precos = [7000, 10000, 2500, 14000]

# For em lista: Quando quer percorrer uma única lista, um único dicionário você utiliza esse.
for preco in precos:
    print(preco * 1.1)

# For i in range (correlaciona duas listas ou mais): i vai ser o índice da lista e o range pega o tamanho da lista e mostra a quantidade de elementos que há dentro da lista.
for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print("Produto: {} | Quantidade: {}".format(produto, preco))

# For item in lista com enumerate: O Enumerate vai apenas numerar as iterações, ele vai dar tanto o índice quanto o elemento.
for i, preco in enumerate(precos):
    produto = produtos[i]
    print(produto, preco)
