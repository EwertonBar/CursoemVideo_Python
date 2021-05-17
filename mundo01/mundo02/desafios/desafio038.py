pri=int(input('Digite o primeiro valor: '))
seg=int(input('Digite o segundo valor: '))

if pri>seg:
    print('O primeiro valor é maior que o segundo! {}>{}'.format(pri, seg))
elif seg>pri:
    print('O segundo valor é maior que o primeiro! {}>{}'.format(seg, pri))
else:
    print('O valores são iguais! {}={}'.format(pri, seg))
