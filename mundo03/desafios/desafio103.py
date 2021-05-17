def ficha(nome='<desconhecido>', gols=0):
    print(f'{nome} fez {gols} gols.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)