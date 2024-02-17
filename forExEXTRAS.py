"""
Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta.
Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.
"""

"""
1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas.
"""

vendas = [1000, 1500, 1200, 1300]
vendedores = ['Fulano', 'Beltrano', 'Ciclano', 'Lira']

for i in range(len(vendedores)):
    print("Vendedor: {} | Vendas: R${:,}".format(vendedores[i], vendas[i]))

for venda in vendas:
    media = sum(vendas) / len(vendas)
print("Média das Vendas: R${:,}".format(media))

print("_______________________________________________________________________________________________________________")

"""
2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.
"""

alunos = ['José', 'Joana', 'Maria', 'Carla', 'Mauricio', 'Andre', 'Tiago', 'Enzo', 'Amanda', 'Alessandra']
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3]
]

media = []
notasMaiores7 = 0

for i in range(len(alunos)):
    notasAluno = notas[i]
    mediaAluno = sum(notasAluno) / len(notasAluno)
    media.append(mediaAluno)

    if mediaAluno >= 7:
        notasMaiores7 += 1

    print(f"Aluno(a): {alunos[i]} | Média: {mediaAluno}")

print(f"\nMédias maiores de 7: {notasMaiores7}")

print("_______________________________________________________________________________________________________________")

"""
3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com mais de 25 anos possuem salário inferior à média de todos os salários.
"""

idades = [35, 32, 50, 33, 48, 50, 33, 48, 22, 49, 35, 38, 20, 47, 49, 48, 34, 21, 48, 44, 48, 30, 25, 42, 42, 23, 25,
          23, 38, 35]
salarios = [3739, 2219, 3554, 3978, 4014, 3270, 4792, 3879, 2981, 2384, 4826, 2460, 3680, 4318, 1872, 1770, 4640, 3929,
            3295, 1729, 3965, 4267, 4007, 1916, 2987, 2943, 3852, 4543, 2055, 1730]

salarioMenor = 0
mediaSalarial = sum(salarios) / len(salarios)

for i, idade in enumerate(idades):
    if idade > 25 and salarios[i] < mediaSalarial:
        salarioMenor += 1

print("Funcionários com mais de 25 anos com salário inferior à média de todos os salários: {}".format(salarioMenor))

print("_______________________________________________________________________________________________________________")

"""
4.Em quais meses a média de temperatura foi maior do que a média nacional?
"""

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']
temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

mediaNacional = sum(temperaturas) / len(temperaturas)

print("Média Nacional: {:.1f}ºC".format(mediaNacional))

for i, mes in enumerate(meses):
    if temperaturas[i] > mediaNacional:
        print("{}: {}ºC".format(mes, temperaturas[i]))

print("_______________________________________________________________________________________________________________")

"""
5. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. 
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo: 

Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
O programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. 

Ao final, o programa deverá apresentar:
    O salário de cada funcionário, juntamente com o valor do abono;
    O número total de funcionário processados;
    O valor total a ser gasto com o pagamento do abono;
    O número de funcionário que receberá o valor mínimo de 100 reais;
    O maior valor pago como abono.

A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.

Projeção de Gastos com Abono
"============================ 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00"
"""

lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
abonos = []

print("Salário  -   Abono")

contaMinimo = 0

for salario in lista_salarios:
    abono = salario * 0.2
    if abono < 100:
        abono = 100
    abonos.append(abono)

    if abono == 100:
        contaMinimo += 1

    print("R${}  -   R${}".format(salario, abono))

qtde = len(lista_salarios)
total = sum(abonos)
maximo = max(abonos)

print("Foram Processados {} colaboradores.".format(qtde))
print("Total gasto com abonos: R${:,}".format(total))
print("Valor mínimo pago a {} colaboradores.".format(contaMinimo))
print("Maior valor de abono pago: R${:,}".format(maximo))

print("_______________________________________________________________________________________________________________")

"""
6. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 

Calcule e mostre:
    a. O modelo do carro mais econômico;
    b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
    considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
    Os dados são fictícios e podem mudar a cada execução do programa.
    
Comparativo de Consumo de Combustível:

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
2 - gol             -   10.0 -  100.0 litros - R$ 225.00
3 - uno             -   12.5 -   80.0 litros - R$ 180.00
4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17

O menor consumo é do peugeout.
"""

veiculos = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeot']
autonomias = [7, 10, 12.5, 9, 14.5]

print('Comparativo de Consumo de Combustível\n')

for i, autonomia in enumerate(autonomias):
    print("Veículo {}".format(i + 1))
    print("Nome: {}".format(veiculos[i]))
    print("Km/L: {}\n".format(autonomias[i]))

print('Relatório Final\n')

for i, autonomia in enumerate(autonomias):
    litros = 1000 / autonomia
    valorTotal = litros * 2.25
    print(" {} | Nome: {} | Km/L: {:.1f} | Litros: {:.1f} | Valor: R${:.2f} |".format(i + 1, veiculos[i], autonomias[i],
                                                                                      litros, valorTotal))

print("_______________________________________________________________________________________________________________")

"""
7. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe R$200 por semana mais 9 por cento de suas vendas brutas daquela semana. 

Por exemplo, um vendedor que teve vendas brutas de R$3000 em uma semana recebe R$200 mais 9 por cento de R$3000, ou seja, um total de R$470. 

Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante

Existem várias formas de fazer. Faça primeiro da forma que parecer mais intuitiva para você.
Em seguida, caso queira um desafio:

Desafio: Crie uma forma para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

vendasLoja = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
contadores = [0] * len(vendasLoja)

for vendaLoja in vendasLoja:
    salarioFunc = 200 + 0.09 * vendaLoja
    if 200 <= salarioFunc < 300:
        contadores[0] += 1
    elif 300 <= salarioFunc < 300:
        contadores[1] += 1
    elif 400 <= salarioFunc < 500:
        contadores[2] += 1
    elif 500 <= salarioFunc < 600:
        contadores[3] += 1
    elif 600 <= salarioFunc < 700:
        contadores[4] += 1
    elif 700 <= salarioFunc < 800:
        contadores[5] += 1
    elif 800 <= salarioFunc < 900:
        contadores[6] += 1
    elif 900 <= salarioFunc < 1000:
        contadores[7] += 1
    else:
        contadores[8] += 1

for i, contador in enumerate(contadores):
    if i == 8:
        tot1 = i * 100 + 200
        print(f"+ R${tot1} | {contador} vendedor.")
    else:
        tot2 = i * 100 + 200
        tot3 = i * 100 + 299
        print(f"R${tot2} - R${tot3} | {contador} vendedor.")
