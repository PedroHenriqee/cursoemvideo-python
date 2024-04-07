print('/--ex67--/')
from time import sleep

cont = 0

while True:
    num = int(input('\033[32mquer mostar a tabuada de qual número?:\033[m '))
    sleep(.5)
    print('\033[1;36m-\033[m' * 50)
    if num < 0:
        break
    else:
        while cont <= 10:
            print(f'{num} X {cont:2} = {num * cont}')
            cont += 1
    print('\033[1;36m-\033[m' * 50)
    cont = 0
print('FIM DO PROGRAMA')