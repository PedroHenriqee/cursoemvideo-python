print('/--ex53--/')

#### FORMA COM O FOR ####
frase = input('digite a frase: ').upper().strip().split()
frase_junta = ''.join(frase)
frase_contrario = ''

for cont in range(len(frase_junta),-1 ,-1):
    frase_contrario += frase_junta[cont:cont+1]
print(f'sua frase foi \033[1;33m{frase_junta}\033[m e ela ao contrario é \033[1;33m{frase_contrario}\033[m')

if frase_junta == frase_contrario:
    print('\033[1;32msua frase é um palindromo!!\033[m')
else:
    print('\033[1;31msua frase não é um palindromo!!\033[m')

#### FORMA FACIL, SEM O FOR ####
# nome = input('nome: ').strip().upper().split()
# nome_junto = ''.join(nome)
# nome_contrario = nome_junto[::-1]

# print(f'o texto digitado: \033[1;32m{nome_junto}\033[m')
# print(f'o texto ao contrario: \033[1;32m{nome_contrario}\033[m')

# if nome_junto == nome_contrario:
#    print('o texto é um palindromo')
# else:
#    print('o texto nao é um palindromo')