lista = list()
men = mai = 0
for v in range (0,5):
    lista.append(int(input('Digite um valor: ')))
    if v == 0:
        men = mai = lista[0]
    if lista[v] > mai:
        mai = lista[v]
    if lista[v] < men:
        men = lista[v]
print(f'Você digitou a lista {lista}.')
print(f'O maior valor digitado foi {mai}. Posição: ',end='')
for i, v in enumerate(lista):
    if v == mai:
        print(i+1, end='...')
print('')
print(f'O menor valor digitado foi {men}. Posição: ',end='')
for i, v in enumerate(lista):
    if v == men:
        print(i+1, end='...')