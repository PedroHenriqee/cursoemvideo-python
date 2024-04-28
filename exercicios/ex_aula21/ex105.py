print('/--ex105--/')

def notas(*num, sit=False):
    """
    função que realiza uma analize das notas passadas por argumentos. retorna a analize feita na função, em um dicionario.
    argumentos:
    números: números int ou float, quantos quiser.
    sit: parametro opcional mostra a situação dos alunos baseado na media. por padrao sit=False. para ativar essa função digite sit=True.
    """
    soma = 0
    dic = dict()
    for key, lop in enumerate(num):
        soma += lop
        if key == 0:
            maior = lop
            menor = lop
        else:
            if lop > maior:
                maior = lop
            if lop < menor:
                menor = lop
    media = soma / len(num)
    if media <= 4:
        situ = 'RUIM'
    elif media <= 6:
        situ = 'BOA'
    elif media <= 8:
        situ = 'RAZOAVEL'
    else:
        situ = 'MUITO BOA'
    dic['total'] = len(num)
    dic['maior'] = maior
    dic['menor'] = menor
    dic['média'] = media
    if sit == True:
        dic['situação'] = situ
    return dic
    


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
