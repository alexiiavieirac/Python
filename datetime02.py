# Guia para o módulo datetime em Python
# O módulo datetime em Python dornece classes para manipulação de datas e horas.

from datetime import datetime, timezone, timedelta
import locale

# datetime.datetime.strftime() -> Converte um objeto datetime para uma string de acordo com um formato específico

agora = datetime.now()
print(agora)
print(type(agora))

print(agora.strftime(""))

data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")
print(f"Data formatada: {data_formatada}")
print(type(data_formatada))

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

agora = datetime.now()
data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")
print(f"Data formatada: {data_formatada}")

# datetime.datetime.strptime() -> Analisa uma string representando uma data e hora de acordo com um formato. O retorno é um objeto datetime.

string_data = "30 Junho, 2023, 15:30:20"
formato = "%d %B, %Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)
print(f"Data: {data} | Tipo:", type(data))

# Formato: DD/MM/YYYY
string_data = "20/02/2024, 16:29:45"
formato = "%d/%m/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)
print(f"Data: {data}")

# Formato: MM/DD/YYYY
string_data = "02/20/2024, 16:29:45"
formato = "%m/%d/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)
print(f"Data: {data}")

# Trabalhando com fuso horário
"""
Podemos criar um objeto datetime usando a classe datetime:
    - year: ano (2024);
    - month: mês (1-12);
    - day: dia (1-31);
    - hour: hora (0-23);
    - minute: minuto (0-59);
    - second: segundo (0-59);
    - microsecond: microssegundo (0-999999);
    - tzinfo: fuso horário.
"""

data_hora = datetime(2024, 6, 25, 16, 30, 25)
print(f"Data/hora: {data_hora}")

# Os horários que vimos até o momento são os que chamamos de ingênuos (naive). Eles não possuem informações sobre o fuso horário.
# Para criar um horário consciente (aware), precisamos passar um objeto tzinfo para o construtor da classe datetime.
# O módulo datetime fornece uma classe timezone que pode ser usada para criar um objeto tzinfo.
# UTC: Tempo Universal Coordenado, que é o fuso horário de referência a partir do qual todos são calculados, e ele é +00:00.

fuso_horario = timezone.utc
data_hora = datetime(2024, 6, 25, 16, 39, 45, tzinfo=fuso_horario)
print(f"Data/hora: {data_hora}")

# Podemos passar um objeto timedelta para construtor da classe timezone para criar um fuso horário com um deslocamento específico.

fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
data_hora = datetime(2024, 2, 20, 16, 42, 14, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")

# Como alternativa, podemos usar o módulo zoneinfo para criar um objeto tzinfo. O módulo zoneinfo fornece uma classe ZoneInfo que pode ser
# usada para criar um objeto tzinfo.

"""
from zoneinfo import ZoneInfo

fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")
"""

# Conversão entre fusos horários: Podemos converter um fuso horário para outro.
"""
data_hora_atual = datetime.now() -> now é naive, sem fuso horário.
print(f"Data/hora atual (fuso horário local): data_hora_atual")

fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
print(f"Data/hora atual em São Paulo: data_hora_sao_paulo")

fuso_horario_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
print(f"Data/hora atual em São Paulo: data_hora_ny")
"""
