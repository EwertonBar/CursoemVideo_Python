import random
ns = random.randint(0, 10)
n = int(input('Escolha um número entre 0 e 10: '))
c = 0
while ns!=n:
    n=int(input('Você errou. Tente novamente: '))
    c += 1
if ns==n:
    print('Parabéns você acertou. O número sorteado: {} é igual ao que você escolheu: {}. Após {} tentativas.'. format(ns, n, c+1))
