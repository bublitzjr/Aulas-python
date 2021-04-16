from MetodosCRUD import Pessoas

menu = 99

while menu != 0:
    print(f"\n{' MENU ':=^30}")
    print("1 - Cadastrar pessoa\n"
          "2 - Listar todos\n"
          "3 - Pesquisar pessoas\n"
          "4 - Deletar pessoas\n"
          "5 - Limpar todos\n"
          "6 - Atualizar pessoa\n"
          "0 - SAIR")
    print(f"{'':=^30}")
    print("Digite:")
    menu = int(input())


    if menu == 1:
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        idade = input("Digite a idade4: ")
        altura = input("Digite a altura: ")

        pessoa = Pessoas(nome, cpf, idade, altura)
        try:
            pessoa.inserir_pessoa()
        except Exception as e:
            print("Erro ao cadastrar: " + str(e))

    elif menu == 2:
        try:
            Pessoas().listar_todos()
        except Exception as e:
            print("Erro ao listar todos: " + str(e))

    elif menu == 3:
        nome = input("Digite o nome da pessoa: ")

        try:
            Pessoas().pesquisar_pessoa(nome)
        except Exception as e:
            print("Erro ao pesquisar pessoa: " + str(e))

    elif menu == 4:
        cpf = input("Digite o cpf da pessoa: ")

        try:
            Pessoas().deleter_pessoa(cpf)
            print("Deletado com sucesso !")
        except Exception as e:
            print("Erro ao deletar pessoa: " + str(e))

    elif menu == 5:
        try:
            Pessoas().deletar_todos()
            print("Limpo com sucesso !")
        except Exception as e:
            print("Erro ao limpar todos: " + str(e))

    elif menu == 6:
        id = input("Digite o id do usuário: ")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        idade = input("Digite a idade: ")
        altura = input("Digite a altura: ")

        try:
            Pessoas().atualizar_dados_pessoa(id, dict(nome=nome, cpf=cpf, idade=idade, altura=altura))
        except Exception as e:
            print("Erro ao alterar pessoa: " + str(e))
    else:
        print("Opção Inválida !")

