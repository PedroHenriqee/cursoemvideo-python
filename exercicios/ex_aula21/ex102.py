print('/--ex102--/')

def fatorial(val, show=False):
    """
    -> Calcula o fatorial de um número.
    :param val: O número a ser calculado
    :param show: (opicional) mostrar ou não a conta.
    :return: o valor do fatorial de um número val
    """
    print('-' * 30)
    fat = val
    
    for lop in range(val, 1, -1):
            fat *= lop - 1
    if show == False:
        print(fat)
    else:
        for lop in range(val, 0, -1):
              print(f'{lop}', '=' if lop == 1 else 'x ', end='')
        print(f' {fat}')
    return fat
    
resultado = fatorial(5, True)