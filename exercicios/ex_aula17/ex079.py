print('/--ex79--/')

lista = [int(input('Digite um valor: '))]
print('Valor adicionado com sucesso..')
play = input('Quer continuar? [S/N]: ').upper().strip()
if 'S' in play:
    while play == 'S':
        lista.append(int(input('Digite um valor: ')))
        if lista.count(lista[-1]) > 1:
            print('Valor duplicado! Não vou adicionar...')
            lista.pop()
            play = input('Quer continuar? [S/N]: ').upper().strip()
        else:
            print('Adicionado com sucesso..')
            play = input('Quer continuar? [S/N]: ').upper().strip()
print('-=' * 25)
lista.sort()
print(f'Você digitou os valores {lista}')