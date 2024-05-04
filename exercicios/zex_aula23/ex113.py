print('/--ex113--/')

def leiaInt():
    while True:
        try:
            n_int = int(input('Digite um numero intero: '))
        except ValueError:
            print('\033[31mERRO! POR FAVOR, DIGITE UM VALOR INTEIRO VALIDO\033[m')
        except KeyboardInterrupt:
            print('\033[31mO USUARIO ESCOLHEU NAO DIGITAR NEHUM VALOR\033[m')
            n_int = 0
        else:
            break
    while True:
        try:
            n_real = float(input('Digite um numero real: '))
        except ValueError:
            print('\033[31mERRO! POR FAVOR, DIGITE UM NUMERO REAL VALIDO\033[m')
        except KeyboardInterrupt:
            print('\033[31mO USUARIO ESCOLHEU NAO DIGITAR NEHUM VALOR\033[m')
            n_real = 0
        else:
            break
        finally:
            print(f'O valor inteiro digitado foi {n_int} e o real foi {n_real}')

leiaInt()