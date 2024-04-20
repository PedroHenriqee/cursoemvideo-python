print('/--ex85--/')

lista = [[],[]]

for lop in range(0, 7):
    valor = int(input(f'Digite o {lop}° valor: '))
    # [0] == par, [1] == ímpar
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os valores ímpares digitados foram: {lista[1]}')