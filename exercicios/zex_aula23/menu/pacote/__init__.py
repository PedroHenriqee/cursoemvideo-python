from time import sleep

def formatado(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)

def menu(*itens):
    sleep(.8)
    formatado('MENU PRINCIPAL')
    for key, lop in enumerate(itens):
        print(f'\033[33m{key+1} -\033[m \033[36m{lop}\033[m')
    print('-' * 40)
    return itens

def opcao():
    list = [1, 2, 3]
    try:
        opc = int(input('\033[33mSua opção:\033[m '))
        confirm = list[opc - 1]
    except ValueError:
        print('\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
    except IndexError:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    else:
        return opc
        
def escolha(it, opc):
    formatado(it[opc])