print('/--ex93--/')

cadastros = dict()
lista_cadastro = list()
idade = 0
while True:
    cadastros['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    cadastros['sexo'] = sexo
    cadastros['idade'] = int(input('Idade: '))
    idade += cadastros['idade']
    lista_cadastro.append([cadastros.copy()])
    terminar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while terminar != 'N' and terminar != 'S':
        print('ERRO! Responda apenas S ou N.')
        terminar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if terminar == 'N':
        break
media = idade / len(lista_cadastro)
print('=-' * 30)

print(f'A) Ao todo temos {len(lista_cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for lop in lista_cadastro:
    if lop[0]['sexo'] == 'F':
        print(f'{lop[0]['nome']},', end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for lop in lista_cadastro:
    if lop[0]['idade'] >= media:
        print(f'''   Nome = {lop[0]['nome']}; sexo = {lop[0]['sexo']}; idade = {lop[0] ['idade']};''')
print('<< ENCERRADO >>')
