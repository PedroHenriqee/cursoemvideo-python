print('/--ex104--/')

def leiaInt(num):
    nu = input(num)
    while True:
        if nu.isnumeric() == True:
            return nu
        else:
            print('\033[31mERRO! digite um número inteiro.\033[m')
            nu = input(num)

n = leiaInt('Escreva um número inteiro: ')
print(f'\033[32mVocê acabou de digitar o número {n}\033[m')
