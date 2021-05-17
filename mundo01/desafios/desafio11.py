#peguntar altura e largura. calcular área. informar quantidade de tinta necessária. cada 1l de tinta pinta 2m²
altura = float(input('Qual é a altura da sua parede? '))
largura = float(input('Qual é a largura da sua parede? '))
a = altura*largura
t=a/2
print('A área da sua parede: {}m². Será necessário: {}L de tinta.'.format(a, t))
