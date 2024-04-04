print('/--ex54--/')
from datetime import date

atual = date.today().year
contma = 0
contme = 0

for l in range(1, 8):
    idade = int(input(f'em que ano a {l}º pessoa nasceu?: '))
    if atual - idade < 18:
        contme += 1
    else:
        contma += 1
print(f'''ao todo tivemos {contma} pessoas maiores de idade
e tambem tivemos {contme} pessoas menores de idade''')