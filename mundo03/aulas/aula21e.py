def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Número: '))
print(f'Fatorial de {n} vale {fatorial(n)}')