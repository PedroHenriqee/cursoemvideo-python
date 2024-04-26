print('/--ex96--/')

def area(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m².')

print('Controle de Terrenos')
print('-' * 20)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lar, comp)