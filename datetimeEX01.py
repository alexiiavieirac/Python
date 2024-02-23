# Exercícios de Datetime e ZoneInfo:

"""
Oferecendo desconto para cliente com base na última compra

Suponha que você está trabalhando em uma empresa que deseja rastrear a atividade do cliente. Uma métrica que eles estão interessados
é o tempo que passou desde a última transação do cliente. Se for muito tempo, eles podem oferecer um desconto para o cliente. Crie
um script Python que mostra quanto tempo se passou desde a última compra do cliente (10 de maio de 2023). Se faz mais de 30 dias,
mostre uma mensagem oferecendo um desconto para o cliente.
"""

# Biblioteca datetime para pegar a data e as horas atuais.
# Pegar a data da última compra do cliente (10 de maio de 2023).
# Calcular a diferença entre as datas.
# Se a data da última compra for maior que 30 dias, mandar uma mensagem dizendo sobre um desconto.
# Mostra na tela.

from datetime import datetime

data_atual = datetime.now()
print(f"Data atual: {data_atual.date()}")

data_cliente = datetime(2023, 5, 10)

diferenca = data_atual - data_cliente
print(f"Tempo desde a última compra: {diferenca}")

if diferenca.days > 30:
    print("Nós temos um desconto incrível para você!")

"""
Data e hora em diferentes fusos horários

Uma empresa tem escritórios em São Paulo, Nova York e Tóquio. Crie um script Python que mostra a data e hora atuais neses três
fusos horários. Exiba, também, se estes escritórios estão abertos ou fechados (9h às 17h).
"""

# Saber primeiro sobre o horário de meu fuso e assim descobrir a diferença entre os fusos.
# Importar a biblioteca datetime para saber e pegar as minhas informações de data e hora:
#   data_hora_atual = datetime.now()
# Importar a biblioteca timezone ou zoneinfo para pegar o fuso horário dos lugares (Nova York, São Paulo e Tóquio).
#   fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
#   data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
#   print(f"Data/hora em São Paulo: data_hora_sao_paulo")
#   fuso_horario_ny = ZoneInfo('America/New_York')
#   data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
#   print(f"Data/hora em Nova York: data_hora_ny")
#   fuso_horario_toquio = ZoneInfo('Asian/Japan')
#   data_hora_toquio = data_hora_atual.astimezone(fuso_horario_toquio)
#   print(f"Data/hora em Tóquio: data_hora_toquio")
# Mostrar se o escritório estará aberto ou fechado conforme o horário (9h às 17h).
#   if data_hora_sao_paulo > 9 and data_hora_sao_paulo < 17:
#       print("Escritório está aberto.")
#   else:
#       print("Escritório está fechado.")

"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

data_hora_atual = datetime.now()
print(f"Data/hora atuais: {data_hora_atual}")

fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
print(f"Data/hora em São Paulo: {data_hora_sao_paulo}")

fuso_horario_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
print(f"Data/hora em New York: {data_hora_ny}")

fuso_horario_toquio = ZoneInfo('Asia/Tokyo')
data_hora_toquio = data_hora_atual.astimezone(fuso_horario_toquio)
print(f"Data/hora em Tóquio: {data_hora_toquio}")

def verifica_horario(data_hora):
    if 9 <= data_hora.hour < 17:
        return "Aberto"
    else:
        return "Fechado"

print(f"Escritório de São Paulo: {verifica_horario(data_hora_sao_paulo)}")
print(f"Escritório de New York: {verifica_horario(data_hora_ny)}")
print(f"Escritório de Tóquio: {verifica_horario(data_hora_toquio)}")

Outra forma de fazer, mas é mais manual e menos automatizado:
    if data_hora_sao_paulo > 9 and data_hora_sao_paulo < 17:
      print("Escritório aberto.")
    else:
      print("Escritório fechado.")
      
    if data_hora_ny > 9 and data_hora_ny < 17:
      print("Escritório aberto.")
    else:
      print("Escritório fechado.")
      
    if data_hora_toquio > 9 and data_hora_toquio < 17:
      print("Escritório aberto.")
    else:
      print("Escritório fechado.")
"""
