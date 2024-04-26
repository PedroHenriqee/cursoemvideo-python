print('/--ex92--/')
from datetime import date

carteira = dict()
carteira['nome'] = str(input('Nome: '))
carteira['nasc'] = date.today().year - int(input('Ano de Nascimento: '))
carteira['ctps'] = int(input('Carteira de  Trabalho (0 não tem): '))

if carteira['ctps'] != 0:
    carteira['ano'] = int(input('Ano de Contratação: '))
    carteira['salario'] = float(input('Salário: '))
    carteira['aposentadoria'] = carteira['ano'] + 15 - (date.today().year - carteira['nasc'])
print('-=' * 30)

for key, val in carteira.items():
    print(f'-- {key} tem o valor {val}')