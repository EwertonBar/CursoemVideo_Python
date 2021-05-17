acum = 0
acumf = 0
velho = 0
nomevelho = ''
for e in range (1,5):
    nome=str(input('{}. Qual seu nome? '.format(e)))
    idade=int(input('{}. Qual sua idade? '.format(e)))
    sexo=int(input('{}. Qual seu sexo. [1] Masculino   [2] Feminino? '.format(e)))
    acum += idade
    if sexo == 2 and idade<20:
        acumf += 1
    if e == 1 and sexo == 1:
        velho = idade
        nomevelho = nome
    if sexo == 1 and idade > velho:
        velho = idade
        nomevelho = nome

print('A média de idade do grupo: {} anos.'.format(acum/4))
print('{} mulheres têm menos de 20 anos.'.format(acumf))
print('Nome do homem mais velho: {}. Idade do homem mais velho: {}'.format(nomevelho,velho))
