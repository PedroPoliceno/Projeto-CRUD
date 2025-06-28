#Pedro Henrique Arantes Policeno / Ánalise e Desenvolvimento de Sistemas.
import json

def display_main_menu(): #Exibe o menu principal.
    menu_principal = ["-----MENU PRINCIPAL-----",
    "(1) Gerenciar estudantes.",
    "(2) Gerenciar professores.",
    "(3) Gerenciar disciplinas.",
    "(4) Gerenciar turmas.",
    "(5) Gerenciar matrículas.",
    "(6) Sair."]

    for c in menu_principal: 
            print(c)

cabecalho_mop = [ #Cria uma personalização para o cabeçalho do menu de operações.
        "[ESTUDANTES]",
        "[PROFESSORES]",
        "[DISCIPLINAS]",
        "[TURMAS]",
        "[MATRÍCULAS]"
    ]

def display_op_menu(menu_atual): #Mostra o menu de operações.

    menu_op = [
    "(1)Incluir.",
    "(2)Listar",
    "(3)Atualizar",
    "(4)Excluir",
    "(5)Voltar ao menu principal"
    ]
    
    print(f"\n*****{cabecalho_mop[menu_atual]}MENU DE OPERAÇÕES*****") #Cria o cabeçalho do menu de operações.

    for i in menu_op: #Exibe as opções do menu de operações.
        print(i)

def display_cabecalho(opcao_atual, menu_atual): #Mostra o cabeçalho das opções.

    if opcao_atual == 1:

        print(f"\n====={cabecalho_mop[menu_atual]}INCLUIR=====")
    if opcao_atual == 2:

        print(f"\n====={cabecalho_mop[menu_atual]}LISTAR=====")
    if opcao_atual == 3:

        print(f"\n====={cabecalho_mop[menu_atual]}ATUALIZAÇÃO=====")
    if opcao_atual == 4:

        print(f"\n====={cabecalho_mop[menu_atual]}EXCLUIR=====")

def validacao_lista(name, lista): #Faz a validação para ver se o nome adicionado já não existe no cadastro.
    for dado in lista:
        if dado.get('nome') == name:
                return True
    
    return False

def cancelar_operacao(name): #Da a opção do usuário cancelar a operação.
    if name == "":
        print("\n-----OPERAÇÃO CANCELADA!-----")
        return True
    else:
        return False

def ler_arquivo_json(arquivo):
    try:
        with open(arquivo + '.json', 'r') as f:
            lidos = json.load(f)
        
        return lidos
    except:
        lidos = []
        return lidos

def escrever_arquivo_json(arquivo, dado):
    with open(arquivo + '.json', 'w', encoding='utf-8') as f:
        json.dump(dado, f)

def add_pessoas_na_lista(lista):  #Adiciona pessoas na lista

    dados_lidos = ler_arquivo_json(lista)
    while True:
        print("(Pressione Enter para cancelar.)")
        nome = input(f"Digite o nome do {lista}(a): ")
        if cancelar_operacao(nome):
            return None

        elif validacao_lista(nome, dados_lidos):
            print("\nCadastro já existe.\n")
            return None

        else:
            idade = int(input("Digite a idade: "))
            cpf = int(input("Digite o CPF: "))

            data = {'nome':nome, 'idade': idade, 'cpf': cpf}
            dados_lidos.append(data)
            escrever_arquivo_json(lista, dados_lidos)
            
            if input("Deseja incluir cadastros?(s/n): ") == "n":
                return None

def add_registro_na_lista(lista):

    while True:
        print("(Pressione Enter para cancelar.)")
        nome = input(f"Digite o nome da {lista}: ")
        if cancelar_operacao(nome):
            return None
        
        else:
            codigo = int(input(f"Digite o código da {lista}: "))

            data = {'nome':nome, 'codigo': codigo}
            dados_lidos = ler_arquivo_json(lista)
            dados_lidos.append(data)
            escrever_arquivo_json(lista, dados_lidos)
                        
            if input("Deseja incluir cadastros?(s/n): ") == "n":
                return None

def show_lista(lista, tipo): #Exibe todos os registros
    lista_lida = ler_arquivo_json(lista)

    if len(lista_lida) == 0:
        print("-----NÃO EXISTE CADASTROS-----")
        return None
    elif tipo == 0 or tipo == 1:
        for data in lista_lida: #Mostra a lista de estudandes
            print(f'Nome: {data['nome']}, idade: {data['idade']}, cpf: {data['cpf']}')

    else:
        for data in lista_lida: #Mostra a lista de registros
            print(f'{lista}: {data['nome']}, código: {data['codigo']}')
        input("\nPressione ENTER para continuar.")
        return None

def atualizar_lista_pessoa(lista): #Atualiza o arquivo de pessoas(estudantes e professores)
    dados_lidos = ler_arquivo_json(lista)
    while True:
        if len(dados_lidos) == 0:
            print("Não existe cadastros.\n")
            return None
        
        else:
            print("(para cancelar a operação aperte ENTER.)")
            nome_atualizacao = input(f"Qual o nome do {lista} que deseja atualizar?: ") 
            if nome_atualizacao == "":
                print("\n-----OPERAÇÃO CANCELADA!-----")
                return None
            
            for dado in dados_lidos:
                if dado.get('nome') == nome_atualizacao: #Passa por toda a lista e confirma se o registro existe
                    dado['nome'] = input("Digite um novo nome: ")
                    dado['idade'] = input('Digite a nova idade: ')
                    dado['cpf'] = input("Digite o novo cpf: ")
                    escrever_arquivo_json(lista, dados_lidos)
                    print("\n*****Cadastro atualizado!*****\n")

                    if input("Deseja atualizar mais algum cadastro?(s/n)") == 'n':
                        return None
            else:
                print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
                return None

def atualizar_lista_registros(lista): #Atualiza o arquivo de registros(turma, matrícula, disciplina)
    dados_lidos = ler_arquivo_json(lista)
    while True:
        if len(dados_lidos) == 0:
            print("\n-----Não existe cadastros.-----\n")
            return None
        
        else:
            print("(para cancelar a operação aperte ENTER.)")
            nome_atualizacao = input(f"Qual o nome do {lista} que deseja atualizar?: ") 
            if nome_atualizacao == "":
                print("\n-----OPERAÇÃO CANCELADA!-----")
                return None
            
            for dado in dados_lidos:
                if dado.get('nome') == nome_atualizacao: #Passa por toda a lista e confirma se o registro existe
                    dado['nome'] = input("Digite um novo nome: ")
                    dado['codigo'] = input('Digite um novo código: ')
                    escrever_arquivo_json(lista, dados_lidos)
                    print("\n*****Cadastro atualizado!*****\n")

                    if input("Deseja atualizar mais algum cadastro?(s/n): ") == 'n':
                        return None
                else:
                    print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
                    return None

def remova_list(lista):
     dados_lidos = ler_arquivo_json(lista)
     while True:
        print("(para cancelar a operação aperte ENTER.)")
        nome_excluir = input("Digite o nome do cadastro que deseja excluir: ")
        if cancelar_operacao(nome_excluir):
            return None
        
        else:
            for cadastro in dados_lidos:
                if cadastro.get('nome') == nome_excluir:
                    dados_lidos.remove(cadastro)
                    print(f'\n*****Cadastro removido*****\n')
                    escrever_arquivo_json(lista, dados_lidos)
                    return None
                
                print("-----CADASTRO NÃO ENCONTRADO-----\n")
                return None
                
while True: #Faz a navegação contínua.
    
    display_main_menu()
    try:
        opcao = int(input("\nInforme a opção desejada :"))

        if opcao < 1 or opcao > 6:
            print("\n-----Escolha uma opção válida-----\n") #Valida a escolha do usuário.
            continue

        elif opcao == 6: #Faz o usuário sair do menu.
            print("Finalizando o algoritmo...")
            break

        else:   
            if opcao == 1:
                n = 0 #Personaliza o cabeçalho do menu de operações com a escolha do usuário, usando a váriavel cabecalho_mop.
                lista_atual = 'aluno' #Personaliza o nome do arquivo.json que vamos usar.

            elif opcao == 2:
                n = 1
                lista_atual = 'professor'

            elif opcao == 3:
                n = 2
                lista_atual = 'disciplina'

            elif opcao == 4:
                n = 3
                lista_atual = 'turma'

            elif opcao == 5:
                n = 4
                lista_atual = 'matrícula'

            while True: #Faz a navegação do menu de operações contínua.
                try:
                    display_op_menu(n)

                    select = int(input("\nInforme a ação desejada: ")) 

                    if select < 1 or select > 5: #Valída a escolha do usuário.
                        print("\n-----Insira uma ação válida.-----\n")
                        continue

                    elif select == 1: #Filtra a escolha do usuário
                        
                        display_cabecalho(select, n) #Menu de adicionar cadastros
                        if n == 0 or n == 1:
                            add_pessoas_na_lista(lista_atual)

                        else:
                            add_registro_na_lista(lista_atual)

                    elif select == 2:
                        display_cabecalho(select, n) #Menu de listagem

                        show_lista(lista_atual, n)

                    elif select == 3:
                        display_cabecalho(select, n) #Menu de atualização
                        if n == 0 or n == 1:
                            atualizar_lista_pessoa(lista_atual)

                        else:
                            atualizar_lista_registros(lista_atual)              

                    elif select == 4:
                        display_cabecalho(select,n) #Menu de excluir.
                        remova_list(lista_atual)
                                    
                    else:
                        print("Retornando ao Menu Principal...") #Volta ao menu principal
                        break
                    
                except ValueError:
                    print("\n-----Digite uma opção válida-----\n") #Valor inválido no menu de operações
    except:
        print("\n-----Digite uma opção válida-----\n") #Valor inválido no menu principal
        continue