import json
from ast import literal_eval
from datetime import date
from .paciente import Paciente


class Farmaceutica:
    nome = "Gabriela Cristofolini"
    crf = 10847

    def receber_receita(self, receita: dict) -> None:
        self.receita_recebida = receita

    def validar_receita(self, documento_recebido: dict) -> bool:
        data_hoje = date.today().strftime("%d/%m/%Y")
        data_validade = date.strftime(self.receita_recebida["validade"], "%d/%m/%Y")

        if documento_recebido["cpf"] == self.receita_recebida["cpf"] \
                and data_validade >= data_hoje:
            return True
        else:
            return False

    def verificar_estoque(self, nome_medicamento: str):
        with open("Estoque.txt", "r") as file:
            read = file.read()
        estoque = literal_eval(read)
        index_estoque = list(estoque.keys())
        if nome_medicamento in index_estoque and \
                self.receita_recebida["quantidade_medicamento"] <= estoque[nome_medicamento]["quantidade"]:
            return True
        else:
            print("Produto não disponível no estoque.")
            return False

    def entregar_medicamento(self):

        print("\t\t\t\t\tComprovante de dispensação de medicamento\n\n", "\tNome paciente: ",
              self.receita_recebida["nome"], "\n",
              "\tMedicamento dispensado: ",
              self.receita_recebida["nome_medicamento"], "\n", "\tFarmacêutica responsável: ",
              self.nome, "\tCRF/SC: ", self.crf)

    def retirar_medicamento_estoque(self, nome: str):
        with open("Estoque.txt", "r") as file:
            read = file.read()

        estoque = literal_eval(read)
        estoque[nome]["quantidade"] -= self.receita_recebida["quantidade_medicamento"]

        file = open("Estoque.txt", "w")
        estoque_json = json.dumps(estoque, indent=2)
        file.write(estoque_json)
        file.close()

