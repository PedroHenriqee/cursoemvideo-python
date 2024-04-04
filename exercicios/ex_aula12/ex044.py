print('/--ex44--/')

preco = int(input('preço das compras: \033[32mR$\033[m'))
print('''\033[35mFORMAS DE PAGAMENTO:\033[m
\033[33m[ 1 ]\033[m à vista dinheiro/cheque
\033[33m[ 2 ]\033[m à vista cartão
\033[33m[ 3 ]\033[m 2x no cartão
\033[33m[ 4 ]\033[m 3x ou mais no cartão''')

opcao = int(input('qual a opção? '))

if opcao < 5 and opcao > 0:
    if opcao == 1:
        desc = preco * .90
        print(f'você pagou a vista e recebeu \033[31m10%\033[m de desconto, passando de \033[31mR${preco}\033[m para \033[31nR${desc}\033[m.')
    elif opcao == 2:
        desc = preco * .95
        print(f'você pagou a vista no cartao e recebeu \033[31m5%\033[m de desconto, passando de \033[31mR${preco}\033[m para \033[31mR${desc}\033[m.')
    elif opcao == 3:
        vx = int(input('em quantas vezes deseja pagar? \033[33m(1x) - (2x)\033[m '))
        if vx > 2 or vx < 1:
            print('\033[31mESCOLHA PAGAR EM (1X) OU EM (2X) PARA REALIZAR O PAGAMENTO!!\033[m')
        else:
            print(f'você passou no cartão em \033[32m{vx}\033[m vez(es). você pagará \033[32mR${preco}\033[m.')
    else:
        vx = int(input('em quantas vezes deseja pagar? \033[33m(3x) a (12x)\033[m '))
        if vx < 3 or vx > 12:
            print('\033[31mESCOLHA PAGAR DE (3X) A (12X) PARA REALIZAR O PAGAMENTO!!\033[m')
        else:
            print(f'''você passou no cartão em \033[32m{vx}\033[m vezes.pela forma de pagamento
você pagará mais 20% de JUROS!, então de \033[32mR${preco}\033[m para \033[32mR${preco * 1.20}\033[m''')
else:
    print('escolha uma opção existente')