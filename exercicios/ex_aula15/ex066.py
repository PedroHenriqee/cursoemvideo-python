print('/--ex66--/')

cont = soma = 0
while True:
    num = int(input('digite um valor [ou 999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'a soma dos {cont} valores é {soma}')