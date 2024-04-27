print('/--ex98--/')
from time import sleep

def contador(i, f, p):
    print('=-' * 30)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    contI = i
    contF = f
    if contI < contF:
        while contI <= f:
            print(contI, end=' ', flush=True)
            sleep(.5)
            contI += p
    else:
        while contI >= contF:
            print(contI, end=' ', flush=True)
            sleep(.5)
            contI -= p
        
    print('FIM!')
        
contador(0, 10, 1)
contador(10, 1, 1)
print('=-' * 30)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
contador(inicio, fim, passo)