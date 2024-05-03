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
    print(f'RESUMO DO VALOR'.center(20))
    print('-' * 25)
    print(f'Preço analizado: \t{moeda(val)}')
    print(f'Dobro do preço: \t{moeda(dobro(val))}')
    print(f'Metade do preço: \t{moeda(metade(val))}')
    print(f'{porcem1}% de aumento: \t{moeda(aumentar(val, porcem1))}')
    print(f'{porcem2}% de redução: \t{moeda(diminuir(val, porcem2))}')
    print('-' * 25)