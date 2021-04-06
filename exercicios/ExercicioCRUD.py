menu = 0
lista = {}

def cadastrar(nome, idade, cpf):
    try:
        lista[cpf] = dict(nome=nome, idade=idade)
        return lista
    except:
        raise Exception("Erro ao cadastrar !")

def buscar(cpf):
    try:
        return(lista[cpf])
    except:
        raise Exception("CPF não encontrado !")

def deletar(cpf):
    try:
        del lista[cpf]
        print("Apagado com sucesso !")
    except:
        raise Exception("Não foi possível excluir !")

def alterar(nome, idade, cpf):
    try:
        lista[cpf] = dict(nome=nome, idade=idade)
        return lista
    except:
        raise Exception("Erro ao alterar !")

#//////////////////////////////////////////////////////////////////////////

while menu != "0":
    menu = input("1 - Cadastro: \n"
                 "2 - Listar: \n"
                 "3 - Pesquisar: \n"
                 "4 - Excluir: \n"
                 "5 - Alterar: \n")

    if menu == "1":
        nome  = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        cpf   = input("Digite seu cpf: ")
        lista = cadastrar(nome, idade, cpf)
    elif menu == "2":
        print(lista.items())
    elif menu == "3":
        cpf = input("CPF da pessoa para consulta : ")
        print(buscar(cpf))
    elif menu == "4":
        cpf = input("CPF da pessoas para exclusão: ")
        print(deletar(cpf))
    elif menu == "5":
        cpf = input("CPF da pessoa que deseja alterar: ")
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        print(alterar(nome, idade, cpf))
    else:
        break