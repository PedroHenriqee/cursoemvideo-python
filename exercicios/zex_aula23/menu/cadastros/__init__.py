def verificar(nome_arq):
    try:
        open(nome_arq)
        print('o arquivo "cadastro.txt" já esta criado')
    except:
        print('arquivo "cadastro.txt" criado com sucesso!')
        arquivo = open(nome_arq, 'wt+')
        return arquivo
    
def ler_arq(nome_arq):
    try:
        lendo = open(nome_arq, 'rt')
    except:
        print('Impossivel ler o arquivo!')
    else:
        ler = lendo.readlines()
        for line in ler:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', ' anos')
            print(f'{dado[0]:<20}{dado[1]}')

def escrever(nome='desconhecido', idade=0, arquivo=''):
    try:
        ape = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            ape.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados no arquivo')
        else:
            print(f'Os dados de {nome} foram registrados com sucesso!')
            ape.close()