# Mais sobre o return

# Pontos importantes:
# 1. Podemos usar no return prraticamente qualquer tipo de objeto: (número, string, tupla, dicionário, outros objetos, etc.)
# 2. O return, se for executado, encerra a função, mesmo que dentro dela haja um 'loop'.


# Retornar um número:
def minha_soma(num1, num2, num3):
    return num1 + num2 + num3


# Retornar um texto:
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace('  ', ' ')
    texto = texto.strip()
    return texto


# Retornar um boolean:
def bateu_meta(vendas, meta):
    if vendas >= meta:
        return True
    else:
        return False


# Retornar uma lista, tupla ou dicionário:
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada
