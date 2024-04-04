print('/--ex034--/')

sal = float(input('qual o seu salario?: R$'))

if sal < 1250.00: # 15%
    aumento = sal * 15/100 + sal
else: # 10%
    aumento = sal * 10/100 + sal

print(f'seu salario passou de {sal} para {aumento}')