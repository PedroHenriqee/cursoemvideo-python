print('/--ex017--/')

from math import hypot

a = float(input('digite em cm o valor de um dos cateto (hipotenusa, teorema de pitagoras.)'))
b = float(input('digite em cm o valor do segundo cateto (hipotenusa, teorema de)'))

hipo = hypot(a, b)

print('o valor da hipotenusa é igual a {}cm'.format(hipo))