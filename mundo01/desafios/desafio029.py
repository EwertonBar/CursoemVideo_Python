vel=int(input('Velocidade lida em km/h: '))
if vel > 80:
    print('Você está acima da velocidade permitida, a cada km a mais a multa custa 7 reais. Você está a {}, o que vai '
          'custar {} reais.'.format(vel, (vel-80)*7))
else:
    print('Parabéns você está andando na velocidade permitida!')