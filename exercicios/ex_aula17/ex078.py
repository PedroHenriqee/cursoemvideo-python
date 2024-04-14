print('/--ex78--/')

lista = list()
for lop in range(0, 5):
    lista += [int(input(f'Digite um valor para a posição {lop}: '))]
print('=-' * 20)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for indice, item in enumerate(lista):
    if item == max(lista):
        print(f'{indice}...', end=' ')
print(f'\nO menor valor foi {min(lista)} nas posições ', end='')
for indice, item in enumerate(lista):
    if item == min(lista):
        print(f'{indice}...', end=' ')