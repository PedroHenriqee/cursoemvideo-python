print('/--ex028--/')

from random import randint
from time import sleep

print('-=-' * 20)
print('vou pensar em um numero de 0 a 5')
print('-=-' * 20)
comp = randint(0, 5)

numero = int(input('digite um numero entre 0 e 5: '))
print("""
PROCESSANDO...""")
sleep(1.5)

if numero == comp:
    print('você acertou! seu numero foi {} e do computador foi {}'.format(numero, comp))
else:
    print('você errou! tente novamente. seu numero foi {} e do computador foi {}'.format(numero, comp))