num = [0,1,5,2,4]
num[2] = 3
num.append(5)
num.sort(reverse=True)
num.insert(2,2)
if 7 in num:
    num.remove(7)
else:
    print('Não há número 7 na lista!')
print(num)
print(f'Quantidade de elementos na lista: {len(num)}')