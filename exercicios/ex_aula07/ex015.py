print('/--ex015--/')

dias = int(input('quantos dias voce alugou o carro?'))
km = float(input('quantos km voce rodou com o carro?'))

valor = dias * 60 + km * 0.15

print(f'o preço a se pagar pelo aluguel é de R${valor}')