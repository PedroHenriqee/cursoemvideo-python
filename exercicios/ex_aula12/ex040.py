print('/--ex40--/')

med1 = float(input('primeira média: '))
med2 = float(input('segunda média: '))

media = (med1 + med2) / 2
if media < 5.0:
    print(f'sua media foi {media}. \033[31mVOCÊ FOI REPROVADO!!\033[m')
elif media < 6.0:
    print('sua média foi {}. \033[33mVOCÊ ESTA DE RECUPERAÇÃO!!\033[m'.format(media))
else:
    print(f'sua médai foi {media}. \033[32mVOCÊ FOI APROVADO!!\033[m')