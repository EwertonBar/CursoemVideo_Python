#algoritmo para calcular a tabuada de um número
n1 = int(input('Digite um número qualquer: '))
for c in range (0,10):
    print('{}x{}={}'.format(n1,c,n1*c))