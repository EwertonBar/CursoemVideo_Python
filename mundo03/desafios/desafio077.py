lista = ('python', 'aprender', 'trabalho', 'curso', 'programar', 'linguagem', 'programador', 'futuro', 'mercado', 'estudar', 'grátis', 'praticar')
for p in lista:
    print(f'\nA palavra {p} apresenta as seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')