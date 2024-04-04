print('/--ex025--/')

nome = input('digite seu nome completo: ')
nome = nome.strip()
nome = nome.lower()

per = input('pergunte qual nome ou sobrenome esta presente no seu nome: ')

print('seu nome tem {}?'.format(per))
print(per in nome)