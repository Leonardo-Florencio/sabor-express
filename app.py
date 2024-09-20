import os #utilizado para chamar a biblioteca OS, que permite o uso do método os.system('cls), que limpa o cmd quando utilizado

array_restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                      {'nome': 'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                      {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}] #utilização de dicionários, conhecidos em outras linguagens como "chave-valor", quase a mesma ideia de um objeto em JS.

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair da aplicação\n')

def finalizar_app():
    exibir_subtitulos('Finalizando aplicação')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    array_restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in array_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado' #método ternário de teste, ao invés do bloco padrão - valor se verdadeiro, teste que deve ser verdadeiro e valor caso seja false apos o else
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}')
        
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in array_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #not é um método que inverte o valor, se for true, vai para false e vice-versa
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante  {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()