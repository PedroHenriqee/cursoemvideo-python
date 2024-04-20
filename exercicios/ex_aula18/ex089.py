print('/--ex89--/')

pessoas = []
while True:
    nome = str(input('Nome: '))
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))
    pessoas.append([nome, not1, not2])
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 25)

print(f'{"No.":<4}{"NOME":>5}{"MÉDIA":>10}')
print('-' * 25)
for ind, lista in enumerate(pessoas):
    print(f'{ind:<4}{lista[0]:<10}{(lista[1] + lista[2]) / 2:<8.1f}')
print('-' * 25)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'Notas de {pessoas[aluno][0]} são {pessoas[aluno][1:]}')
    print('-' * 25)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')