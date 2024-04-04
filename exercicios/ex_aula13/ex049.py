print('/--ex49--/')

tab = int(input('\033[1mdigite um numero:\033[m '))
print(f'\033[1;35mtabuada do {tab}:\033[m')

cont = 0
for c in range(1, 11):
    cont += 1
    print('\033[1;32m{} x {:2} =\033[m \033[1;33m{:2}\033[m'.format(tab, cont, tab * cont))