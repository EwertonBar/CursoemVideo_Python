n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
r = 4
while r != 5:
    r = int(input('O que você deseja? \n[1] Soma \n[2] Multiplicar \n[3] Qual é maior \n[4] Digitar novos valores \n[5] Sair do programa \nR: '))
    if r == 1:
        print('Soma: {}'.format(n1+n2))
    elif r==2:
        print('Multiplicação: {}'.format(n1*n2))
    elif r==3:
        if n1>n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n2>n1:
            print('{} é maior que {}'.format(n2,n1))
        else:
            print('Os valores são iguais! {}={}'.format(n1,n2))
    elif r == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite um valor: '))
    print('x'*30)
print("\nPrograma finalizado!")
