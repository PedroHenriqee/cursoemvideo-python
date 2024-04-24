print('/--ex90--/')

nome = str(input('Nome: ')).capitalize()
media = float(input(f'Média de {nome}: '))
if media <= 3:
    situacao = 'Reprovado'
elif media <= 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'
dic = {'nome': nome, 'média': media, 'situação': situacao}

print('-=' * 30)

for key, it in dic.items():
    print(f'-- {key} é igual a {it}')