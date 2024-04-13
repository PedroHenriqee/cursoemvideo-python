print('/--ex77--/')

lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
cont_vogal = 0

for lop in lista:
    print(f'\nNa palavra {lop.upper()} temos ', end='')
    while cont_vogal < len(lop):
        if lop[cont_vogal] in 'aeiou':
            print(f'\033[33m{lop[cont_vogal]}\033[m ', end='')
        cont_vogal += 1
    cont_vogal = 0