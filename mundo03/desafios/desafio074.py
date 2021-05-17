import random
lista = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(lista)
seq = sorted(lista)
print(f'O maior valor foi: {seq[4]}')
print(f'O menor valor foi: {seq[0]}')

print(f'O maior valor foi: {max(lista)}')
print(f'O menor valor foi: {min(lista)}')
