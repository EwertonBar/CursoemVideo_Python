lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('Fim')
print(f'Quantidade de números digitados: {len(lista)}.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')