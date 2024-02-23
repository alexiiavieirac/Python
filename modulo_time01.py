# Módulo time em Python

# Fornece uma variedade de funções apra tabalhar com tempo.

# Ex: time.time() -> retorna o tempo atual em segundos desde a Epoch (1º de Janeiro de 1970).

"""
O tempo ajuda no controle de nosso programa, exemplo: se estivesse rodando devagar, você deverá procurar o gargalo de desempenho
do programa, assim podendo cronometrar o tempo de funções chave do programa, para ver se alguma das funções está levando mais tempo que
o necessário para ser executada.
"""

import time

print('Primeiro Modo: time.time()')
inicio = time.time()

for i in range(100_000_000):
    pass

fim = time.time()

print(f'Tempo Decorrido: {fim - inicio} segundos.')

# Podemos fazer uma análise de Branchmark, pois testa a performance e o desempenho de seu computador.

# time.sleep() -> O progama espera a quantidade de segundos para executar o resto do programa.

print('Segundo Modo: time.sleep()')
print('Iniciando a pausa.')

time.sleep(5)

print('Pausa de 5 segundos finalizada.')

# time.ctime() -> Converte um tempo expresso em segundos desde a Epoch em uma string representando o tempo local.

print('Terceiro Modo: time.ctime()')
tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f'Tempo Local: {tempo_local}')

# time.time() vs time.localtime() -> A função time retorna o tempo em segundos desde a Epoch. A função localtime converte
# um tempo em segundos desde a Epoch em um objeto struct_time. Esse objeto contém informções sobre tempo local, como: ano,
# mês, dia, hora, segundo, etc. A função localtime() usa o fuso horário local.

print('Quarto Modo: time.localtime()')

temp_sec = time.time()
temp_local = time.localtime(temp_sec)
print(f'Tempo Local: {temp_local}')

print(f'Year: {temp_local.tm_year}')
print(f'Hour: {temp_local.tm_hour}')
print(f'Day: {temp_local.tm_mday}')
print(f'Week Day: {temp_local.tm_wday}')
print(f'Year Day: {temp_local.tm_yday}')
print(f'Time Zone: {temp_local.tm_zone}')
