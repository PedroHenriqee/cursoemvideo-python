print('/--ex70--/')

print('-' * 35)
print(' ' * 7, 'LOJA SUPER BARATÃO')
print('-' * 35)

total = preco_1000 = mais_barato = 0
nome_mais_barato = ''

while True:
    produto = input('nome do produto: ').strip().upper()
    preco = float(input('preço R$'))

    total += preco

    if preco >= 1000:
        preco_1000 += 1

    if mais_barato == 0:
        mais_barato = preco
    elif mais_barato > preco:
        mais_barato = preco
        nome_mais_barato = produto

    parada = input('quer continuar? [S/N]: ').strip().upper()
    print('-' * 35)
    while parada not in 'SN':
        parada = input('quer continuar? [S/N]: ').strip().upper()
        print('-' * 35)
    if parada == 'N':
        break

print('-' * 9, 'FIM DO PROGRAMA', '-' * 9)
print(f'''\033[33m
O total da compra foi R${total}
Temos {preco_1000} produtos custando mais de R$1000.00
O produto mais barato foi {nome_mais_barato} que custa {mais_barato}\033[m''')