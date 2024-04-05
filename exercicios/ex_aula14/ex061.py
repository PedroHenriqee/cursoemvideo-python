print('/--ex61--/')

print('Gerador de PA')
print('-=' * 20)

first = int(input('Primeiro termo: '))
razao = int(input('Razão de PA: '))
cont = 0

while cont < 10:
    print(first, ' =>', end=' ')
    first += razao
    cont += 1
print('FIM')