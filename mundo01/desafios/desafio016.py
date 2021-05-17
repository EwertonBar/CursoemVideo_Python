#programa para ler um número int e mostrar sua parte inteira
from math import trunc
num = float(input("Digite um número qualquer: "))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))