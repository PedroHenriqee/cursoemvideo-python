print('/--ex027--/')

nome = str(input('digite seu nome inteiro: '))
tamanho = len(nome.split())

print(f'ola {nome}!')
print(f'seu primeiro nome é {nome.split()[0]}')
print(f'seu ultimo nome é {nome.split()[tamanho - 1]}')