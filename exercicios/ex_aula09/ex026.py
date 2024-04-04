print('/--ex026--/')

frase = str(input('Digite uma frase:')).strip()
frase = frase.lower()

print(f'a letra A aparece {frase.count('a')} vezes na frase')
print(f'a primeira letra apareceu na posição {frase.find('a') + 1}')
print(f'a ultima letra apareceu na posição {frase.rfind('a') + 1}')