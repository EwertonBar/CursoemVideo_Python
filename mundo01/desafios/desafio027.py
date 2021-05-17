nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()

#print(len(lista))
#print(lista)

print('Seu primeiro nome: {}. \nSeu sobrenome: {}.'.format(lista[0],lista[len(lista)-1]))
