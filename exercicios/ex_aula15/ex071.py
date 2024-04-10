print('/--ex71--/')

print('=' * 35)
print(' ' * 9, 'BANCO PHH')
print('=' * 35)

valor = int(input('qual valor quer sacar?: \033[32mR$\033[m'))
sed_100 = sed_50 = sed_10 = sed_5 = sed_1 = 0

# cédulas de 100.00R$
while valor >= 100:
    valor -= 100
    sed_100 += 1

# cédulas de 50.00R$
while valor >= 50:
    valor -= 50
    sed_50 += 1

# cédulas de 10.00R$
while valor >= 10:
    valor -= 10
    sed_10 += 1

# cédulas de 5.00R$
while valor >= 5:
    valor -= 5
    sed_5 += 1

# cédulas de 1.00R$
while valor >= 1:
    valor -= 1
    sed_1 += 1

print(f'Total de \033[33m{sed_100}\033[m céduas de R$100')
print(f'Total de \033[33m{sed_50}\033[m cédulas de R$50')
print(f'Total de \033[33m{sed_10}\033[m cédulas de R$10')
print(f'Total de \033[33m{sed_5}\033[m cédulas de R$5')
print(f'Total de \033[33m{sed_1}\033[m cédulas de R$1')
print('=' * 35)
print('Obrigado por usar o nosso banco. tenha um bom dia!')