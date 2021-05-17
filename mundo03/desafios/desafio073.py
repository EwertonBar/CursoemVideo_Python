brasileiro = 'Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Corinthians', 'Bragantino', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo'
print(f'Times do brasileiro {brasileiro}')
print(f'\nPrimeiros 5 colocados: {brasileiro[:5]}')
print(f'\nÚltimos 4 colocados: {brasileiro[16:]}')
print(f'\nTimes em ordem alfabética: {sorted(brasileiro)}')
print('\nO Palmeiras está na {}° Posição'.format(brasileiro.index('Palmeiras')+1))