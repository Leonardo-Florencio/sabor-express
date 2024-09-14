print('Sabor Express\n')

print('1. Cadastrar restaurante')
print('2. Listar restaurantes')
print('3. Ativar restaurante')
print('4. Sair da aplicação\n')

opcao_escolhida = int(input('Escolha uma opção: '))
print(f'Você escolheu a opção {opcao_escolhida}')
#opcao_escolhida = int(opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print ('Listar restaurantes')
elif opcao_escolhida == 3:
    print ('Ativar restaurante')
else:
    print('Encerrando programa')