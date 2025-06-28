#Pedro Henrique Arantes Policeno / Ánalise e Desenvolvimento de Sistemas.

'''Cria o menu principal, menu de operações, personalização do cabeçalho e uma lista de listas das opções'''
def display_main_menu():
    menu_principal = ["-----MENU PRINCIPAL-----",
    "(1) Gerenciar estudantes.",
    "(2) Gerenciar professores.",
    "(3) Gerenciar disciplinas.",
    "(4) Gerenciar turmas.",
    "(5) Gerenciar matrículas.",
    "(6) Sair."]

    for c in menu_principal: #Exibe o menu principal.
            print(c)

def display_op_menu(cabecalho, menu_atual):
    menu_op = [
        "(1)Incluir.",
        "(2)Listar",
        "(3)Atualizar",
        "(4)Excluir",
        "(5)Voltar ao menu principal"
    ]
    print(f"*****{cabecalho[menu_atual]}MENU DE OPERAÇÕES*****") #Cria o cabeçalho do menu de operações.

    for i in menu_op: #Exibe as opções do menu de operações.
        print(i)

personalizacao = [
    "do estudante",
    "do professor(a)",
    "da disciplina",
    "da turma",
    "da matrícula"
]

cabecalho_mop = [
    "[ESTUDANTES]",
    "[PROFESSORES]",
    "[DISCIPLINAS]",
    "[TURMAS]",
    "[MATRÍCULAS]"
]




listas = {}

while True: #Faz a navegação contínua.    

        
        display_main_menu()

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

                display_op_menu(cabecalho_mop, n)

                select = int(input("Informe a ação desejada: "))

                if select < 1 or select > 5: #Valída a escolha do usuário.
                    print("Insira uma ação válida.")
                    continue

                elif select == 1: #Filtra a escolha do usuário
                    print(f"====={cabecalho_mop[n]}INCLUIR=====")   #Menu de incluir estudantes
                    primary_data = (input(f"Digite o nome {personalizacao[n]} que deseja incluir: "))



                elif select == 2:
                    print(f"====={cabecalho_mop[n]}LISTAR=====")
                    if primary_data not in listas:  #Caso não tenha nenhum estudande o algoritmo vai avisar
                        print("Não existe cadastros")
                    
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