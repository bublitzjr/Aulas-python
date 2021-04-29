from conexao.conexaoMongo import db
from bson.objectid import ObjectId

class Alunos:
    
    def __init__(self, matricula="", nome="", data_nasc=""):
        self.matricula = matricula
        self.nome = nome
        self.data_nasc = data_nasc
        self.alunos = db["alunos"]
        self.prova = db["prova"]
        
    def convert_to_json(self, data):
        df = pd.DataFrame(data)
        df = df.astype(str) # _id salvo como objeto no banco
        json = df.to_json(orient="records")
        return json

    def cadastrar_alunos(self, dados_aluno: dict):                                          
        self.alunos.insert_one(dados_aluno)

    def listar_alunos(self, codigo_aluno=None):
        cursor = self.alunos.find({}, {'_id':0, 'Matricula':1, 'Nome':1})

        if codigo_aluno:
            cursor = self.alunos.find({'Matricula': codigo_aluno}, {'_id':0, 'Matricula':1, 'Nome':1})

        result = self.convert_to_json(cursor)
        return result
            
    def solicitar_prova(self, codigo_prova):               
        cursor = self.prova.find_one({'_id':ObjectId(codigo_prova)}, {"_id":0})
        for numero_questao in cursor["Questoes"]:
            del cursor["Questoes"][numero_questao]["Resposta correta"]    
            
        return cursor
        
    def responder_prova(self, dados_aluno_prova):
        gabarito = list(self.pegar_gabarito("608ae084eff16fd43049bb61"))
        
        print(gabarito)
        # for key, value in gabarito['Questoes'].items():
        #     print(key, value)
            
        # for key, value in dados_aluno_prova.items():
        #     print(key, value)

    def pegar_gabarito(self, codigo_prova):
        cursor = self.prova.find_one({'_id':ObjectId(codigo_prova)}, {"_id":0})              
        for numero_questao in cursor["Questoes"]:
            del cursor["Questoes"][numero_questao]["Peso"]    
            del cursor["Questoes"][numero_questao]["Alternativas"]    
        return cursor
