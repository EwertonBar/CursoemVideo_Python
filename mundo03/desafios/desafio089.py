lista = []
cadastro = []
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Nota 1: ')))
    cadastro.append(float(input('Nota 2: ')))
    lista.append(cadastro[:])
    cadastro.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-'*21)
print('N°  Nome        Média')
print('-'*21)
for i, v in enumerate(lista):
    print(f'{i:<4}{lista[i][0]:<12}{(lista[i][1]+lista[i][2])/2:>5}')
n=0
while n >= 0:
    n=int(input('Mostrar nota de qual aluno? [-1 finaliza]: '))
    while n > len(lista)-1:
        print('N° de aluno inválido. Tente novamente')
        n = int(input('Mostrar nota de qual aluno? [-1 finaliza]: '))
    if n < 0:
        break
    print(f'Notas de {lista[n][0]}: {lista[n][1:]}')

print('\nPrograma finalizado. Volte sempre!')