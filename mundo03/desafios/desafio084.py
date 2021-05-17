dados = []
cadastro = []
total = 0
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    cadastro.append(dados[:])
    if total == 0:
        maior = menor = dados[1]
    if dados[1]>maior:
        maior=dados[1]
    if dados[1]<menor:
        menor=dados[1]
    dados.clear()
    total += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas cadastradas: {total}')
print(f'O maior peso: {maior}. Que foi o peso de:')
for v in cadastro:
    if v[1] == maior:
        print(v[0])
print(f'O menor peso: {menor}. Que foi o peso de:')
for v in cadastro:
    if v[1] == menor:
        print(v[0])
print('fim')
