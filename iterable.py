# Iterable

# Um Iterable é uma estrutura que armazena dados que pode ser 'iterada', ou seja, que pode fazer um ‘loop’ como um for dentro dela e ir passando
# de ‘item’ a ‘item’. É como se fosse um tipo de lista de coisas que voce pode ir olhando cada um dos elementos dentro dela.

# Estrutura com várias informações, onde podemos correr ela e podemos fazer alguma ação com cada uma das coisas dentrro dessa lista.

# Listas:
produtos = ['iPhone', 'Samsung Galaxy', 'TV Samsung', 'PS5', 'Tablet', 'iPad', 'TV Philco', 'Notebook HP', 'Notebook Dell', 'Notebook Asus']

for produto in produtos:
    print(produto)

# Strings
texto = 'lekacvieira@gmail.com'

for ch in texto:
    print(ch)

# Tuplas
produtos = ('iPhone', 'Samsung Galaxy', 'TV Samsung', 'PS5', 'Tablet', 'iPad', 'TV Philco', 'Notebook HP', 'Notebook Dell', 'Notebook Asus')

for produto in produtos:
    print(produto)

# Dicionário
vendas_produtos = {'iPhone': 1500, 'Samsung Galaxy': 12000, 'TV Samsung': 10000, 'PS5': 14300, 'Tablet': 1720, 'iPad': 1000, 'TV Philco': 2500, 'Notebook HP': 1000, 'Notebook Dell': 17000, 'Notebook Asus': 2450}

for produto in vendas_produtos:
    #print(produto)
    print('{}: {} unidades.'.format(produto, vendas_produtos[produto]))
