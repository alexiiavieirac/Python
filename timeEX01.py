# Exercício usando a biblioteca time()

import locale
import time

print("Primeiro Exercício")

# Contagem regressiva:
# Um evento especial está programado para começar em 10 segundos. Crie uma contagem regressiva que começa em 10 e vai até 0, com uma pausa de um segundo entre cada número.

for numero in range(10, 0, -1):
    print(numero, end=" \r")
    time.sleep(1)

print("O evento começou!")

print("---------------------------------------------")

print("Segundo Exercício")

# Formatação de tempo
# Uma empresa quer exibir a data e a hora atual em seu site no formato "Dia da semana, dia do mês de mês de ano, horas:minutos".
# Crie um script Python que mostra a data e a hora atuais neste formato.

# Definir a loc para português:
locale.setlocale(locale.LC_TIME, "pt-BR.UTF-8")

tempo_struct = time.localtime()
formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_struct)
print(f"Hora atual: {formatado}")

print("---------------------------------------------")

# \n pula linha:
print("Vai \n pular linha.")

# \t é o tab:
print("Olha \t o tab")

# print("", end=" \r") -> uma função print sem pular de linha em linha.
