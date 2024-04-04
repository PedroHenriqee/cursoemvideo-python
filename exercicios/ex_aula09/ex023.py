print('/--ex023--/')

#forma simples:

# num = input('Digite um numero: ')
# print('seu numero é {} e ele possui:'.format(num))
# print(f'unidades: {num[3:4]}')
# print(f'dezenas: {num[2:3]}')
# print(f'centenas: {num[1:2]}')
# print(f'milhares: {num[0:1]}')

#formar mais complexa:

num = input('digite um numero: ')

if len(num) == 4:
    print('seu numero é {} e ele possui:'.format(num))
    print(f'unidades: {num[3:4]}')
    print(f'dezenas: {num[2:3]}')
    print(f'centenas: {num[1:2]}')
    print(f'milhares: {num[0:1]}')

if len(num) == 3:
    print('seu numero é {} e ele possui:'.format(num))
    print(f'unidades: {num[2:3]}')
    print(f'dezenas: {num[1:2]}')
    print(f'centenas: {num[0:1]}')
    print(f'milhares: 0')

if len(num) == 2:
    print('seu numero é {} e ele possui:'.format(num))
    print(f'unidades: {num[1:3]}')
    print(f'dezenas: {num[0:1]}')
    print(f'centenas: 0')
    print(f'milhares: 0')

if len(num) == 1:
    print('seu numero é {} e ele possui:'.format(num))
    print(f'unidades: {num}')
    print(f'dezenas: 0')
    print(f'centenas: 0')
    print(f'milhares: 0')