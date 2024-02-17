# Mais de 1 argumento e formas de passar argumento para uma função

# Estrutura:
# 2 formas de passar o argumento:
#   1. Em ordem (positional argument)
#   2. Com o nome kdo arguemento (keyword argument)

def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False


produtos = ['CAR46275', 'TFA23962',  'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510',  'TFA44968', 'CAR75448', 'CAR23596', 'CAR13490', 'BEB21365',
            'BEB31623', 'BSA62419', 'BEB73344', 'TFA20079', 'BEB80694', 'BSA11769', 'BEB19495', 'TFA14792', 'TFA78043', 'BSA33484', 'BEB97471',
            'BEB62362', 'TFA27311', 'TFA17715', 'BEB85146', 'BEB48898', 'BEB79496', 'CAR38417', 'TFA19947', 'TFA58799', 'CAR94811', 'BSA59251',
            'BEB15385', 'BEB24213', 'BEB56262', 'BSA96915', 'CAR53454', 'BEB75073']

for produto in produtos:
    # if categoria(cod_categoria = 'BEB', bebida = produto):
    if categoria(produto, 'BEB'):
        print(f'Enviar {produto} para o setor de bebidas alcóolicas.')
    elif categoria(produto, 'BSA'):
        print(f'Enviar {produto} para o setor de bebidas não alcóolicas.')
