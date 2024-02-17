# Estrutura While

# Usamos o whiule quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.
# A lógica é: enquanto a condição for verdadeira, o while executa o código. Assim que ela terminar de ser verdadeira, o código "sai" do while.

"""
while condicao:
    repete esse código
"""

"""
Aplicações do WHILE:
    1. Quando criamos uma automação na internet.
        Ex: Quando estamos querendo entrar no WhatsApp Web e ele fica carregando, o código não será executado até que a página carregue e assim consiga fazer o resto do código.
    
    2. Crie um programa que funcione como o registro de vendas de uma empresa.
       Nela a pessoa deve inserir o nome do produto e o produto deve ser adicionado na lista de venda. Enquanto o usuário não encerrar o programa, significa que ele está
       registrando novos produtos, então o programa deve permitir a entrada de quantos produtos o usuário quiser.
"""

print("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia.")

venda = input("Produto: ")
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input("Produto: ")

print("Registro finalizado. Os produtos cadastrados foram: {}".format(vendas))
