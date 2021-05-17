cabeçalho = 'Calculando seu financiamento'
print('\033[40m{:^50}\033[m'.format(cabeçalho))
casa = float(input('Qual o valor da casa? '))
sal=float(input('Qual seu salário? '))
tempo=int(input('Quantos anos vai durar o financiamento? '))
prest = casa/(tempo*12)
cond = sal*0.3
if prest <= cond:
    print('Parabéns seu financiamento foi aprovado! \nO valor da sua prestação será: {:2f}.'.format(prest))
else:
    print('Infelizmente não podemos atender seu pedido. A prestação está muito alta para seu rendimento.')
rodapé = ' '
print('\033[40m{:^50}\033[m'.format(rodapé))