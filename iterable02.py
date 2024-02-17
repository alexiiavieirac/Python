# Range

# range(tamanho)
# range(inicio, fim)
# range(inigio, fim, passo)

# Uso mais comum: Tamanho do range.
produtos = ['A', 'B', 'C', 'D', 'E']
estoque = [50, 100, 20, 5, 80]

for i in range(5):
    print('{}: {}'.format(produtos[i], estoque[i]))

# Range com início e fim: começa do 1 e termina no 9.
print(range(1, 10))

for i in range(1, 10):
    print(i)

# Exemplo: Modelo Jack Welch da G&E

# 1. Classe A: 10% melhor;
# 2. Classe B: 80% mantém/busca melhorar;
# 3. Classe C: 10% pior.

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

print('Funcionários Classe B')

for i in range(2, 18):
    print('{}: {} vendas.'.format(funcionarios[i], vendas[i]))

# Range com passo: podemos ver uma utilidade como exemplo para fazer um programa que salve os números do Whatts.
print(range(0, 1000, 100))

for i in range(0, 1000, 10):
    print(i)
