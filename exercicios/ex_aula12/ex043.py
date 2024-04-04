print('/--ex43--/')

peso = float(input('seu peso (em kg): '))
altura = float(input('sua altura em (m ): '))

imc = peso / altura ** 2
print('seu imc é: {:.1f} '.format(imc))

if imc < 40:
    if imc <= 18.5:
        print('abaixo do peso')
    elif imc <= 25:
        print('peso ideal')
    elif imc <= 30:
        print('sobrepeso')
    elif imc <= 40:
        print('obesidade')
else:
    print('obesidade mórbida')