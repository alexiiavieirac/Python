# Desafio: Tempo até o próximo ano

import time

# Saber o tempo atual:
#   Utilizar o time.localtime() para pegar as informações do dia atual.
# Identificar o próximo ano, dia, mês, etc, do próximo ano:
#   Podemos fazer o código ficar mais dinâmico ainda:
#       Pegar a informação do ano com o tm_year e assim conseguimos somar 1, pois como estamos pegando o tempo real, ele adicionará 1 independente de quando o código for executado.
# Devemos pegar as informações acumuladas e fazer a diferença delas para os segundos:
#   segundos_restantes = int(time.mktime(variável)) - time.mktime(variável) -> Colocamos int(), pois só nos interessa, por enquanto, a parte inteira.
# Transformar tudo em segundos para fazer as contas:
#   Utilizaremos aqui o time.mktime(), já que ele transforma para segundos.
# Transformar os segundos em dia, hora, minuto e segundo:
#   minuto = 60 segundos é 1min;
#   hora = 60 min * 60 seg, pois 60seg é 1min e 60min é 1h;
#   dia = 24h * 60min * 60seg, pois o dia tem 24h e cada hora tem 60min e cada minuto tem 60seg.
# Depois de feito os tratamentos para segundos, faremos a modificação para cada dia, hora, minuto e segundo que queremos:
#   resultado, resto = divmod(130, segundos_por_minuto);
#   dias, resto_segundos = divmod(resto_segundos, segundos_por_dia);
#   hora, resto_segundos = divmod(resto_segundos, segundos_por_hora);
#   minutos, segundos = divmod(resto_segundos, segundos_por_minuto).
# Printar na tela os dias, horas, minutos e segundos que faltam para o ano novo.

tempo_atual = time.localtime()
print(tempo_atual)

print(f"Ano atual: {tempo_atual.tm_year}")

tempo_ano_novo = (tempo_atual.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)

print(f"Segundos tempo atual: {time.mktime(tempo_atual)} segundos")
print(f"Segundos ano novo: {time.mktime(tempo_ano_novo)} segundos")

resto_segundos = int(time.mktime(tempo_ano_novo)) - time.mktime(tempo_atual)
print(f"Diferença entre os segundos atuais e os do ano novo: {resto_segundos} segundos")

# Segundos por minuto = 60, pois cada minuto possui 60seg:
segundos_por_minuto = 60
# Segundos por hora = 60 * 60, pois cada minuto tem 60seg e cada hora tem 60min:
segundos_por_hora = 60 * 60
# Segundos por dia = 24 * 60 * 60, pois cada dia tem 24h, cada hora 60min e cada min tem 60seg:
segundos_por_dia = 24 * 60 * 60

print(f"Segundos por minuto: {segundos_por_minuto} segundos")
print(f"Segundos por hora: {segundos_por_hora} segundos")
print(f"Segundos por dia: {segundos_por_dia} segundos")

# O resto_segundos é o que deu de resultado sobre a diferença dos segundos atuais e os do ano novo e foi dividido pela quantidade de
# segundos por minuto, que é 60, e assim foi feito uma tupla com dois valores, o inteiro e o resto:
resultado, resto = divmod(resto_segundos, segundos_por_minuto)
# Pegamos o resto_segundos e dividimos pela quantidade de segundos por dia para sabermos a quantidade de dias que faltam:
dias, resto_segundos = divmod(resto_segundos, segundos_por_dia)
# Pegamos o resto_segundos e dividimos pela quantidade de segundos por hora para sabermos a quantidade de horas restantes:
horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)
# Pegamos o resto_segundos e dividimos pela quantidade de segundos por minuto para sabermos a quantidade de minutos restantes e
# o que sobrou é designado a ser os segundos finais:
minutos, segundos = divmod(resto_segundos, segundos_por_minuto)

print(f"Faltam {dias} dias, {horas} horas. {minutos} minutos e {segundos} segundos para o Ano Novo!")
