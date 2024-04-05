print('/--ex58--/')

from random import randint
sort = randint(0, 10)
cont = 1
jogador = int(input('ecerte o número sorteado de 1 a 10: '))

while jogador != sort:
    if jogador < sort:
        print('\033[1;32mMAIS... tente mais uma vez\033[m')
        cont += 1
    else:
        print('\033[1;31mMENOS... tente mais uma vez\033[m')
        cont += 1
    jogador = int(input('acerte o nùmero sorteado: '))
print('\033[1;35mvocê acertou com {} tentativas\033[m'.format(cont))