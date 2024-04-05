print('/--ex57--/')

c = 1
while c != 0:
    sexo = input('digite seu sexo [M/F]: ').lower().strip()
    if sexo in 'mf':
        print(f'seu sexo é {'\033[1;32mmasculino\033[m' if sexo == 'm' else '\033[1;35mfeminino\033[m'}.')
        print('conta registrada com sucesso!')
        c = 0
    else:
        print(f'{sexo} não é um sexo!')