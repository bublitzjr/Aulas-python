class Paciente:

    def __init__(self, documentos: dict, receita: dict):
        self.nome = documentos["nome"]
        self.cpf = documentos["cpf"]
        self.documento = dict(nome=documentos["nome"], cpf=documentos["cpf"])
        self.receita = dict(nome=receita["nome"], cpf=receita["cpf"],
                            nome_medicamento=receita["nome_medicamento"],
                            quantidade_medicamento=receita["quantidade_medicamento"], validade=receita["validade"])
