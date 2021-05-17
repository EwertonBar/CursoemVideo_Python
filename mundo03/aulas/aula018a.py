pessoas = []
dados = []
for c in range (0,3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    pessoas.append(dados[:])
    dados.clear()

for p in pessoas:
    if p[1] >= 18:
        print(f'Maiores de  idade: \nPessoa : {p[0]}. Idade: {p[1]}.')