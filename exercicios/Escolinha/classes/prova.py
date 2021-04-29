from conexao.conexaoMongo import db

import pandas as pd
import json
from bson.objectid import ObjectId

class Prova():

    def __init__(self):           
        self.prova = db["prova"]
        self.alunos = db["alunos"]

    def convert_to_json(self, data):
        df = pd.DataFrame(data)
        df = df.astype(str) # _id salvo como objeto no banco
        json = df.to_json(orient="records")
        return json

    def cadastrar_provas(self, dados_prova):
        self.provas.insert_one(dados_prova)

    def listar_provas(self, codigo_prova=None):                               
        cursor = self.prova.find({}, {'_id':1, 'Nome':1})

        if codigo_prova:
            cursor = self.prova.find({'_id':ObjectId(codigo_prova)}, {"_id":1, 'Nome':1})          
 
        result = self.convert_to_json(cursor)
        return result
        




