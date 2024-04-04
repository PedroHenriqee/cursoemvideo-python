print('/--ex035--/')

seg1 = float(input('primero segmento: '))
seg2 = float(input('segundo segmento: '))
seg3 = float(input('segundo segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('os segmentos acima formam um triangulo')
else:
    print('os segmentos acima nao formam um triangulo')