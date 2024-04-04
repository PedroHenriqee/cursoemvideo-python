print('/--ex50--/')

par = 0
for l in range(1, 7):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        par += num
print('\033[1;32ma soma dos numeros pares é {}\033[m'.format(par))