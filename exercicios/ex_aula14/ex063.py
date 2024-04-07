print('/--ex63--/')

print('-' * 50)
print('\033[35mSEQUENCIA\033[m DE \033[36mFIBONACCI\033[m')
print('-' * 50)

termo = int(input('digite a quantidade de termos: '))
num1 = 1
num2 = 1
num3 = num1 + num2
co = 4

print('\033[1;36m~\033[m' * 50)

print(f'0 -> {num1} -> {num2} -> ', end='')

if termo > 3:
    while co <= termo:
        co += 1
        print(num3, '-> ' if co <= termo else '-> \033[32mFIM\033[m', end='')
        num1 = num2
        num2 = num3
        num3 = num1 + num2
else:
    print('\033[32mFIM\033[m')
print('')
print('\033[1;31m~\033[m' * 50)