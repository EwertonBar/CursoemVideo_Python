try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Problema encontrado no tipo de dado inserido.!')
except ZeroDivisionError:
    print(f'Não é possível dividir por zero.')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(r)
finally:
    print('Volte sempre. Obrigado')