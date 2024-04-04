print('/--ex52--/')

cont = 0
num = int(input('digite um numero: '))

for l in range(1, num + 1):
    if num % l == 0:
        print('\033[33m', l, '\033[m', end=' ')
        cont += 1
    else:
        print('\033[31m', l, '\033[m', end=' ')

print('')
if cont == 2:
    print(f'o numero {num} foi dividido {cont} vezes')
    print('por isso ele é primo!!')
else:
    print(f'o numero {num} foi dividido {cont} vezes')
    print('por isso ele neo é primo!!')