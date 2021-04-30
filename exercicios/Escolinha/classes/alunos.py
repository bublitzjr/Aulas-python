from conexao.conexaoMongo import db
from bson.objectid import ObjectId
import pandas as pd

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
        list_prova_aluno = []                       
        cod_prova = dados_aluno_prova['codigo_prova']
        
        for key in dados_aluno_prova["Questoes"]:
            list_prova_aluno.append(dados_aluno_prova["Questoes"][key])

        result = self.corrigir_prova(list_prova_aluno, cod_prova)

        return result

    def corrigir_prova(self, list_prova_aluno, cod_prova):
        list_gabarito = self.pegar_gabarito(cod_prova)                     
        lista_correcao = []
        dicionario_correcao = dict()
        soma_pesos = 0          
        
        for i in range(len(list_gabarito)):
            if list_gabarito[i][0] == list_prova_aluno[i]:                                                                
                soma_pesos += list_gabarito[i][1]                                                  
                dicionario_correcao['Correcao'] = dict(gabarito=list_gabarito[i][0], questao_aluno=list_prova_aluno[i])                
            else:
                dicionario_correcao['Correcao'] = dict(gabarito=list_gabarito[i][0], questao_aluno=list_prova_aluno[i])                

        dicionario_correcao['nota final'] = soma_pesos

        return dicionario_correcao

    def pegar_gabarito(self, codigo_prova):
        list_gabarito = []

        gabarito = self.prova.find_one({'_id':ObjectId(codigo_prova)}, {"_id":0})              
        for numero_questao in gabarito["Questoes"]:            
            del gabarito["Questoes"][numero_questao]["Alternativas"]    

        for key in gabarito['Questoes']:
            list_gabarito.append([gabarito["Questoes"][key]["Resposta correta"], gabarito["Questoes"][key]["Peso"]])        

        return list_gabarito

