print('/--ex93--/')

jogo = dict()
jogo['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogo['nome']} jogou?: '))

jogo['gols'] = []
tot = 0
for lop in range(0, quant):
    gol = int(input(f'Quantos gols na partida {lop}?: '))
    jogo['gols'] += [gol]
    tot += gol
jogo['total'] = tot

print('=-' * 30)
print(jogo)
print('=-' * 30)

for key, valor in jogo.items():
    print(f'O campo {key} tem o valor {valor}')
print('=-' * 30)

print(f'O jogador {jogo['nome']} jogou {quant} partidas.')
for lop in range(0, quant):
    print(f'''      {f"=> Na partida {lop}, fez {jogo['gols'][lop]} gols"}''')
print(f'Foi um total de {tot} gols')