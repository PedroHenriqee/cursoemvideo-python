print('/--ex74--/')

from random import randint

# ex feito com listas
# numeros = []
# for l in range(0, 5):
#     sorteio = randint(0, 10)
#     numeros += [sorteio]

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os números sorteados foram: {numeros}')
print(f'O maior nùmero sorteado foi: {sorted(numeros)[-1]}')
print(f'O menor número sorteado foi: {sorted(numeros)[0]}')