print('/--ex004--/')

txt = input('digite algo:')
print('o texto escrito foi {}'.format(txt))

if txt.isalpha():
    print('seu texto é composto somente por letras!')
else:
    print('seu texto nao é composto somente por letras!')

if txt.islower():
    print('seu texto é composto somente por letars maiusculas!')
else:
    print('seu texto nao é composto somente por letras maiusculas!')

if txt.isupper():
    print('seu texto é composto somente por letras minusculas!')
else:
    print('seu texto nao é composto somente por letras minusculas!')

if txt.isnumeric():
    print('seu texto é composto por numeros!')
else:
    print('seu texto nao é composto por numeros!')

if txt.isalnum():
    print('seu texto é composto por letras ou numeros!')
else:
    print('seu texto nao é composto por letras ou numeros!')

if txt.isspace():
    print('seu texto é composto somente por espaços!')
else:
    print('seu texto nao é composto somente por espaços!')
