print('/--ex101--/')

def voto(vt):
    from datetime import date
    ano = date.today().year
    idade = ano - vt
    return idade

print('-' * 25)
dado = voto(int(input('Em que ano você nasceu?: ')))
print(f'Com {dado} anos: ', end='')
if dado < 16 or dado > 70:
    print('NÃO VOTA.')
elif dado <= 18 or dado > 65:
    print('VOTO OPCIONAL.')
else:
    print('VOTO OBRIGATÓRIO.')
