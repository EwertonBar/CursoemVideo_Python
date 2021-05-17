#desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma {valores} vale {s}')


soma(4, 5)
soma(3, 23, 7)
