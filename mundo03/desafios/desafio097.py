def mensagem(msg):
    a = len(msg) + 6
    print('-'*a)
    print(f'{msg:^{a}}')
    print('-'*a)


mensagem('Alô comunidade')