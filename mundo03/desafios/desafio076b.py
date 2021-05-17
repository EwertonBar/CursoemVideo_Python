compras = ('Caneta', 1.50, 'Borracha', 2, 'Caderno', 8.5, 'Mochila', 88, 'Notebook', 1520)

print('-'*37)
print('{:^37}'.format('LISTA DE PREÇOS'))
print('-'*37)
for pos in range(0,len(compras)):
    if pos % 2 ==0:
        print(f'{compras[pos]:.<28}R$', end='')
    if pos % 2 == 1:
        print(f'{compras[pos]:>7.2f}')
print('-'*37)