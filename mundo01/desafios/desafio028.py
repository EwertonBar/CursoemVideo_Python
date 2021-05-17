import random
ns = random.randint(0, 5)
n = int(input('Escolha um número entre 0 e 5: '))
if ns==n:
    print('Parabéns você acertou. O número sorteado: {} é igual ao que você escolheu {}.'. format(ns, n))
else:
    print('Tente novamente. O número sorteado foi {} e o seu: {}.'.format(ns, n))