def aumentar(val=0, tax=0):
    res = val + (val * tax/100)
    return res

def diminuir(val=0, tax=0):
    res = val - (val * tax/100)
    return res

def dobro(val=0):
    res = val * 2
    return res

def metade(val=0):
    res = val / 2
    return res

def moeda(val=0, moeda='R$'):
    return f'{moeda}{val}'.replace('.', ',')

def resumo(val=0, porcem1=0, porcem2=0):
    print('-' * 25)
    print(f'     {"RESUMO DO VALOR"}')
    print('-' * 25)
    print(f'Preço analizado: {moeda(val):>8}')
    print(f'Dobro do preço: {moeda(dobro(val)):>8}')
    print(f'Metade do preço: {moeda(metade(val)):>8}')
    print(f'{porcem1}% de aumento: {moeda(aumentar(val, porcem1)):>8}')
    print(f'{porcem2}% de redução: {moeda(diminuir(val, porcem2)):>8}')
    print('-' * 25)