# Módulo time em Python
import locale
import time
# Fornece uma vaiedade de funções poaa trabalhar com tempo.

print("----------------------------------------------------------------------------------------------------------------------------------")

# time.strftime() -> Converte um objeto de tempo struct para uma sting de acordo com um formato específico.

tempo_em_struct = time.localtime()
print(tempo_em_struct)

print(time.strftime('%d %B %Y', tempo_em_struct))
print(time.strftime('%H:%M:%S', tempo_em_struct))

tempo_formatado = time.strftime('%A, %d de %B de %Y, %H:%M:%S', tempo_em_struct)
print(f'Tempo formatado: {tempo_formatado}')

# Passar para o formato em português, podemos usar o módulo locale do Python

# Definir a localização para potuguês:
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime('%A, %d de %B de %Y, %H:%M:%S', tempo_em_struct)
print(f"Tempo formatado em pt-br: {tempo_formatado}")

print("----------------------------------------------------------------------------------------------------------------------------------")

# time.strptime() -> Analisa uma string representando um horário de acordo com um formato. O retorno é um objeto struct_time.

#string_tempo = "30 de Junho, 2023"
#formato = "%d %B, %Y"
#tempo_em_struct = time.strptime(string_tempo, formato)

#print(f"Tempo em struct: {tempo_em_struct}")

# Data em forma de dia/mês/ano
string_tempo = '06/09/2023'
formato = '%d/%m/%Y'
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")

# Data em forma de mês/dia/ano
string_tempo = "06/09/2023"
formato = "%m/%d/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")

print("----------------------------------------------------------------------------------------------------------------------------------")

# time.gmtime() -> Converte um tempo expresso em segundos desde a epoch em um objeto struct_time em UTC (Greenwich Mean Times).

# Tempo em UTC para 0 segundos desde a epoch
time.gmtime(0)

# Quando não colocamos nada como parâmetro, ela pega o atual
gmt_struct = time.gmtime()

print(f"Tempo em UTC: {gmt_struct}")

# Comparando com localtime
print(f"Tempo local: {time.localtime()}")

print(f"Tempo em UTC: {time.strftime('%A, %d de %B de %Y, %H:%M:%S', gmt_struct)}")

print(gmt_struct.tm_zone)

gmt_struct_exemplo = time.gmtime(1_234_567_890)

print(f"Tempo em UTC: {gmt_struct_exemplo}")

print(f"Tempo em UTC: {time.strftime('%A, %d de %B de %Y, %H:%M:%S')}")

print("----------------------------------------------------------------------------------------------------------------------------------")

# time.mktime() -> Converte um objeto struct_time em segundos desde a epoch. É o inverso da função localtime().
# Podemos converter o objeto struct_time retornado pela função localtime() em segundos desde a epoch usando a função mktime().
# O resultado deve ser o mesmo que o valor retornado pela função time().

tempo_em_struct = time.localtime()
tempo_em_segundos = time.mktime(tempo_em_struct)
print(f"Tempo em segundos: {tempo_em_segundos}")
print(f"Tempo em segundos: {time.time()}")

# Podemos usar esse método para calcular a diferença entre dois tempos. Exemplo: O tempo atual e o ínicio do ano.
# Podemos usar a função localtime() para obter o tempo atual e a função mktime() para obter o tempo em 1 de Janeiro de 2023.

tempo_atual = time.localtime()
tempo_ano_novo = time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0))

diferenca = time.mktime(tempo_atual) - tempo_ano_novo
print(f"Diferença em segundos: {diferenca}")
