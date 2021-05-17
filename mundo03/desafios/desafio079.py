lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Tente outro!')
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print('Lista finalizada!')
print(f'{lista}')