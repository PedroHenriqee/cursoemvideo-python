print('/--ex86--/')

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for lop in range(0, 3):
    for laço in range(0, 3):
        lista[lop][laço] = int(input(f'Digite o valor para [{lop}, {laço}]: '))
print('=-' * 30)

for lop in range(0, 3):
    for laço in range(0, 3):
        print(f'[{lista[lop][laço]:^5}]', end=' ')
    print()