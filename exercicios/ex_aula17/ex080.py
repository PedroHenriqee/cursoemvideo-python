print('/--ex80--/')

lista = list()
for loop in range(0, 5):
    valor = int(input('Digite um valor: '))
    if loop == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Item adicinado no final da lista..')
    else:
        index = 0
        while index < len(lista):
            if valor <= lista[index]:
                lista.insert(index, valor)
                break
            index += 1
        print(f'Item adicionado na posição {index} da lista..')

print('-=' * 25)
print(f'valores da lista em posição ordenada: {lista}')