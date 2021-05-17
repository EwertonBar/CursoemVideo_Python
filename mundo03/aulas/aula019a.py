estado = { }
brasil = [ ]
for c in range (0,2):
    estado['uf']=str(input('Unidade federativa: '))
    estado['sigla']=str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.items():
        print(v)
