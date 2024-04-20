print('/--ex88--/')

from random import randint
from time import sleep

print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 6, f'SORTEANDO {jogos} JOGOS', '-=' * 6)

lista = []
lista_tot = []
for lop in range(0, jogos):
    while True:
        sort = randint(1, 60)
        if sort not in lista:
            lista.append(sort)
        if len(lista) == 6:
            break
    lista.sort()
    print(f'Jogo {lop + 1}: {lista}')
    lista_tot.append(lista[:])
    lista.clear()
    sleep(.8)
print('-=' * 8, '< BOA SORTE >', '-=' * 8)