print('/--ex51--/')

ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))
dec = ter + 10 * raz


for l in range(ter, dec, raz):
    print(l, end=' -> ')
print('acabou!!')