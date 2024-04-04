print('/--ex19--/')

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

import random

sort = random.randint(1, 4)
if sort == 1:
    print(f'o aluno escolhido foi {a}')
if sort == 2:
    print(f'o aluno escolhido foi {b}')
if sort == 3:
    print(f'o aluno escolhido foi {c}')
if sort == 4:
    print(f'o aluno escolhido foi {d}')