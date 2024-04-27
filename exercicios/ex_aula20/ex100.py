print('/--ex100--/')
from random import randint
from time import sleep

def sorteio():
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    for lop in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[lop], end=' ', flush=True)
        sleep(.5)
    print('PRONTO!')

def soma(list):
    soma = 0
    for lop in list:
        if lop % 2 == 0:
            soma += lop
    print(f'Somando os valores pares de {list}, temos {soma}')

lista = list()
sorteio()
soma(lista)