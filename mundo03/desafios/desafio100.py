def sorteia(lista):
    import random
    for v in range(0, 5):
        a = random.randint(1, 10)
        if v == 0:
            lista.append(a)
        else:
            while a in lista:
                a = random.randint(1, 10)
            lista.append(a)
    print(f'Sorteando 5 valores: {lista}.')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Lista: {lista}. A soma dos valores pares {soma}.')


lista = []
sorteia(lista)
somapar(lista)
