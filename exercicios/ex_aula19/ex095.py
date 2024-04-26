print('/--ex95--/')

jogadores = dict()
lista_jogadores = list()
tot_lst = list()
tot = 0
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    jogadores['gols'] = []
    for lop in range(0, quant):
        tot_lst.append(int(input(f'Quantos gols na partida {lop + 1}? ')))
        tot += tot_lst[lop]
    jogadores['gols'] = tot_lst[:]
    jogadores['tot'] = tot
    tot = 0
    tot_lst.clear()
    lista_jogadores.append(jogadores.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            print('Digite entre S e N para prosseguir: ')
    if continuar == 'N':
        break
print('=-' * 30)

print(f'{"COD"} {"NOME"} {"GOLS":>8} {"TOTAL":>8}')
print('-' * 30)
for enu, lop in enumerate(lista_jogadores):
    print(f'{enu} {lop['nome']} {lop['gols']} {lop['tot']}')

while True:
    print('-' * 30)
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    if dados < len(lista_jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {lista_jogadores[dados]['nome']}')
        for enu, lop in enumerate(lista_jogadores):
            if enu == dados:
                for key, gol in enumerate(lop['gols']):
                    print(f'''    No jogo {key + 1} fez {gol} gols''')
                break
    else:
        print('ESCOLHA UM JOGADOR EXISTENTE OU SAIA DO PROGRAMA!!')
print('FIM DO PROGRAMA!!')