print('/--ex033--/')

v1 = int(input('digite o primeiro valor: '))
v2 = int(input('digite o segundo valor: '))
v3 = int(input('digite o terceiro valor: '))

ma = v1
if v2 > v3 and v2 > v1:
    ma = v2
if v3 > v2 and v3 > v1:
    ma = v3

print(f'o maior valor é: {ma}')

me = v1
if v2 < v3 and v2 < v1:
    me = v2
if v3 < v2 and v3 < v1:
    me = v3

print(f'o menor valor é: {me}')