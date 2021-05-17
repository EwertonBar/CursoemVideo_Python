from operator import itemgetter
dados = list()
cadastro = dict()
while True:
    cadastro['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('ERRO! Por favor digite apenas M ou F. \nSexo: [M/F] ')).upper().strip()[0]
    cadastro['sexo'] = sexo
    cadastro['idade'] = int(input('Idade: '))
    dados.append(cadastro.copy())
    cadastro.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('ERRO! Por favor digite apenas S ou N. \nDeseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
tot = 0
for i, v in enumerate(dados):
    tot += dados[i]['idade']
print(f'A) Total de pessoas cadastradas: {len(dados)}.')
print(f'B) A média de idade: {tot/len(dados)}.')
print(f'C) Pessoas do sexo F: ', end='')
for i, v in enumerate(dados):
    if dados[i]['sexo'] == 'F':
        print(dados[i]['nome'], end='... ')
print()
print(f'D) Pessoas com idade acima da média: ')
for i, v in enumerate(dados):
    if dados[i]['idade'] > tot/len(dados):
        for k, d in v.items():
            print(f'{k}={d}', end=' / ')
        print()
