print('/--ex003--/')

num1 = input('digite um valor:')
num2 = input('digite outro valor:')
print('*+*')
print('*-*')
print('*x*')
print('*/*')
oper = input('escreva a operação que ira ser feita sobre os dois algarismos acima:')
print('')

if num1 == '' or num2 == '' or oper == '':
    print('preencha todos os campos acima:')

if oper == '+':
    print(f'a soma entre {num1} e {num2} é: {int(num1) + int(num2)}')
else:
    pass

if oper == '-':
    print(f'a conta de {num1} menos {num2} é: {int(num1) - int(num2)}')
else:
    pass

if oper == 'x':
    print('a conta de {} multiplicado por {} é: {}'.format(num1, num2, int(num1) * int(num2)))
else:
    pass

if oper == '/':
    print('a conta de {} dividido por {} é: {}'.format(num1, num2, int(num1) / int(num2)))