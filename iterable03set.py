# Set

# meu_set = {valor, valor, valor...}

# Observações:
# Não pode ter valores duplicados;
# Não tem ordem fixa.

# Obs.: É importante, pois já que quando temos valores duplicados, ele tira da lista, não o coloca. Além de não ser um dicionário, mas sim um ‘set’ com apenas valor.

set_produtos = {'A', 'B', 'C', 'D', 'E'}
print(set_produtos)

# Aplicação bem útil:
# 1. Quantos clientes tivemos na loja?

cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

set_cpf_clientes = set(cpf_clientes)
set_cpf_unicos = list(set_cpf_clientes)

print(set_cpf_unicos)
print('Temos {} clientes na loja.'.format(len(set_cpf_clientes)))
