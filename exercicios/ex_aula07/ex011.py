print('/--ex011--/')

altura = float(input('Qual a altura da sua parede: '))
largura = float(input('Qual a largura da sua parede: '))

area = altura * largura
tinta = area / 2

print(f'a altura da sua parede tem {altura}.')
print(f'a largura da sua parede tem {largura}.')
print(f'sua parede tem {area}m².')
print(f'voce deve comprar {tinta} litros de tinta para sua parede')