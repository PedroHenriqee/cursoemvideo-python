print('/--ex48--/')

ac = 0
cont = 0
for l in range(1, 501, 2):
    if l % 3 == 0:
        cont += 1
        ac += l
print('a soma de todos os {} numeros solicitados é {}'.format(cont, ac))