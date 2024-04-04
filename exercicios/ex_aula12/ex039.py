print('/--ex39--/')

from datetime import date
hj = date.today().year

data = int(input('Digite seu ano de nascimento: '))
idade = hj - data

if idade < 18:
    print(f'''quem nasceu em {data}, em {hj} tem {(hj - data)} anos.
você irá se alistar em {18 - idade} ano(s)
seu alistamento sera em {18 - idade + hj}''')
elif idade > 18:
    print(f'''quem nasceu em {data}, em {hj} tem {hj - data} anos.
você deveria ou se alistou a {hj - (data + 18)} ano(s)
seu alistamentos foi em {data + 18}''')
else:
    print(f'''quem nasceu em {data} tem 18 anos
você se alistará este ano
seu alistamento sera em {hj}''')