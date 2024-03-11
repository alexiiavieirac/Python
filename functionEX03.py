# Exercícios

# 1. Cálculo do Percentual e da Lita de Vendedores

# Queremos criar uma function que consiga identificar os vendedores que bateram uma meta, mas, além disso, consigo já me dar como resposta o cáculo do % da lista de vendedores
# que bateram a meta;
# Essa function deve receber duas informações como parâmetro: a meta e um dicionário com os vendedores e as suas vendas. E dar duas respostas: uma lista com o nome dos vendedores
# que bateram a meta e o % de vendedores que bateu a meta.

meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 7350,
    'Ana': 10300,
    'Alon': 7870
}


def calculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    percentual_meta = len(bateram_meta) / len(vendas)
    return percentual_meta, bateram_meta


percentual, vendedores_meta = calculo_meta(meta, vendas)
print(f'Vendedores: {vendedores_meta} / Percentual: {percentual:.1%}')
