print('/--ex73--/')

lista = ('corinthians', 'palmeiras', 'santos', 'gremio', 'fluminense', 'flamengo', 'internacional', 'botafogo', 'vasco', 'bahia')

print('-=' * 20)
print(f'Lista de times do brasieirão: \033[1;33m{lista}\033[m')
print('=-' * 20)
print(f'Os cinco primeiros: \033[1;33m{lista[0:6]}\033[m')
print('-=' * 20)
print(f'Os quatro ultimos: \033[1;33m{lista[-4:]}\033[m')
print('=-' * 20)
print(f'Times em ordem alfabetica: \033[1;33m{sorted(lista)}\033[m')

print(f'\033[32mo {lista[2]} esta na 3º posição.\033[m')