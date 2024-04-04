print('/--ex020--/')
a1 = input('Primeiro aluno: ')
a2 = input('Segunda aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')

from random import shuffle

lista_name = [a1, a2, a3, a4]
shuffle(lista_name)

print(f'a ordem é: {lista_name}')