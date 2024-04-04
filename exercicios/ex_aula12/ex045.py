print('/--ex45--/')
from random import randint
from time import sleep

print('''\033[1;33mPEDRA [ 0 ]\033[m
\033[1;32mPAPEL [ 1 ]\033[m
\033[1;34mTESOURA [ 2 ]\033[m''')

nome = input('nome do jogador: ')
user = int(input('pedra papel ou tesoura: '))
if user >= 3:
    print('escolha uma opção existente!')
else:
    if user == 0:
        user = 'pedra'
    elif user == 1:
        user = 'papel'
    else:
        user = 'tesoura'

    computer = randint(0,2)
    if computer == 0:
        computer = 'pedra'
    elif computer == 1:
        computer = 'papel'
    else:
        computer = 'tesoura'

    print('JO')
    sleep(.8)
    print('KEN')
    sleep(.8)
    print(f'''PO!!
----------------------------
\033[1;32mo jogador(a) {nome.upper()} jogou {user}\033[m
\033[1;31mo COMPUTADOR jogou {computer}\033[m
----------------------------''')

    if user == 'papel' and computer == 'pedra' or user == 'pedra' and computer == 'tesoura' or user == 'tesoura' and computer == 'papel':
        print(f'\033[1;32m{nome.upper()} venceu!!!\033[m')
    elif computer == 'papel' and user == 'pedra' or computer == 'pedra' and user == 'tesoura' or computer == 'tesoura' and user == 'papel':
        print('\033[4;31mcomputador venceu!!!\033[m')
    else:
        print('\033[33mEMPATE!!!\033[m')