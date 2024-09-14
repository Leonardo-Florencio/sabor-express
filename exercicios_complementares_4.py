usuario = 'dittopk'
senha = 'eUmaTristezaNaoTerPersonalidadeDefinida143'

usuario_fornecido = input('Informe o nome de usuário: ')
senha_fornecida = input('Informe a senha: ')

if usuario_fornecido == usuario and senha_fornecida == senha:
    print('Acesso liberado')
elif usuario_fornecido != usuario and senha_fornecida == senha:
    print('Usuário não cadastrado, verifique as credenciais')
elif usuario_fornecido == usuario and senha_fornecida != senha:
    print('Senha incorreta')
else:
    print('Acesso negado, verifique as credenciais')