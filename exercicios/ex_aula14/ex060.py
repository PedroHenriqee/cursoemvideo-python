print('/--ex60--/')

num = int(input('digite um numero: '))
print(f'\033[1;33mcalculando {num}!\033[m ', end='= ')

fat = 1
for c in range(1, num + 1):
    print(f'{num}', 'x' if num != 1 else '=', end=' ')
    num -= 1
    fat *= c
print(f'\033[1;32m{fat}\033[m')