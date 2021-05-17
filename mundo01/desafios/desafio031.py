dist=float(input('Qual a distância da sua viagem? '))

if dist <= 200:
    print('O preço da sua passagem será {} reais. Tarifa: R$0.50.'.format(dist*0.5))
else:
    print('O preço da sua passagem será {} reais. Tarifa: R$ 0.45.'.format(dist*0.45))