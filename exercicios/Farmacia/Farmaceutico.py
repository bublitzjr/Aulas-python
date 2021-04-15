import datetime

class Farmaceutico():

    def receber_receita(self, dados_receita: dict):
        dados_receita = dict(nome=dados_receita['nome'],
                             validade=dados_receita['validade'],
                             quantidade=dados_receita['quantidade'],
                             paciente=dados_receita['paciente'])

        result = Farmaceutico().validar_receita(dados_receita)

        if result == True:
            self.entregar_medicamento(dados_receita['nome'], dados_receita['quantidade'], dados_receita['paciente'])

    def entregar_medicamento(self, medicamento, quantidade, paciente):
        print(f"\n{'Descrição':=^30}")
        print("Medicamento: " + medicamento)
        print("Quantidade: " + str(quantidade))
        print("Paciente: " + paciente)
        print("Status solicitação: Aprovado ")
        print(f"{'':=^30}")

    def validar_receita(self, dados_receita: dict):
        dados_requisicao = dict(nome=dados_receita['nome'],
                                validade=dados_receita['validade'],
                                quantidade=dados_receita['quantidade'],
                                paciente=dados_receita['paciente'])
        possui_estoque = self.verificar_estoque(dados_requisicao['nome'], dados_requisicao['quantidade'])
        cliente_valido = self.verificar_cliente(dados_requisicao['paciente'])

        if not possui_estoque:
            raise Exception("Não possui medicamento em estoque !")
            return False

        if datetime.datetime.strptime(dados_requisicao['validade'], "%m/%Y") <= datetime.datetime.today():
            raise Exception("Data de validade inválida")
            return False

        if not cliente_valido:
            raise Exception("Cliente inválido !")
            return False

        return True

    def verificar_cliente(self, paciente):
        with open("ArquivosTXT/paciente.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.split(";")
            if paciente == line[1].strip():
                return True
        return False

    def listar_estoque(self):
        with open("ArquivosTXT/medicamentos.txt", "r") as file:
            lines = file.readlines()

        print(f"\n{' ESTOQUE ':=^50}")
        print(f"{'Código':<4}\t{' Descrição ':<20}\t{'Quantidade':<4}")
        print(f"{'':-^50}")
        for line in lines:
            line = line.strip().split(";")
            print(f"{line[0]:<4}\t{line[1]:<20}\t{line[2]:<4}")
        print(f"{'':=^50}")

    def verificar_estoque(self, medicamento, quantidade):
        with open("ArquivosTXT/medicamentos.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.split(";")
            if medicamento == line[1] or medicamento == line[0]:
                if quantidade < int(line[2]):
                     self.retirar_estoque(medicamento, quantidade)
                     return True
        return False

    def retirar_estoque(self, medicamento, quantidade):
        with open("ArquivosTXT/medicamentos.txt", "r") as file:
            lines = file.readlines()

        with open("ArquivosTXT/medicamentos.txt", "w") as file:
            for i in range(len(lines)):
                line = lines[i].split(";")
                if medicamento == line[1]:
                    qtd_atualizada = int(line[2]) - quantidade
                    line[2] = str(qtd_atualizada) + "\n"
                    lines[i] = ";".join(line)
            file.write("".join(lines))