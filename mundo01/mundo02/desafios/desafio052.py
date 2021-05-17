n=int(input('Digite um número para saber se é primo: '))
tot=0
for d in range(1,n+1):
    if n % d == 0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(d), end=" ")
print('\n\033[mSeu número {} foi divisível {} vezes.'.format(n,tot))
if tot == 2:
    print('Seu número é primo!')
else:
    print('Seu número não é primo!')