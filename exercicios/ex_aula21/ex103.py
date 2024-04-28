print('/--ex103--/')

def jogador(nome=False, gol=0):
    if gol.isnumeric() == False:
        gol = 0
    if nome == '':
        nome = '<desconhecido>'
    print(f'o jogador {nome} fez {gol} gol(s) no campeonato.')

nome = str(input('Nome do jogador: ')).strip()
gols = input('Número de gols: ')
jogador(nome, gols)