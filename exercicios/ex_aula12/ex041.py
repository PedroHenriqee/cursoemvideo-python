print('/--ex41--/')
from datetime import date

nasc = int(input('ano de nascimento: '))
atual = date.today().year
print(f'o atleta tem {atual - nasc} anos')

if atual - nasc < 19:
    if atual - nasc <= 9:
        print('CLASSIFICAÇÃO [\033[1;34mMirim\033[m]')
    elif atual - nasc <= 14:
        print('CLASSIFICAÇÃO [\033[1;32mInfantil\033[m]')
    else:
        print('CLASSIFICAÇÃO [\033[1;33mJunior\033[m]')
elif atual - nasc <= 25:
    print('CLASSIFICAÇÃO [\033[1;35mSenior\033[m]')
else:
    print('CLASSIFICAÇÃO [\033[1;31mMaster\033[m]')