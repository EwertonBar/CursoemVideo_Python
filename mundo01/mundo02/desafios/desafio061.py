n=int(input('Digite um número: '))
r=int(input('Digite a razão da PA: '))
pa = n
c = 10
print('A PA é: ', end='')
while c>0:
    print('{}'.format(pa),end=' ')
    pa += r
    c -= 1
print('\nFim.')
