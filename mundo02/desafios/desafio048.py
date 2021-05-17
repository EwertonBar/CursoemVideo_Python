print('Soma de números ímpares múltiplos de 3 entre 1 e 500:')
soma = 0
cont = 0
for c in range (1,501):
    if c % 2 == 1 and c % 3 == 0:
       cont += 1
       soma += c
print('Soma: {}. Quantidade de números divisíveis por 3: {}.'.format(soma, cont))


