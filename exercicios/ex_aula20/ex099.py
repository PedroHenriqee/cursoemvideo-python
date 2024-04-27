print('/--ex99--/')

def valores(*val):
    print('=-' * 30)
    print('Analizando os valores passados...')
    maior = 0
    for key, lop in enumerate(val):
        if maior < val[key]:
            maior = val[key]
        print(lop, end=' ')
    print(f'Foram informados {len(val)} valores ao todo')
    print(f'O maior valor informado foi {maior}')

valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()
print('=-' * 30)
