print('/--ex87--/')

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira_col = maior_segunda = 0

for lop in range(0, 3):
    for laço in range(0, 3):
        lista[lop][laço] = int(input(f'Digite um número [{lop}, {laço}]: '))
        if lista[lop][laço] % 2 == 0:
            par += lista[lop][laço]
        if laço == 2:
            terceira_col += lista[lop][laço]
        if lop == 1 and maior_segunda == 0:
            maior_segunda = lista[lop][laço]
        else:
            if lop == 1 and lista[lop][laço] > maior_segunda:
                maior_segunda = lista[lop][laço]
print('=-' * 30)

for lop in range(0, 3):
    for laço in range(0, 3):
        print(f'[{lista[lop][laço]:^5}]', end=' ')
    print()
print('=-' * 30)

print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {terceira_col}')
print(f'O maior valor da segunda linha é {maior_segunda}')