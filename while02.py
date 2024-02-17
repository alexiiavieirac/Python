# Loop Infinito (Cuidado!)

# Sempre que for usar o While, lembre-se de ter certeza que o programa vai terminar em algum momento.

vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

i = 0

while vendas[i] > meta:
    print("Meta alcançada: {} | Vendas: {}".format(vendedores[i], vendas[i]))
    i += 1 
