exp = input('Digite sua expressão: ').strip()
pilha = []
for v in exp:
    if v == '(':
        pilha.append(v)
    elif v == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
