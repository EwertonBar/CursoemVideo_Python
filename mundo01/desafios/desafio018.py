#programa para ler um ângulo e calcular seu sen, cos e tangente
import math
an = float (input('Digite um ângulo qualquer: '))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('Se o ângulo for {} \nseu sen vale {:2f} \nseu cos vale {} \n sua tang vale {}'.format(an, s, c, t))
