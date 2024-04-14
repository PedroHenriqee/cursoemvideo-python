print('/--ex83--/')

texto = str(input('Digite uma expressão: '))

numero_p = ordem_p = 0
lib = ''
for letra in texto:
    if texto.count('(') == texto.count(')'):
        numero_p = 1

    if letra == '(':
        key_abre = texto.index(letra)
        lib = 'o'
    if letra == ')':
        key_fecha = texto.index(letra)
        lib += 'pen'
    if lib == 'open':
        if key_abre < key_fecha:
            ordem_p = 1
        else:
            ordem_p = 0
            break
        
if numero_p == 1 and ordem_p == 1:
    print('Expressão válida!')
else:
    print('Expressão inválida!')