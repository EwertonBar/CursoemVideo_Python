matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somat = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l} {c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            somat += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
print(f'A soma dos itens pares: {somap}')
print(f'Soma dos itens da terceira coluna: {somat}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')