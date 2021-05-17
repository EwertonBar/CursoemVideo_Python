#números pares entre 1 e 50
print('{}'.format('\033[44:4mNúmeros pares entre 1 e 50\033[m'))
for c in range (1,51):
    if c % 2 == 0:
        print(c, end=' ')
print('fim')