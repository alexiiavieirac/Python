# Exemplos de parâmetros

# upper() -> Não possui parâmetros;
# sort() -> Apenas parâmetros keyword;
# extend(lista) -> 1 parâmetro obrigatório;
# nossa função categoria(bebida, cod) -> 2 parâmetros de posição obrigatórios.


def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False


# Texto para upper
cod_produto = 'beb12304'
print(cod_produto.upper())

# Lista para sort e extend
vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
vendas_novdez = [500, 1555]

vendas_ano.extend(vendas_novdez)

vendas_ano.sort(reverse=True)
print(vendas_ano)


if categoria(cod_produto, 'BEB'):
    print('É uma bebida alcóolica.')

