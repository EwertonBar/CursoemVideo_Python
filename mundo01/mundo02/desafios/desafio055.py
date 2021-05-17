maior = 0
menor = 0
for c in range (1,6):
    peso=float(input('{}° Pessoa. Qual seu peso? '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior foi {} e o menor foi {}.'.format(maior, menor))
