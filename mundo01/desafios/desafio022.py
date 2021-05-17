#leia o nome completo de uma pessoa, Mostre todo em letras maiúsculas. Quantas letras ao todos sem os espaços. Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
qtdletras = nome.split()


print('Nome com letras maiúsculas: {}. '
      '\nQuantidade de letras: {}. '
      '\nQuantidade de letras do primeiro nome: {}'.format(nome.upper(), len(nome) - nome.count(' '), len(qtdletras[0])))