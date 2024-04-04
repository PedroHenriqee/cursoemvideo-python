print('/--ex031--/')

distancia = float(input('digite a distancia da viagem: '))
print('você esta prestes a começar uma viagem de {}Km.'.format(distancia))

# if distancia <= 200:
#     distancia = distancia * 0.50
#     print(f'o valor da sua passagem é de R${distancia}')
# else:
#     distancia = distancia * 0.45
#     print(f'o valor da sua passagem é de R${distancia}')

print(f'o valor da sua passagem ficou {distancia * 0.50}' if distancia <= 200 else 'o valor da sua passagem ficou {}'.format(distancia * 0.45))