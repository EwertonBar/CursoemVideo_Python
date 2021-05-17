cadastro = {}
qtd = []
tot = 0
cadastro["nome"] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for c in range(1, partidas+1):
    qtd.append(int(input(f'Quantos gol na partida {c}: ')))
cadastro['gols'] = qtd[:] # recebe uma cópia.
cadastro['total'] = sum(qtd)
print('='*30)
print(cadastro)
print('='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem valor {v}')
print('='*30)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas')
for i, v in enumerate(qtd):
    print(f'Na partida {i+1}, fez {v} gols.')
print('=' * 30)