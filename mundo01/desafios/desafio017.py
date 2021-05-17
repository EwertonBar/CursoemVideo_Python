#programa para ler cateto adjacente e cateto oposto e calcula o valor da hipotenusa
import math
cato = float(input('Qual o valor do cateto oposto? '))
cata = float(input('Qual o valor do cateto adjacente? '))
h = math.hypot(cato, cata)
print('O valor da hipotenusa é {:.2f}'.format(h))