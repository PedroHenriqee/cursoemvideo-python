print('/--ex56--/')

h_idade = 0
media_id = 0
cont_f = 0
for l in range(1, 5):
    print(f'----- {l}º PESSOA -----')
    nome = input('seu nome: ')
    idade = int(input('sua idade: '))
    sexo = input('[M/F]: ').lower()
    sexo = sexo[0:1]

    # media da idade do grupo
    media_id += idade

    # homem mais velho
    if h_idade == 0:
        if sexo == 'm':
            h_idade = idade
            h_nome = nome
    else:
        if sexo == 'm' and idade > h_idade:
            h_idade = idade
            h_nome = nome

    # mulheres menores de 20
    if sexo == 'f' and idade < 20:
        cont_f += 1
print(f'''
a media de idade do grupo é: {media_id / 4}
o homem mais velho tem {h_idade} anos e se chama {h_nome}
''', end='')
if cont_f >= 1:
    print(f'ao todo existe(m) {cont_f} mulher(es) menor(es) de 20 anos')
else:
    print('nao existem mulheres menores de 20 anos no programa')