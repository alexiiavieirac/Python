# Datetime em Python:

from datetime import datetime, timedelta
from datetime import date

# O módulo datetime() em Python fornece classes para manipulação de datas e horas.

# datetime.datetime.now() -> Retorna a data e a hora atuais

agora = datetime.now()
print(f"Agora: {agora}")

print(agora.date())
print(agora.time())

print(f"Ano: {agora.year}")
print(f"Mês: {agora.month}")
print(f"Dia: {agora.day}")
print(f"Hora: {agora.hour}")
print(f"Minuto: {agora.minute}")
print(f"Segundo: {agora.second}")

# datime.date.today() -> Retorna a data atual

hoje = date.today()
print(f"Data atual: {hoje}")

print(f"Ano: {hoje.year}")
print(f"Mês: {hoje.month}")
print(f"Fia: {hoje.day}")

# datetime.timedelta() -> É usada para realizar operações com datas (adição e subtração)

data_atual = datetime.now()
print(f"Data atual: {data_atual}")

data_futura = data_atual + timedelta(days=10)
print(f"Data futura: {data_futura}")

data_passada = data_atual - timedelta(days=10)
print(f"Data passada: {data_passada}")

dez_horas_adiante = data_atual + timedelta(hours=10)
print(f"Dez horas adiante: {dez_horas_adiante}")

dez_horas_antes = data_atual - timedelta(hours=10)
print(f"Dez horas antes: {dez_horas_antes}")

# Criação de um objeto datetime:
"""
Podemos criar um objeto datetime usando a classe datetime. O construtor da classe possuo como principais argumentos:
    - year: ano (2024)
    - month: mês (1-12)
    - day: dia (1-31)
    - hour: hora (0-23)
    - minute: minuto (0-59)
    - second: segundo (0-59)
    - microsecond: microssegundo (0-999999)
    - tzinfo: fuso horário
"""

data = datetime(2023, 7, 20, 8, 30, 20)
print(f"Data: {data}")

data = datetime(2024, 6, 25)
print(f"Data: {data}")

data = datetime(2024, 6, 25, 8, 30, 20, 100000)
print(f"Data/hora: {data}")

# fromisoformat() -> é um método de classe que converte uma string em um objeto datetime.

data_hora_iso = datetime.fromisoformat("2024-06-25 00:35:52")
print(f"Data/hora iso: {data_hora_iso}")

# Calcular a diferença entre duas datas subtraindo uma da outra:

# A diferença de duas datas gera um timedelta().

data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

diferenca = data2 - data1
print(f"Diferença das datas: {diferenca.days} dias.")
print(type(diferenca))

# Comparação entre duas datas:
# Podemos comparar duas datas usando os operadores de comparação padrão:
# passado < presente < futuro

data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

if data1 > data2:
    print("A data1 é posterior a data2.")
elif data1 < data2:
    print("A data1 é anterior a data2.")
else:
    print("As datas são iguais.")

data1 = datetime(2024, 2, 20, 15, 46, 30)
data2 = datetime(2024, 2, 20, 15, 46, 29)

if data1 > data2:
    print("A data1 é posterior a data2.")
elif data1 < data2:
    print("A data1 é anterior a data2.")
else:
    print("As datas são iguais.")

# Ordenando uma lista de datas:
# Função sorted para ordenar uma lista de datas.

datas = [
    datetime(2024, 6, 25),
    datetime(2024, 8, 14),
    datetime(2024, 5, 5),
    datetime(2024, 2, 7)
]

datas_ordenadas = sorted(datas)
print(datas_ordenadas)

for data in datas_ordenadas:
    print(data.date())
