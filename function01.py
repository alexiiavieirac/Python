# Function

def cadastrar_produto():
    produto = input('Nome do Produto: ')
    produto = produto.casefold()
    print(f'Produto {produto} cadastrado com sucesso.')


for i in range(3):
    cadastrar_produto()
