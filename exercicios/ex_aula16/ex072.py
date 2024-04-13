print('/--ex72--/')

print('\033[1;33mDIGITE UM NÚMERO ENTRE [0 - 20]\033[m')
numero_digitado = int(input('digite um número: '))
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nive', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while numero_digitado < 0 or numero_digitado > 20:
    numero_digitado = int(input('digite um número entre [0 e 20]: '))

print(f'Você digitou o número: {numeros[numero_digitado]}')