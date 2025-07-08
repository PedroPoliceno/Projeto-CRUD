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

def validacao_lista(codigo, lista):
    '''
    Faz a validação do registro
    :codigo: É o código, ou lista que o usuário deseja adicionar nos registros
    :lista: É a lista na qual o usuário quer adicionar o registro
    '''
    if lista == 'aluno' or lista == 'professor': 
        for dado in lista:
            if dado.get('codigo') == codigo:
                return True
        return False
    else:
        for dado in lista:
            if codigo == dado:
                return True
        return False
    
def cancelar_operacao(name): #Da a opção do usuário cancelar a operação.
    if name == "":
        print("\n-----OPERAÇÃO CANCELADA!-----")
        return True
    else:
        return False

def ler_arquivo_json(arquivo): #Faz a leitura do arquivo .json, para manipula-lo depois
    try:
        with open(arquivo + '.json', 'r') as f:
            lidos = json.load(f)
        
        return lidos
    except:
        lidos = []
        return lidos

def escrever_arquivo_json(arquivo, dado): #Escreve no arquivo .json
    with open(arquivo + '.json', 'w', encoding='utf-8') as f:
        json.dump(dado, f)

def add_pessoas_na_lista(lista):  #Adiciona pessoas na lista

    dados_lidos = ler_arquivo_json(lista)
    try:
        while True:
            print("(Digite 0 para cancelar.)")
            codigo = int(input(f"Digite o código do {lista}(a): "))
            if cancelar_operacao(codigo):
                return None

            elif validacao_lista(codigo, dados_lidos):
                print("\n-----Código já existe.-----\n")

            else:
                nome = input("Digite o nome: ")
                cpf = int(input("Digite o CPF: "))

                data = {'codigo': codigo, 'nome':nome, 'cpf': cpf}
                dados_lidos.append(data)
                escrever_arquivo_json(lista, dados_lidos)
                
                if input("Deseja incluir cadastros?(s/n): ") == "n":
                    return None
    except:
        print("\nDigite um dado válido\n")

def add_registro_na_lista(lista): #Adiciona registros na lista
    dados_lidos = ler_arquivo_json(lista)
    try:
        while True:
            if lista == 'disciplina':
                print('(Digite 0 para cancelar.)')
                codigo_disciplina = int(input("Digite o código da disciplina: ")) #Adiciona disciplinas em formato de dicionário
                if cancelar_operacao(codigo_disciplina):
                    return None

                elif validacao_lista(codigo_disciplina, dados_lidos):
                    print("\n-----Código já existe.-----\n")

                else:
                    nome_disciplina = input("Digite o nome da disciplina: ")
                    data = {'codigo': codigo_disciplina, 'disciplina': nome_disciplina}
                    dados_lidos.append(data)
                    escrever_arquivo_json(lista, dados_lidos)
                    
                    if input("Deseja incluir cadastros?(s/n): ") == "n":
                        return None                
            elif lista == 'turma':
                print('(Digite 0 para cancelar.)')
                turma = int(input("Digite o código da turma: ")) #Adiciona turmas em formato de lista
                if cancelar_operacao(turma):
                    return None

                else:
                    professor = int(input("Digite o código do professor: "))
                    disciplina = int(input(("Digite o código da disciplina: ")))
                    data = [turma, professor, disciplina]   
                    if validacao_lista(data, dados_lidos):
                        print("\n-----Turma já existe.-----\n")
                    else:
                        dados_lidos.append(data)
                        escrever_arquivo_json(lista, dados_lidos)
                        if input("Deseja incluir cadastros?(s/n): ") == "n":
                            return None
            elif lista == 'matrícula':
                print('(Digite 0 para cancelar.)')
                codigo_turma = int(input("Digite o código da turma: ")) #Adiciona matrículas em formato de lista
                if cancelar_operacao(codigo_turma):
                    return None
                else:
                    codigo_estudante = int(input("Digite o código do estudante: "))
                    data = [codigo_turma, codigo_estudante]

                    if validacao_lista(data, dados_lidos):
                        print("\n-----Matrícula já existe-----\n")
                    else:
                        dados_lidos.append(data)
                        escrever_arquivo_json(lista, dados_lidos)
                        if input("Deseja incluir cadastros?(s/n): ") == "n":
                                return None
    except:
        print("\nDigite um dado válido\n")

def show_lista(lista, tipo): #Exibe os registros de alunos, professores e disciplinas.
    lista_lida = ler_arquivo_json(lista)

    if len(lista_lida) == 0:
        print("-----NÃO EXISTE CADASTROS-----")
        return None
    elif tipo == 0 or tipo == 1:
        for data in lista_lida: #Mostra a lista de estudandes
            print(f'Código: {data['codigo']}, nome: {data['nome']}, cpf: {data['cpf']}')

    elif tipo == 2:
        for data in lista_lida: #Mostra a lista de disciplinas
            print(f'{lista}: {data['nome']}, código: {data['codigo']}')
        input("\nPressione ENTER para continuar.")
        return None
    elif tipo == 3:
        for data in lista_lida: #Mostra a lista de turmas
            print(f'Turma: {data[0]}, professor: {data[1]}, disciplina: {data[2]}')
    elif tipo == 4:
        for data in lista_lida: #Mostra a lista de matrículas
            print(f'Turma: {data[0]}, estudante: {data[1]}')

    input("\nPressione Enter para continuar")

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

def atualizar_lista_registros(lista, menu_atual): #Atualiza o arquivo de registros(turma, matrícula, disciplina)
    dados_lidos = ler_arquivo_json(lista)
    if menu_atual == 2:
        while True:
            if len(dados_lidos) == 0:
                print("\n-----Não existe cadastros.-----\n")
                return None
            
            else:
                print("(para cancelar a operação aperte ENTER.)")
                nome_atualizacao = int(input(f"Qual o código da {lista} que deseja atualizar?: ")) 
                if nome_atualizacao == "":
                    print("\n-----OPERAÇÃO CANCELADA!-----")
                    return None
                
                for dado in dados_lidos:
                    if dado.get('codigo') == nome_atualizacao: #Passa por toda a lista e confirma se o registro existe
                        dado['nome'] = input("Digite um novo nome: ")
                        dado['codigo'] = input('Digite um novo código: ')
                        escrever_arquivo_json(lista, dados_lidos)
                        print("\n*****Cadastro atualizado!*****\n")

                        if input("Deseja atualizar mais algum cadastro?(s/n): ") == 'n':
                            return None
                    else:
                        print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
                        return None
    elif menu_atual == 3:
        cod_turma = int(input("Digite o código da turma: "))
        cod_professor = int(input("Digite o código do professor: "))
        cod_disciplina = int(input("Digite o código da disciplina: "))
        data = [cod_turma, cod_professor, cod_disciplina]
        if validacao_lista(data, dados_lidos, 2):
            for dado in lista:
                if dado == data:
                    nova_turma = int(input("Digite o novo código da turma: "))
                    novo_professor = int(input("Digite o novo código do professor: "))
                    novo_disciplina = int(input("Digite o novo código da disciplina: "))
                    dado = [nova_turma, novo_professor, novo_disciplina]
                else:
                    print("\n-----Registro não foi encontrado-----")
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
                        atualizar_lista_registros(lista_atual, n)



                elif select == 4:
                    display_cabecalho(select,n) #Menu de excluir.
                    remova_list(lista_atual)
                                
                else:
                    print("Retornando ao Menu Principal...") #Volta ao menu principal
                    break   
            
