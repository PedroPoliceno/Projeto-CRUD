#Pedro Henrique Arantes Policeno / Ánalise e Desenvolvimento de Sistemas.

'''Cria o menu principal, menu de operações, personalização do cabeçalho e uma lista de listas das opções'''

menu_principal = ["-----MENU PRINCIPAL-----",
"(1) Gerenciar estudantes.",
"(2) Gerenciar professores.",
"(3) Gerenciar disciplinas.",
"(4) Gerenciar turmas.",
"(5) Gerenciar matrículas.",
"(6) Sair."]

personalizacao = [
    "estudante",
    "professor",
    "disciplina",
    "turma",
    "matrícula"
]

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


listas = [[],[],[],[],[]]

while True: #Faz a navegação contínua.    

        for c in menu_principal: #Exibe o menu principal.
            print(c)


        opcao = int(input("Informe a opção desejada :"))

        if opcao < 1 or opcao > 6:
            print("Por favor escolha uma opção válida.") #Valida a escolha do usuário.
            continue

        elif opcao == 6: #Faz o usuário sair do menu.
            print("Finalizando o algoritmo...")
            break

        else:   #Personaliza o cabeçalho do menu de operações com a escolha do usuário.
            if opcao == 1:
                n = 0
                
            elif opcao == 2: #Caso o usuário escolha alguma opção que não seja estudantes.
                n = 1

            elif opcao == 3:
                n = 2

            elif opcao == 4:
                n = 3

            elif opcao == 5:
                n = 4

            while True: #Faz a navegação do menu de operações contínua.

                    print(f"*****{cabecalho_mop[n]}MENU DE OPERAÇÕES*****") #Cria o cabeçalho do menu de operações.

                    for i in menu_op: #Exibe as opções do menu de operações.
                        print(i)

                    select = int(input("Informe a ação desejada: ")) 

                    ''' Mostra a escolha do usuário na tela.'''

                    if select < 1 or select > 5: #Valída a escolha do usuário.
                        print("Insira uma ação válida.")
                        continue

                    elif select == 1: #Filtra a escolha do usuário
                        print(f"====={cabecalho_mop[n]}INCLUIR=====")   #Menu de incluir estudantes
                        listas[n].append(input(f"Digite o nome do {personalizacao[n]} que deseja incluir: "))

                    elif select == 2:
                        print(f"====={cabecalho_mop[n]}LISTA=====")
                        if len(listas[n])== 0:  #Caso não tenha nenhum estudande o algoritmo vai avisar
                            print("Não existe",personalizacao[n],"no cadastrado")
                        
                        else:
                            for i in range(len(listas[n])): #Mostra a lista de estudandes
                                print('-', listas[n][i])
                            input("Pressione ENTER para continuar.")

                    elif select == 3:
                        print(f"====={cabecalho_mop[n]}ATUALIZAÇÃO=====")
                        print("EM DESENVOLVIMENTO...")

                    elif select == 4:
                        print(f"====={cabecalho_mop[n]}EXCLUIR=====")
                        print("EM DESENVOLVIMENTO...")

                    else:
                        print("Retornando ao Menu Principal...")
                        break