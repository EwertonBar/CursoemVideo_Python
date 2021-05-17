def aumentar(v, format=False):
    v *= 1.1
    return (f'Aumentando 10%, temos R${v:2f}')


def dobro(v, format=False):
    d = v*2
    return (f'O dobro de R${v} é R${d}')


def metade(v, format=False):
    m = v / 2
    return (f'A metade de R${v} é R${m}')


