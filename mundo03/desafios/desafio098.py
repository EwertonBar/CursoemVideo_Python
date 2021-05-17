from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *=-1
    if passo == 0:
        passo = 1
    print(f'A contagem de {inicio} até o {fim}, de {passo} em {passo}.')
    if inicio >= fim:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
            sleep(1)
        print('FIM')
    else:
        cont = inicio           # RESETO O INÍCIO PARA FAZER O TESTE.
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
            sleep(1)
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Digite o Início: '))
f = int(input('Digite o Fim: '))
p = int(input('Digite o Passo: '))
contador(i, f, p)
