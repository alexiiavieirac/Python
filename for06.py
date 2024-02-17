# Formas de Interromper um FOR

# Break -> Interrompe e finaliza o FOR;
# Continue -> Interrompe e vai para o próximo item do FOR.

vendas = [100, 150, 1500, 2000, 120]

meta = 110

# O Break serve para quando encontra o que procura, ele não continua a percorrer a lista, e assim para no “item” que já identificamos para cada caso distinto:
# o Break sai do FOR.
for venda in vendas:
    if venda < meta:
        print("A loja não ganha bônus.")
        break

vendedores = ['João', 'Júlia', 'Ana', 'José', 'Maria']
meta = 130

# Neste caso, o Continue, serve para uma condição que não deve ser inclusa, pois, não pertence ao que foi pedido, e assim ele volta para o FOR nesse caso:
# Ex: No código abaixo, o FOR será exucatado, o IF também, caso a venda seja menor que a meta, ele não irá passar pelo print, mas sim irá direto para o FOR novamente, voltando ao “loop”.
# O Continue, continua para o próximo "item" que está na lista.
for venda in vendas:
    if venda < meta:
        continue
    print(venda)
