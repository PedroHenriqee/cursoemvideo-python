print('/--ex68--/')
from random import randint
from time import sleep

cont = 0
derrota = 0

print('\033[31m-=\033[m' * 20)
print('vamos jogar par ou impar!')
print('\033[36m-=\033[m' * 20)

while True:
    if derrota > 0:
        cont = 0
    
    comp = randint(1, 11)
    val = int(input('digite um valor: '))
    parimpar = input('par ou impar [P/I]: ').upper().strip()[0]

    if parimpar in 'PI':
        if (comp + val) % 2 == 0:
            print('-' * 40)
            print(f'\033[32mvocê jogou {val}\033[m e o \033[31mcomputador {comp}\033[m. Total de \033[33m{comp + val}\033[m DEU \033[33mPAR\033[m')
            print('-' * 40)
        else:
            print('-' * 40)
            print(f'\033[32mvocê jogou {val}\033[m e o \033[31mcomputador {comp}\033[m. Total de \033[33m{comp + val}\033[m DEU \033[33mÍMPAR\033[m')
            print('-' * 40)
        if parimpar == 'P' and (comp + val) % 2 == 0 or parimpar == 'I' and (comp + val) % 2 != 0:
            print('\033[32mvocê VENCEU!\033[m')
            print('Vamos jogar novamente...')
            print('-=' * 20)
            sleep(1)
        else:
            print('\033[31mVocê perdeu!\033[m')
            print('-=' * 20)
            print(f'GAME OVER! Você venceu \033[33m{cont}\033[m vezes.')
            game_over = int(input('quer recomeçar? [ 0 -> NÃO/ 1 -> SIM ]: '))
            if game_over == 0:
                break
            else:
                derrota += 1
        cont += 1
    else:
        print('ERRO! JOGUE NOVAMENTE E ESCOLHA ENTRE P/I')
print('FIM DE JOGO!')