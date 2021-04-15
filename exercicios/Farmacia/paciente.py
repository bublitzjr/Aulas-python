class Paciente:

    def __init__(self, documento: dict, receita: dict):
        self.receita = receita
        self.documento = documento
