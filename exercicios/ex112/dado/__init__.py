def leiaDinheiro(val=''):
    valor = str(input(val)).strip()
    if valor.isalpha() == True:
        while True:
            print(f'ERRO: "{valor}" É UM PREÇO INVÁLIDO')
            valor = str(input(val)).strip()
            if valor.isalpha() == False:
                break
    if valor.count(',') >= 1:
        valor = valor.replace(',', '.')
    valor = float(valor)
    return valor

