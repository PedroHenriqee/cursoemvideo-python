print('/--ex112--/')

import moeda
from dado import leiaDinheiro

p = leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
