from conexao.conexaoMongo import db

class Alunos:
    
    def __init__(self, matricula="", nome="", data_nasc=""):
        self.matricula = matricula
        self.nome = nome
        self.data_nasc = data_nasc
        self.alunos = db["alunos"]

    def cadastrar_alunos(self, dados_aluno: dict):                          
        self.alunos.insert_one(dados_aluno)
            
        