def mensagem(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))


mensagem('Área do terreno')

def area(larg, comp):
    a = larg*comp
    print(f'A área para um terreno de {larg}x{comp} vale {a}m².')

a = float(input('Digite a largura: '))
b = float(input('Digite o comprimento: '))
area(a, b)
