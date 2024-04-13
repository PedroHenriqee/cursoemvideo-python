print('/--ex75--/')

n1 = int(input('digite um número: '))
n2 = int(input('digite qualquer número: '))
n3 = int(input('digite outro numero: '))
n4 = int(input('digite um ultimo numero: '))

lista = (n1, n2, n3, n4)
print(f'Você digitou os seguintes números: {lista}')

print(f'O valor 9 apareceu {lista.count(9)} vezes.')
print(f'o valor 3 apareceu pela primeira vez na posição: {lista.index(3) if 3 in lista else ''}')
print('os numeros pares são: ', end='')
for lis in lista:
    if lis % 2 == 0:
        print(lis, end=', ')