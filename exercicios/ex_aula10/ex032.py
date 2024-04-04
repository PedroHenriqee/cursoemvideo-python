print('/--ex032--/')

ano = int(input('Digite um ano, ou coloque 0 para analizar o ano atual:  '))
from datetime import date

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
        print(f'o ano de {ano} È BISEXTO!')
else:
    print(f'o ano de {ano} NÃO É UM ANO BISEXTO!')