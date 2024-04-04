print('/--ex36--/')

casa = float(input('valor da casa: R$'))
sal = float(input('seu salario: R$'))
tempo = int(input('em quantos você deseja pagar?: '))

mensal = casa / (tempo * 12)
print('você vai pagar {}R$ por ano para quitar a casa!'.format(mensal))
sal30 = sal * 0.30
print('30% do seu salario é: {}R$'.format(sal30))

if mensal > sal30:
    print('prestação não realizada! o valor da casa exede os 30% do salario!')
else:
    print('prestação realizada!')