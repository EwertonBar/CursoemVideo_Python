lista = {'nome':'Ewerton', 'idade': 28, 'sexo': 'M'}
print(lista)
print(lista['nome'])
print(lista.keys())
print(lista.values())
print(lista.items())
print(f'O {lista["nome"]} tem {lista["idade"]} anos')
for k in lista.keys():
    print(k)
for v in lista.values():
    print(v)
for k,v in lista.items():
    print(f'{k} = {v}')