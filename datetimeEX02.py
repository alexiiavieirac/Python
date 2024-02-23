# Calculando a idade:
# Um usuário fornece sua data de nascimento no formato "DD/MM/YYYY". Crie um script Python que calcula a idade do usuário.

# Devemos pedir a data de nascimento da pessoa, no formato DD/MM/YYYY.
# Devemos calcular a idade do usuário:
#   Fazer a data atual - data de nascimento;
#   Fazer a verificação dos meses;
#   Fazer a verificação dos dias.
# Printar na tela.

from datetime import datetime

data_nascimento_usuario = input("DD/MM/YYY: ")
print(f"Data de Nascimento do Usuário: {data_nascimento_usuario} | Tipo: {type(data_nascimento_usuario)}")

data_nascimento_usuario = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")
print(f"Data formatada: {data_nascimento_usuario.date()} | Tipo: {type(data_nascimento_usuario)}")

data_atual = datetime.now()
print(f"Data atual formatada: {data_atual} | Tipo: {type(data_atual)}")

# Dará 19, pois não estou verificando os dias e os meses, apenas os anos:
print("Sem tratar os meses e os dias:")
idade = data_atual.year - data_nascimento_usuario.year
print(f"Idade: {idade}")

mes_atual = data_atual.month
dia_atual = data_atual.day

mes_nascimento = data_nascimento_usuario.month
dia_nascimento = data_nascimento_usuario.day

if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1

print("Tratando os meses e os dias:")
print(f"Idade: {idade}")
