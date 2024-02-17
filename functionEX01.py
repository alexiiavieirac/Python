# Exercícios

# 1. Function para Cálculo de Carga Tributária

# Crie uma function que calcule o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o 'lucro' e os custos (com exceção do imposto) dele.

preco = 1500
custo = 400
lucro = 800


def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    carga = imposto / preco
    return carga


carga = carga_tributaria(preco, custo, lucro)
print(f'Carga Tributária: {carga:.1%}')
