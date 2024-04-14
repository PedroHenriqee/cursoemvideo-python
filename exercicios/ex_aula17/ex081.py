print('/--ex81--/')

lista = list()
play = 'S'
while play == 'S':
    lista.append(int(input('Digite um valor: ')))
    play = input('Quer continuar? [S/N]: ').upper().strip()

print('-=' * 25)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) >= 1:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')