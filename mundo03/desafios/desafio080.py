lista = []
for n in range (0,5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('Seu número foi adicionado no fim da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Seu número foi adicionado na posição {pos}.')
                break
            pos+=1
print(lista)