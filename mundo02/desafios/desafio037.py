num=int(input('Digite um número inteiro qualquer: '))

base=int(input('Digite 1 para mudança de base para binário. \nDigite 2 oara mudança de base para octal. \nDigite 3 para mudança de base para hexadecimal. \n' ))

if base == 1:
    print('Seu número em base binário: {}'.format(bin(num)[2:]))
elif base==2:
    print('Seu número em base octal: {}'.format(oct(num)[2:]))
elif base==3:
    print('Seu número em base hexadecimal: {}'.format(hex(num)[2:]))
else:
    print('Opção inválida!')


