# Function em Iterables

"""
Segua a mesma lógica que o List Comprehension, mas é mais simples.
Basicamente alguns métodos e funções que já existem no Python podem rodar uma function para cada item, da mesma forma
que fizemos com List Comprehension.

Isso pode ajudar na resolução de alguns desafios de forma mais simples.

Uma função que permite que façamos isso é a Map Function.

Map Function: O Map aplica a sua função para cada iterable.
    lista = list(map(função, iterable_original))
"""

# Exemplo: Digamos que eu tenha uma function que corrige um código de um produto.


def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace('  ', ' ')
    texto = texto.strip()
    return texto


# Agora queremos padronizar uma lista de códigos:
produtos = [' ABC12 ', 'abc34', 'AbC37', ' BSA151', 'BEB23']

print("For tradicional:")
# Usando o for, temos que percorrer a lista toda e para cada item executar a function:
for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)

print("-------------------------------------------------------------------------------")

print("Usando Map:")
# Usando o Map, apenas chamamos a função e ela faz o que o For faz:
# Obs.: Precisamos colocar o Map dentro do List, pois ele é um objeto, e queremos uma lista.
tratamento_texto = list(map(padronizar_texto, produtos))
print(tratamento_texto)
