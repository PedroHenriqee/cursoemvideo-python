print('/--ex59--/')
from time import sleep

pv = int(input('primeiro valor: '))
sv = int(input('segundo valor: '))
programa = False
while not programa:
    print('''    \033[1;33m[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa\033[m''')
    opcao = int(input('\033[32m>>>>>>qual é a sua opção?\033[m '))
    if opcao < 1 or opcao > 5:
        print('\033[1;31m!!ERRO. ESCOLHA UMA OPÇÃO EXISTENTE!!\033[m')
    else:
        if opcao == 1:
            print(f'\033[36ma soma entre {pv} + {sv} é {pv + sv}\033[m')
        elif opcao == 2:
            print(f'\033[36ma multiplicação entre {pv} X {sv} é {pv * sv}\033[m')
        elif opcao == 3:
            print(f'\033[36mo maior número é o {pv}\033[m' if pv > sv else f'\033[36mo maior número é {sv}\033[m')
        elif opcao == 4:
            print('informe os números novamente:')
            pv = int(input('primeiro valor: '))
            sv = int(input('segundo valor: '))
        else:
            print('\033[1mFinalizando...\033[m')
            programa = True
        print('\033[1m=-=\033[m' * 15)
        sleep(1)
print('fim do programa')