from datetime import date
nasc=int(input('Qual seu ano de nascimento? '))
anoatual = date.today().year
idade=anoatual-nasc
if idade==18:
    print('Você deve se alistar esse ano ainda!'.format(idade))
elif idade<18:
    print('Está quase. Falta: {} ano(s) para você se alistar!'.format(18-idade))
else:
    print('Você passou {} ano(s) do prazo.'.format(idade-18))