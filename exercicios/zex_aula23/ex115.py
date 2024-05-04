print('/--ex115--/')

from menu import pacote
from menu import cadastros

arq = 'cadastro.txt'
arquivo = cadastros.verificar(arq)

while True:
    itens = pacote.menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Programa')
    for lop in range(0, 3):
        opc = pacote.opcao()
        if opc:
            break
    if opc:
        if opc == 1:
            pacote.escolha(itens, opc-1)
            cadastros.ler_arq(arq)
        elif opc == 2:
            pacote.escolha(itens, opc-1)
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            cadastros.escrever(nome, idade, arq)
        else:
            pacote.formatado('Saindo do Programa... até logo!')
            break