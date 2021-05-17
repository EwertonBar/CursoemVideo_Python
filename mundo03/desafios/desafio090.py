ficha = { }
ficha['nome']=str(input('Nome: '))
ficha['média']=int(input('Média: '))
if ficha['média'] >= 7:
    ficha['situação']= 'APROVADO'
else:
    ficha['situação']='RECUPERAÇÃO'

for k, v in ficha.items():
    print(f'{k} é igual: {v}')