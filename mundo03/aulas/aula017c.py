valores = list()

for v in range (0,5):
    valores.append(int(input('Digite um valore: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei no final da lista.')
print(valores)