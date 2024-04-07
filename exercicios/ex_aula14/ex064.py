print('/--ex64--/')

cont = soma = numero = 0

while numero != 999:
    numero = int(input('digite um número \033[33m[999 para terminar]\033[m: '))
    if numero != 999:
        cont += 1
        soma += numero
print(f'você digitou {cont} números e a soma entre eles foi {soma}')