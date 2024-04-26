print('/--ex98--/')

def contagem(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for lop in range(i, f, p):
        print(lop, end=' ')
    print('FIM!')

print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
for lop in range(0, 10):
    print(lop+1, end=' ')
print('FIM!')
print('-=' * 30)

print('Contagem de 0 até 10 de 2 em 2')
for lop in range(10, 0, -2):
    print(lop, end=' ')
print('0', 'FIM!')
print('-=' * 30)

print('Agora é sua vez de personalizar a contagem')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 30)
contagem(inicio, fim, passo)