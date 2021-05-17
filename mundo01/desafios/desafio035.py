r1=float(input('Diga o valor da primeira reta: '))
r2=float(input('Diga o valor da segunda reta: '))
r3=float(input('Diga o valor da terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')