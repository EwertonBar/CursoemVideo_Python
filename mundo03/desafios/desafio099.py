def maior(*num):
    lista = []
    print('Analisando dados passados...')
    for v in num:
        lista.append(v)
    print(f'{lista} Total de valores: {len(lista)}')
    print(f'O maior valor: {max(lista)}')


maior(3, 6, 8, 1, 10)
maior(4, 3)
maior(-1, 10, 200, -800)