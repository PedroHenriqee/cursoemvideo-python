print('/--ex62--/')

print('Gerador de PA')
print('-=-' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
quantidade_termo = 10

fim_programa = False
cont = 10

while fim_programa == False:
    print(termo, ' => ', end='')
    termo += razao
    cont -= 1
    
    if cont == 0:
        print('PAUSE')
        plus = int(input('\033[33mQUANTOS TERMOS VOCÊ QUER A MAIS?\033[m '))
        quantidade_termo += plus
        cont = plus
        if cont == 0:
            fim_programa = True

print(f'\033[1;35mPROGREÇÃO FINALIZADA COM {quantidade_termo} TERMOS MOSTRADOS\033[m')
print('\033[1;32mFIM DO PROGRAMA\033[m')