print('/--ex69--/')

cont = cont_h = cont_m = color = 0
while True:
    if color % 2 == 0:
         print('\033[36m')
         color += 1
    else:
         print('\033[34m')
         color += 1

    print('-' * 32)
    print(' ' * 6, 'CADASTRAR PESSOAS')
    print('-' * 32)
    idade = int(input('idade: '))
    sexo = input('sexo: [M/F] ').strip().upper()
    while sexo not in 'FM':
         sexo = input('sexo: [M/F] ').strip().upper()

    if idade > 18:
            cont += 1
    if sexo == 'M':
            cont_h += 1
    if sexo == 'F' and idade < 20:
         cont_m += 1

    print('-' * 32)
    continuar = input('quer continuar?: [S/N] ').strip().upper()
    while continuar not in 'SN':
          continuar = input('qur continuar?: [S/N] ').strip().upper()
    if continuar == 'N':
          break

print(f'''
\033[33mTotal de pessoas com mais de 18 anos: {cont}
Ao todo temos {cont_h} homens cadastrados
E temos {cont_m} mulheres com menos de 20 anos\033[m''')