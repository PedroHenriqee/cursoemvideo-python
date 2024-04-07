print('/--ex46--/')
from time import sleep

s_n = 's'
cont = soma_med = 0

print('\033[1;36m-\033[m' * 50)

while s_n == 's':
    num = int(input('digite um número: '))
    s_n = input('quer continuar? [S/N]: ').lower().strip()[0]

    cont += 1
    soma_med += num

    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

print('\033[1;36m-\033[m' * 50)
sleep(1)

print(f'\033[33mvocê digitou {cont} números e a média foi {soma_med / cont}')
print(f'o maior valor foi {maior} e o menor foi {menor}\033[m')