#Pedro Henrique Arantes Policeno / Ánalise e Desenvolvimento de Sistemas.

'''Cria o menu principal, menu de operações, personalização do cabeçalho e a lista de estudantes(Vazia)'''

menu_principal = ["-----MENU PRINCIPAL-----",
"(1) Gerenciar estudantes.",
"(2) Gerenciar professores.",
"(3) Gerenciar disciplinas.",
"(4) Gerenciar turmas.",
"(5) Gerenciar matrículas.",
"(6) Sair."]

cabecalho_mop = [
    "[ESTUDANTES]",
    "[PROFESSORES]",
    "[DISCIPLINAS]",
    "[TURMAS]",
    "[MATRÍCULAS]"
]

menu_op = [
    "(1)Incluir.",
    "(2)Listar",
    "(3)Atualizar",
    "(4)Excluir",
    "(5)Voltar ao menu principal"
]

lista_estudantes = {}

while True: #Faz a navegação contínua.

    try:

        for c in menu_principal: #Exibe o menu principal.
            print(c)


        opcao = int(input("\nInforme a opção desejada :"))

        if opcao < 1 or opcao > 6:
            print("Por favor escolha uma opção válida.") #Valida a escolha do usuário.
            continue

        elif opcao == 6: #Faz o usuário sair do menu.
            print("Finalizando o algoritmo...")
            break

        else:   #Personaliza o cabeçalho do menu de operações com a escolha do usuário.
            if opcao == 1:
                n = 0
                while True: #Faz a navegação do menu de operações contínua.

                    print(f"\n*****{cabecalho_mop[n]}MENU DE OPERAÇÕES*****") #Cria o cabeçalho do menu de operações.

                    for i in menu_op: #Exibe as opções do menu de operações.
                        print(i)

                    select = int(input("\nInforme a ação desejada: ")) 

                    ''' Mostra a escolha do usuário na tela.'''

                    if select < 1 or select > 5: #Valída a escolha do usuário.
                        print("Insira uma ação válida.")
                        continue

                    elif select == 1: #Filtra a escolha do usuário
                        while True:
                            print(f"\n====={cabecalho_mop[n]}INCLUIR=====")   #Menu de incluir estudantes
                            print("(para cancelar a operação aperte ENTER.)") #Da a opção do usuário cancelar a operação
                            nome = input("Digite o nome do estudande que deseja incluir: ")
                            if nome == "":
                                print("\n-----OPERAÇÃO CANCELADA!-----")
                                break

                            else:
                                idade = int(input("Digite a idade do estudante: ")) #Adiciona o nome e idade do estudande no dicionário
                                lista_estudantes[nome] = idade

                            escolha_menu_incluir = input("Deseja incluir mais estudantes?(s/n): ")
                            if escolha_menu_incluir == "n":
                                break

                    elif select == 2:
                        print(f"\n====={cabecalho_mop[n]}LISTAR=====")
                        if lista_estudantes == {}:  #Caso não tenha nenhum estudande o algoritmo vai avisar
                            print("\nNão existe estudantes cadastrados")
                        
                        else:
                            for nome in lista_estudantes: #Mostra a lista de estudandes
                                print(f"{nome:>12}, {lista_estudantes[nome]} anos.")
                            input("Pressione ENTER para continuar.")

                    elif select == 3:
                            if lista_estudantes == {}:  #Caso não tenha nenhum estudande o algoritmo vai avisar
                                print("\nNão existe estudantes cadastrados")
                            
                            else:
                                while True:
                                    print(f"\n====={cabecalho_mop[n]}ATUALIZAÇÃO=====")

                                    print("(para cancelar a operação aperte ENTER.)")
                                    nome_atualizacao = input("Qual o nome do estudande quer atualizar?: ") 
                                    if nome_atualizacao == "":
                                        print("\n-----OPERAÇÃO CANCELADA!-----")
                                        break

                                    if nome_atualizacao in lista_estudantes: #Valida a escolha do usuário
                                        novo_nome = input("Digite o novo nome:")
                                        nova_idade= int(input("Digite a nova idade: "))
                                        
                                        lista_estudantes[novo_nome] = lista_estudantes.pop(nome_atualizacao) #Tira e coloca o dado dnv
                                        lista_estudantes[novo_nome] = nova_idade
                                        break

                                    else:
                                        print("Digite um nome válido.")

                    elif select == 4:
                            while True:
                                print(f"\n====={cabecalho_mop[n]}EXCLUIR=====")
                                if lista_estudantes == {}:
                                    print("\nNão existe estudantes cadastrados")
                                    break

                                else:
                                    print("(para cancelar a operação aperte ENTER.)")
                                    nome_excluir = input("Digite o nome do estudante que deseja excluir: ")
                                    if nome_excluir == "":
                                        print("\n-----OPERAÇÃO CANCELADA!-----")
                                        break

                                    elif nome_excluir in lista_estudantes: #Valida a escolha do usuário
                                        print(f"\nO estudante {nome_excluir} foi excluído do cadastro.") #Avisa o nome do estudante que foi tirado
                                        del lista_estudantes[nome_excluir]

                                        escolha_menu_excluir = input("Deseja excluir mais estudantes?(s/n): ")

                                        if escolha_menu_excluir == "n":
                                            break

                                    else:
                                        print("\nDigite um nome válido") 

                    else:
                        print("Retornando ao Menu Principal...") #Volta ao menu principal
                        break

            elif opcao == 2: #Caso o usuário escolha alguma opção que não seja estudantes.
                print("\nEM DESENVOLVIMENTO...\n")

            elif opcao == 3:
                print("\nEM DESENVOLVIMENTO...\n")

            elif opcao == 4:
                print("\nEM DESENVOLVIMENTO...\n")

            elif opcao == 5:
                print("\nEM DESENVOLVIMENTO...\n")

    except:     #Mensagem caso tenha algum erro nos dados do usuário.
        print("\nDigite um dado válido.\n")