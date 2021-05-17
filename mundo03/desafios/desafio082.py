lista=[]
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um  valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('FIM...')
print(f'Lista: {lista}')
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'Lista par: {listapar}')
print(f'Lista ímpar: {listaimpar}')