print('/--ex010--/')

real = float(input('quantia de dinheiro que voce possui: '))
dol = real * 0.20

from math import trunc

print('com R${} voce pode comprar U${}'.format(real, trunc(dol)))