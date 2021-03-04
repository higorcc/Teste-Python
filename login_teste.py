login = 'Higor'
senha = 1234

login_user = input('Digite seu login: ')
senha_user = int(input('Digite sua senha: '))

if login_user == login and senha_user == senha:
    print('Seja bem-vindo')
elif login_user == login and senha_user != senha:
    print('Senha não confere')
elif
else:
    print('Acesso negado')