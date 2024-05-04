print('/--ex114--/')

import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não esta acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')