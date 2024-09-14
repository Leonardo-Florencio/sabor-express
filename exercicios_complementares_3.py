idade_usuario = int(input('Quantos anos você tem ? '))

if idade_usuario >= 0 and idade_usuario <= 12:
    print(f'Este usuário tem {idade_usuario} anos e é criança')
elif idade_usuario >= 13 and idade_usuario <= 18:
    print(f'Este usuário tem {idade_usuario} anos e é adolescente')
else:
    print(f'Este usuário tem {idade_usuario} anos e é adulto')
    