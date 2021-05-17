sal=float(input('Qual seu salário? '))
if sal>1250.00:
    print('Com um aumento de 10% o salário passa para: {}.'.format(sal*1.1))
if sal<=1250.00:
    print('Com um aumento de 15% o salário passa para: {}.'.format(sal*1.15))