import random
import time
v=1
jogo = []
lista = []
a = int(input('Quantidade de palpites: '))
while v <= a:
    c = 0
    while True:
        p = random.randint(1, 60)
        if p not in jogo:
            jogo.append(p)
            c += 1
        if c == 6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    v+=1
for i, q in enumerate(lista):
    print(f'Jogo {i+1}: {q}')