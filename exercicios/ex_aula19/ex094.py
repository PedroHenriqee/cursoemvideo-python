print('/--ex94--/')

pessoas = {}
cadastros = []
idade = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('sexo: ')).upper().strip()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    idade += pessoas['idade']
    cadastros.append(pessoas.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('=-' * 30)

media = idade / len(cadastros)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B) A médiade idade é de {media} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for lop in range(0, len(cadastros)):
    if cadastros[lop]['sexo'] == 'F':
        print(f'{cadastros[lop]['nome']},', end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for lop in range(0, 4):
    if cadastros[lop]['idade'] > media:
        print(f'  Nome = {cadastros[lop]['nome']}; sexo = {cadastros[lop]['sexo']}; idade = {cadastros[lop]['idade']};')