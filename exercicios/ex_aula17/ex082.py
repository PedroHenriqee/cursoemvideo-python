print('/--ex82--/')

lista = list()
par = list()
imp = list()
while True:
    lista.append(int(input('Digite um número: ')))
    if lista[-1] % 2 == 0:
        par.append(lista[-1])
    else:
        imp.append(lista[-1])
    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
print('-=' * 25)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímapares é {imp}')