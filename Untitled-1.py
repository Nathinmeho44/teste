
while True:
    Any = input('digite o nome de sua conta: ')
    Who = input('digite a senha de sua conta: ')
    if Any != Who:
        print ('Seja bem-vindo de volta ao ECIT Tech.')
    else:
        while Who:
            print ('Sua senha e nome não podem ser identicos.')
            if Who != Any:
                ('Tudo bem, bem-vindo')
                break