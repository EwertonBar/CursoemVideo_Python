linha = [[], [], [], [], [], [], [], [], []]
a=b=c=0
for v in range (0,9):
    if v <= 2:
        termo = int(input('Digite um valor para [0, {}]: '.format(a)))
        a+=1
        linha[v].append(termo)
    elif 2 < v <= 5:
        termo = int(input('Digite um valor para [1, {}]: '.format(b)))
        b += 1
        linha[v].append(termo)
    else:
        termo = int(input('Digite um valor para [2, {}]: '.format(c)))
        c += 1
        linha[v].append(termo)
print(linha[:3])
print(linha[3:6])
print(linha[6:])
