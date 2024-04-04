print('/--ex42--/')

first = int(input('primeiro segmento: '))
second = int(input('segundo segmento: '))
third = int(input('terceiro segmento: '))

if first + second > third and third + first > second and second + third > first:
    if first == second == third:
        print('de acordo com os segmentos, você tem um triângulo \033[1;35mEQUILATERO\033[m')
    elif first != second != third != first:
        print('de acordo com os segmentos, você tem um triângulo \033[31;35mESCALENO\033[m')
    else:
        print('de acordo com os segmentos, você tem um triângulo \033[1;35mESÓSCELES\033[m')
else:
    print('isso não forma um triângulo!')