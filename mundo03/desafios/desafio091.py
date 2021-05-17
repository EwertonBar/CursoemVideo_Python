import random, time
from operator import itemgetter
rank = dict()
jogadas = {'jogador1': random.randint(1, 6),
           'jogador2': random.randint(1, 6),
           'jogador3': random.randint(1, 6),
           'jogador4': random.randint(1, 6),}

for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(rank):
    print(f'{k+1}º {v[0]} tirou {v[1]} no dado')
