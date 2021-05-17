def voto(ano):
    import datetime
    atual = datetime.date.today().year
    idade = atual - ano
    if 18 <= idade < 70:
        print(f'Com {idade} anos é obrigatório votar.')
    elif 16 <= idade < 18 or idade >= 70:
        print(f'Com {idade} anos é facultativo a votação.')
    else:
        print(f'Com {idade} anos é proibido votar.')


a = int(input('Ano de nascimento: '))
voto(a)
