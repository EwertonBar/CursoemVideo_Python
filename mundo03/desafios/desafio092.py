import datetime
cadastro = dict()
ctps = 1
while ctps != 0:
    cadastro['nome']=str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    ano = datetime.date.today().year
    cadastro['idade']=ano-nasc
    ctps = int(input('Nº carteira de trabalho: [0 se não tiver] '))
    if ctps == 0:
        cadastro['CTPS'] = 0
        for k, v in cadastro.items():
            print(f'{k}: {v}.')
        break
    else:
        cadastro['CTPS'] = ctps
        cadastro['Contratação'] = int(input('Ano de contratação: '))
        cadastro['Salário'] = float(input('Salário? R$ '))
        for k, v in cadastro.items():
            print(f'{k}: {v}.')
        break
print('Obrigado por utilizar!')