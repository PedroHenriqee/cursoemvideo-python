print('/--ex76--/')

print('-' * 45)
print(f'\033[1;33m{"LISTAGEM DE PREÇOS":^35}\033[m')
print('-' * 45)

produtos = ('lápis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'transferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)

for lop in produtos:
    if type(lop) == str:
        tamanho = 33 - len(lop)
        print(lop, end='')
        print('.' * tamanho, end='')
    else:
        print(f'R$ {lop:>6.2f}')
print('-' * 45)