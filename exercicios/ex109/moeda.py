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
    return f'{val}{moeda}'.replace('.', ',')