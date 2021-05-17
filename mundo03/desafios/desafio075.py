lista = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))
print(lista)
print(f'\nQuantos 9 foram digitados: {lista.count(9)}')
if 3 in lista:
    print(f'Em que posição foi digitado o primeiro valor 3: {lista.index(3)+1}°. ')
else:
    print('Não foi digitado nenhum número 3.')
print('Os valores pares digitados foram: ', end='')
for a in lista:
    if a % 2 == 0:
        print(a, end=' ')