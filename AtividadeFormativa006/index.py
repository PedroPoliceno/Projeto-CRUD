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

def validacao_lista(cod_validar, lista, nome_lista): #Faz a validação para ver se o nome adicionado já não existe no cadastro.
    if nome_lista == 'aluno' or nome_lista == 'professor':
        for dado in lista:
            if dado.get('codigo') == cod_validar:
                    return True
    else:    
        if cod_validar in lista:
            return True
        return False

def validar_cpf_nome(dado_validar, lista, nome_lista): #Valida o cpf ou nome.
    if nome_lista == 'aluno' or nome_lista == 'professor':        
        for dado in lista:
            if dado.get('cpf') == dado_validar:
                return True
    else:
        for dado in lista:
            if dado.get('nome') == dado_validar:
                return True
            
def cancelar_operacao(name): #Da a opção do usuário cancelar a operação.
    if name == 0:
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
    try:
        while True:
            print("(Digite 0 para cancelar.)")
            codigo = int(input(f"Digite o código do {lista}: "))
            if cancelar_operacao(codigo):
                return None

            elif validacao_lista(codigo, dados_lidos, lista):
                print("\nCadastro já existe.\n")
                return None

            else:
                nome = input(f"Digite o nome do {lista}(a): ")
                cpf = int(input("Digite o CPF: "))
                if validar_cpf_nome(cpf, dados_lidos, lista):
                    print("\nCpf já está cadastrado!\n")
                    return None

                data = {'codigo':codigo, 'nome':nome, 'cpf': cpf}
                dados_lidos.append(data)
                escrever_arquivo_json(lista, dados_lidos)
                
                if input("Deseja incluir cadastros?(s/n): ") == "n":
                    return None
    except:
        print('\nDigite um dado válido\n')

def add_registro_na_lista(lista):
    dados_lidos = ler_arquivo_json(lista)
    try:
        while True:
            if lista == 'disciplina':
                print("(Digite 0 para cancelar.)")
                codigo = int(input(f"Digite o código da {lista}: ")) #Faz todas as validações
                if cancelar_operacao(codigo):
                    return None
                nome = input(f"Digite o nome da disciplina: ")
                if validar_cpf_nome(nome, dados_lidos, lista):
                    print("\nNome já cadastrado!\n")
                    return None
                data = {'nome':nome, 'codigo': codigo}
                
                if validacao_lista(data, dados_lidos, lista):
                    print("\nCadastro já existe.\n")
                    return None

            if lista == 'turma':
                print("(Digite 0 para cancelar.)")
                turma = int(input("Digite o código da turma: "))
                if cancelar_operacao(turma):
                    return None
                        
                professor = int(input("Digite o código do professor: "))
                disciplina = int(input("Digite o código da disciplina: "))
                data = {'codigo':turma, 'professor':professor, 'disciplina': disciplina}
                if validacao_lista(data, dados_lidos, lista):
                    print("\nCadastro já existe.\n")
                    return None
                
            if lista == 'matrícula':
                print("(Digite 0 para cancelar.)")
                turma = int(input("Digite o código da turma: "))
                if cancelar_operacao(turma):
                    return None
                estudante= int(input("Digite o código do estudante: "))
                data = {'turma':turma, 'estudante':estudante}
                if validacao_lista(data, dados_lidos, lista):
                    print('\nCadastro já existe.\n')
                    return None
                
            dados_lidos.append(data)
            escrever_arquivo_json(lista, dados_lidos)
            print("Cadastro criado!")
            if input("Deseja adicionar mais cadastros? (s/n): ") == 'n':
                return None
    except:
        print('\nDigite um dado válido\n')

def show_lista(lista): #Exibe todos os registros
    lista_lida = ler_arquivo_json(lista)

    if len(lista_lida) == 0:
        print("-----NÃO EXISTE CADASTROS-----")
        return None
    elif lista == 'aluno' or lista == 'professor':
        for data in lista_lida: #Mostra a lista de estudandes e professores
            print(f'Código: {data['codigo']}, nome: {data['nome']}, cpf: {data['cpf']}')

    elif lista == 'disciplina':
        for data in lista_lida: #Mostra a lista de disciplinas
            print(f'Nome: {data['nome']}, código: {data['codigo']}')
        
    elif lista == 'turma':
        for data in lista_lida: #Mostra a lista de disciplinas
            print(f'Turma: {data['codigo']}, professor: {data['professor']}, disciplina: {data['disciplina']}')
        
    else:
        for data in lista_lida: #Mostra a lista de disciplinas
            print(f'Turma: {data['turma']}, estudante: {data['estudante']}')

    input("\nPressione ENTER para continuar.")
    return None    

def atualizar_lista_pessoa(lista): #Atualiza o arquivo de pessoas(estudantes e professores)
    dados_lidos = ler_arquivo_json(lista)
    while True:
        try:
            if len(dados_lidos) == 0:
                print("Não existe cadastros.\n")
                return None
            
            else:
                print("(Digite 0 para cancelar.)")
                codigo_atualizacao = int(input(f"Qual o código do {lista}(a) que deseja atualizar?: "))
                if cancelar_operacao(codigo_atualizacao):
                    return None
                else:
                    encontrado = False
                    for dado in dados_lidos:
                        if dado.get('codigo') == codigo_atualizacao: #Passa por toda a lista e confirma se o registro existe
                            dado['codigo'] = int(input('Digite o novo código: '))
                            dado['nome'] = input("Digite um novo nome: ")
                            cpf_novo = input("Digite o novo cpf: ")
                            if validar_cpf_nome(cpf_novo, dados_lidos, lista):
                                print("\nCpf já cadastrado!\n")
                                return None
                            dado['cpf'] = cpf_novo
                            escrever_arquivo_json(lista, dados_lidos)
                            encontrado = True
                            print("\n*****Cadastro atualizado!*****\n")

                    if not encontrado:
                        print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
                        return None
                    else: 
                        if input("Deseja atualizar mais algum cadastro?(s/n)") == 'n':
                            return None
        except:
            print("\nDigite um dado válido.\n")

def modificar_registros_lista(old_data, new_data, lista): #Modifica as listas 
    for i, item in enumerate(lista): #Passa pela lista identificando os dicionários
        if item == old_data:    #Identifica o dicionário que queremos modificar
            lista[i].update(new_data)   #Modifica o dicionário inteiro de uma vez
            return lista #Retorna a lista modificada
        
    return print("Algo deu errado!")

def atualizar_lista_registros(lista): #Atualiza o arquivo de registros(turma, matrícula, disciplina)
    dados_lidos = ler_arquivo_json(lista)
    while True:
        try:
            if len(dados_lidos) == 0:
                print("\n-----Não existe cadastros.-----\n")
                return None
            
            elif lista == 'disciplina':
                print("(Digite 0 para cancelar.)")
                codigo_antigo = int(input("Qual o código do disciplina que deseja atualizar?: "))
                if cancelar_operacao(codigo_antigo):
                    return None
                nome_antigo = input("Digite o nome da disciplina que deseja atualizar?: ")
                dado_antigo = {'nome':nome_antigo, 'codigo': codigo_antigo}
                if validacao_lista(dado_antigo, dados_lidos, lista):
                    novo_codigo = int(input('Digite um novo código: '))
                    novo_nome = input("Digite um novo nome: ")
                    dado_novo = {'nome':novo_nome, 'codigo': novo_codigo}
                    dados_lidos = modificar_registros_lista(dado_antigo,dado_novo,dados_lidos)
                    escrever_arquivo_json(lista, dados_lidos)
                    print("\n*****Cadastro atualizado!*****\n")
                else:
                
                    print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
                    return None
            elif lista == 'turma':
                print("(Digite 0 para cancelar.)")
                antigo_turma = int(input("Digite o código da turma: "))
                if cancelar_operacao(antigo_turma):
                    return None
                antigo_professor = int(input("Digite o código do professor: "))
                antigo_disciplina = int(input("Digite o código da disciplina: "))
                dado_antigo = {'codigo':antigo_turma, 'professor':antigo_professor, 'disciplina': antigo_disciplina}
                if validacao_lista(dado_antigo, dados_lidos, lista):

                    novo_turma = int(input("Digite o novo código da turma: "))
                    novo_professor = int(input("Digite o novo código do professor: "))
                    novo_disciplina = int(input("Digite o novo código da disciplina: "))
                    dado_novo = {'codigo':novo_turma, 'professor':novo_professor, 'disciplina': novo_disciplina}
                    if validacao_lista(dado_novo, dados_lidos, lista):
                        print("-----CADASTRO JÁ EXISTE-----")   #Impede de atualizar o cadastro com um que já existe
                        return None
                    dados_lidos = modificar_registros_lista(dado_antigo, dado_novo, dados_lidos)
                    escrever_arquivo_json(lista, dados_lidos)
                    print("\n*****Cadastro atualizado!*****\n")
                    
                else:
                    print("\n-----CADASTRO NÃO ENCONTRADO-----\n")
            else:
                print("(Digite 0 para cancelar.)")
                antigo_turma = int(input("Digite o código da turma: "))
                if cancelar_operacao(antigo_turma):
                    return None
                
                antigo_estudante = int(input("Digite o código do estudante: "))
                dado_antigo = {'codigo':antigo_turma, 'estudante':antigo_estudante}
                if validacao_lista(dado_antigo, dados_lidos, lista):
                    novo_turma = int(input("Digite o novo código da turma: "))
                    novo_estudante = int(input("Digite o novo código do estudante: "))
                    dado_novo = {'turma':novo_turma, 'estudante':novo_estudante}
                    if validacao_lista(dado_novo, dados_lidos, lista):
                        print("-----CADASTRO JÁ EXISTE-----") #Impede de atualizar o cadastro com um que já existe
                        return None
                    dados_lidos = modificar_registros_lista(dado_antigo, dado_novo, dados_lidos)
                    escrever_arquivo_json(lista, dados_lidos)
                    print("\n*****Cadastro atualizado!*****\n")
                else:
                    print("\n-----CADASTRO NÃO ENCONTRADO-----\n")

            if input("Deseja atualizar mais algum cadastro?(s/n): ") == 'n':
                return None
        except:
            print("\nDigite um dado válido.\n")
            continue
        
def remova_list(lista): #Remove os módulos que tem código próprio(Estudantes, Professores, Disciplinas e Turmas)
     dados_lidos = ler_arquivo_json(lista)
     while True:
        try:
            if len(dados_lidos) == 0:
                print("\n-----NÃO EXISTE CADASTROS-----\n")
                return None
            elif lista == 'matrícula':
                print("(Digite 0 para cancelar.)")
                excluir_turma = int(input("Digite o código da turma que deseja excluir: "))
                if cancelar_operacao(excluir_turma):
                    return None
                
                excluir_estudante = int(input("Digite o código do estudante que deseja exlcluir: "))
                dado_excluir = {'turma':excluir_turma, 'estudante':excluir_estudante}
                if dado_excluir in dados_lidos:
                    dados_lidos.remove(dado_excluir)
                    escrever_arquivo_json(lista, dados_lidos)
                    print(f'\n*****Cadastro removido*****\n')
                else:
                    print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
            else:
                print("(Digite 0 para cancelar.)")
                codigo_excluir = int(input("Digite o código do cadastro que deseja excluir: "))
                if cancelar_operacao(codigo_excluir):
                    return None

                encontrado = False
                for cadastro in dados_lidos:
                    if cadastro.get('codigo') == codigo_excluir: #Pega o código do registro que deseja excluir
                        dados_lidos.remove(cadastro) #Remove o registro da lista
                        print(f'\n*****Cadastro removido*****\n')
                        escrever_arquivo_json(lista, dados_lidos)
                        encontrado = True
                        
                if not encontrado:
                    print("\n-----CADASTRO NÃO ENCONTRADO.-----\n")
                    return None
                
            if input("Deseja remover mais cadastros?(s/n): ") == 'n':
                return None
        except:
            print("\nDigite um dado válido.\n")

while True: #Faz a navegação contínua.
    
    display_main_menu()
    try:
        opcao = int(input("\nInforme a opção desejada :"))
    except:
        print("Digite uma opção válida.")
        continue
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
                try:
                    select = int(input("\nInforme a ação desejada: ")) 
                except:
                    print("Digite um dado válido.")
                    continue

                if select < 1 or select > 5: #Valída a escolha do usuário.
                    print("\n-----Insira uma ação válida.-----\n")
                    continue

                elif select == 1: #Filtra a escolha do usuário
                    
                    display_cabecalho(select, n) #Menu de adicionar cadastros
                    if lista_atual == 'aluno' or lista_atual == 'professor':
                        add_pessoas_na_lista(lista_atual)

                    else:
                        add_registro_na_lista(lista_atual)

                elif select == 2:
                    display_cabecalho(select, n) #Menu de listagem

                    show_lista(lista_atual)

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