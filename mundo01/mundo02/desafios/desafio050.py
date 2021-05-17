#ler seis números inteiros e somar apenas os pares
n=0
s=0
for p in range (0,6):
    n=int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares: {}.'.format(s))
