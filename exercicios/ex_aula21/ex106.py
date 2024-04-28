print('/--ex106--/')

def doc():
    def titulo(txt='', color=False):
        tio = len(txt) + 4
        if color != False:
            print(end=color)
        print('~' * tio)
        print(f'  {txt}')
        print('~' * tio)
        if color != False:
            print('\033[m', end='')
    def cor(enter=False, exit=False):
        if enter != False:
            print(end=enter)
        if exit != False:
            print(exit, end='')
    
    while True:
        titulo('SISTEMA DE AJUDA PYHELP', '\033[42m')
        fubi = str(input('Função ou biblioteca > ')).strip()
        if fubi == 'fim':
            cor(enter='\033[41m')
            titulo('ATÉ LOGO!')
            cor(exit='\033[m')
            break
        titulo(f"ACESSANDO O MANUAL DO COMANDO '{fubi}'", '\033[46m')
        cor(enter='\033[42m')
        help(fubi)
        cor(exit='\033[m')
doc()