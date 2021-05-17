frase = str(input("Digite sua frase: ")).strip().upper()
print('Na sua frase a letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.rfind('A')))
