def leiaint(n):
    while True:
        if n.isnumeric():
            break
        else:
            print('ERRO. digite um número inteiro!')
        n = leiaint(input('Digite um número: '))
    return n

n = leiaint(input('Digite um número: '))
print(f'Você digitou um número inteiro: {n}.')