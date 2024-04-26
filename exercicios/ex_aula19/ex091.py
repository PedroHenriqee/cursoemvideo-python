print('/--ex91--/')

from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados:')

pontos = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)}
for key, val in pontos.items():
    print(f'o {key} tirou {val} no dado.')
    sleep(1)
print('=-' * 30)

ranking = list()
ranking = sorted(pontos.items(), key=itemgetter(1), reverse=True)

print('== RANKING DOS JOGADORES ==')
for ind, val in enumerate(ranking):
    print(f'{ind+1}º lugar: {val[0]} com {val[1]}.')