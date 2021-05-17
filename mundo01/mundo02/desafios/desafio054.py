import datetime
atual = datetime.date.today().year
cont = 0
cont2 = 0
for c in range (1,8):
    ano=int(input('{}° Pessoa. Qual ano você nasceu? '.format(c)))
    if atual - ano >= 18:
        cont += 1
    else:
        cont2 += 1
print('Total de maiores de idade: {}. \nTotal de menores de idade: {}.'.format(cont, cont2))