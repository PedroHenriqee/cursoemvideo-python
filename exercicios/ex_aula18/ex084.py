print('/--ex84--/')

lista = list()
pessoas = list()
maior = menor = 0

while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    play_again = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if play_again == 'N':
        break
print('-=' * 20)

print(f'{len(lista)} pessoas foram cadastradas.')
print(f'a pessoa mais pessada cadastrada tem {maior}Kg.', end=' ')
for lop in lista:
    if lop[1] == maior:
        print(f'[{lop[0]}]', end=' ')
print(f'\na pessoas mais leve cadastrada tem {menor}Kg.', end=' ')
for lop in lista:
    if lop[1] == menor:
        print(f'[{lop[0]}]', end=' ')