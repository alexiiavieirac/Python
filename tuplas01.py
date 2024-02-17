vendas = ('Aléxia', '08/01/2024', '25/06/2005', 2000, 'Estagiária')

# Podemos mostrar dessa forma as tuplas, mas lembrando sempre que deve-se colocar me ordem!
nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(data_nascimento)

print('----------------------------------------------')

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(f'Nome: {nome}')
print(f'Data de Contratação: {data_contratacao}')
print(f'Data de Nascimento: {data_nascimento}')
print(f'Salário: R${salario:.2f}')
print(f'Cago: {cargo}')
