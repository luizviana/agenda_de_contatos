AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print(">>>>> Agenda vazia")


def buscar_contato(contato):
    try:
        print("---------------------------------------------")
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["telefone"])
        print("Email:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
    except KeyError:
        print(">>>>> Contato inexistente")


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    salvar()
    print()
    print(">>>>> Contato {} adicionado/editado com sucesso.".format(contato))
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(">>>>> Contato {} deletado com sucesso.".format(contato))
        print()
    except KeyError:
        print(">>>>> Contato inexistente")
    except Exception as error:
        print(">>>>> Erro inesperado:", error)


def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(
                    contato, telefone, email, endereco))
        print(">>>>> Agenda exportada com sucesso.")
    except Exception as error:
        print(">>>>> Algum erro ocoreu:", error)


def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print(">>>>> O arquivo CSV não foi encontrado.")
    except Exception as error:
        print(">>>>> Algum erro ocorreu:", error)


def ler_detalhes_contato():
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    endereco = input("Digite o endereco: ")
    return telefone, email, endereco


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print(">>>>> Database carregado com sucesso.")
        print(">>>>> {} contatos carregados".format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> Arquivo nÃ£o encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)


def imprimir_menu():
    print("---------------------------------------------")
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Exportar contatos para CSV")
    print("7 - Importar contatos de um CSV")
    print("0 - Fechar agenda")
    print("---------------------------------------------")


# INICIO DO PROGRAMA
carregar()
while True:
    imprimir_menu()

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_contatos()
    elif opcao == "2":
        contato = input("Digite o nome do contato: ")
        buscar_contato(contato)
    elif opcao == "3":
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print(">>>>> Contato já existente")
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == "4":
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print(">>>>> Editando contato:", contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print("Contato inexistente")
    elif opcao == "5":
        contato = input("Digite o nome do contato: ")
        excluir_contato(contato)
    elif opcao == "6":
        nome_arquivo = input("Digite o nome do arquivo CSV a ser exportado: ")
        exportar_contatos(nome_arquivo)
    elif opcao == "7":
        nome_arquivo = input("Digite o nome do arquivo CSV a ser importado: ")
        importar_contatos(nome_arquivo)
    elif opcao == "0":
        print(">>>>> Saindo do programa...")
        break
    else:
        print(">>>>> Opção inválida.")
