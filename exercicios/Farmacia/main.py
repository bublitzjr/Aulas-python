from Farmaceutico import Farmaceutico
from paciente import Paciente

print(f"\n{' MENU ':=^30}")
print(" 1 - Solicitando remédio\n"
      " 2 - Listar remédios\n"
      " 0 - Sair")
print(f"{'':=^30}")
menu = int(input("Digite uma opção: "))

farmaceutico = Farmaceutico()

if menu == 1:

    cpf         = input("Digite seu CPF: ")
    nome        = input("Digite seu nome: ")
    farmaceutico.listar_estoque()
    medicamento = input("Digite o medicamento: ")
    quantidade  = int(input("Digite a quantidade: "))
    validade    = input("Digite a validade: ")

    paciente = Paciente(dict(cpf=cpf,
                             nome=nome),
                        dict(nome=medicamento,
                             validade=validade,
                             quantidade=quantidade,
                             paciente=nome))
    try:
        farmaceutico.receber_receita(paciente.receita)
    except Exception as e:
        print("Erro: " + str(e))

elif menu == 2:
    farmaceutico.listar_estoque()