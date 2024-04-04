print('/--ex37--/')

num = int(input('digite um número: '))

print(f"""\033[4mseu número é o \033[35m{num}\033[m\033[m.
agora escolha uma das opções abaixo para
que ele \033[33mseja convertido\033[m:
[1] binário
[2] octal
[3] hexadecimal""")
select = int(input('digite uma das opções acima (1, 2, 3): '))

if select == 1:
    bi = bin(num)
    print(f'{str(bi)[2:]} -> \033[32mBINARIO\033[m')
elif select == 2:
    oc = oct(num)
    print(f'{str(oc)[2:]} -> \033[32mOCTAL\033[m')
elif select == 3:
    hx = hex(num)
    print(f'{hx} -> \033[32mHEXADECIMAL\033[m')
else:
    print('\033[31mopção invalida! escolha uma opção existente e tente novamente (1, 2, 3)\033[m')