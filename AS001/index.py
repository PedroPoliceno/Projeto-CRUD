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

lista_estudantes = []

while True: #Faz a navegação contínua.

    try:

        for c in menu_principal: #Exibe o menu principal.
            print(c)


        opcao = int(input("Informe a opção desejada :"))

        if opcao < 1 or opcao > 6:
            print("\nPor favor escolha uma opção válida.\n") #Valida a escolha do usuário.
            continue

        elif opcao == 6: #Faz o usuário sair do menu.
            print("\nFinalizando o algoritmo...\n")
            break

        else:   #Personaliza o cabeçalho do menu de operações com a escolha do usuário.
            if opcao == 1:
                n = 0
                while True: #Faz a navegação do menu de operações contínua.

                    print(f"\n*****{cabecalho_mop[n]}MENU DE OPERAÇÕES*****") #Cria o cabeçalho do menu de operações.

                    for i in menu_op: #Exibe as opções do menu de operações.
                        print(i)

                    select = int(input("Informe a ação desejada: ")) 

                    ''' Mostra a escolha do usuário na tela.'''

                    if select < 1 or select > 5: #Valída a escolha do usuário.
                        print("Insira uma ação válida.")
                        continue

                    elif select == 1: #Filtra a escolha do usuário
                        print(f"====={cabecalho_mop[n]}INCLUIR=====")   #Menu de incluir estudantes
                        lista_estudantes.append(input("\nDigite o nome do estudande que deseja incluir: "))

                    elif select == 2:
                        print(f"====={cabecalho_mop[n]}LISTAR=====")
                        if lista_estudantes == []:  #Caso não tenha nenhum estudande o algoritmo vai avisar
                            print("\nNão existe estudantes cadastrados\n")
                        
                        else:
                            for i in range(len(lista_estudantes)): #Mostra a lista de estudandes
                                print('-', lista_estudantes[i])
                            input("\nPressione ENTER para continuar.\n")

                    elif select == 3:
                        print(f"====={cabecalho_mop[n]}ATUALIZAÇÃO=====")
                        print("\nEM DESENVOLVIMENTO...\n")

                    elif select == 4:
                        print(f"====={cabecalho_mop[n]}EXCLUIR=====")
                        print("\nEM DESENVOLVIMENTO...\n")

                    else:
                        print("\nRetornando ao Menu Principal...\n")
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
        print("Digite um dado válido.")