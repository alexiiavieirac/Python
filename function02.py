# Retornar um valor na Function

def cadastrar_produto():
    produto = input('Nome do Produto: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto

# Não tem problema colocar o mesmo nome da variável como o nome que usamos na Function, pois o da Function é exclusivo dela somente.
produto = cadastrar_produto()

print(f'Produto {produto} cadastrado')
