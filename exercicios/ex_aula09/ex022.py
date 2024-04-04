print('/--ex022--/')

nome = input('digite seu nome inteiro: ')

print("""
analizando...""")
print(f'seu nome em letras maiuscuas: {nome.upper()}')
print(f'seu nome em letras minusculas: {nome.lower()}')
print(f'contando espaços: seu nome tem {len(nome)} letras')
print(f'sem espaços: seu nome tem {len(nome) - nome.count(' ')} letras')
print(f'seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')