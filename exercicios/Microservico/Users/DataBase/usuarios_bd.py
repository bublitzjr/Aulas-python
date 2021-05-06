from .config_db import Conexao_bd as db
from security.criptografia import *

import datetime
import pandas as pd
import json

def persistir_dados(sql):
    affected_rows = db.cursor.execute(sql)

    if affected_rows > 0:
        return dict(Status=200, Text="Ação realizada com sucesso")    
    raise Exception("Não foi possível realizar a ação")        

def atualizar(dados):
    email = codificar_dado(dados['Email'])
    phone = codificar_dado(dados['Phone_number'])
    cpf   = codificar_dado(dados['CPF'])

    sql = f"""UPDATE users SET 
              Name = '{dados['Name']}', 
              Email = 'email', 
              Phone_number = '{phone}', 
              Updated_at = '{str(datetime.date.today())}' 
              WHERE CPF = '{cpf}'"""

    return persistir_dados(sql)

def cadastrar(dados):    
    name  = dados['Name']
    cpf   = codificar_dado(dados['CPF'])
    email = codificar_dado(dados['Email'])
    phone = codificar_dado(dados['Phone_number'])

    sql = f"""INSERT INTO users 
            (Name, CPF, Email, Phone_number, Created_at) 
            VALUES 
            ('{name}', '{cpf}', '{email}', '{phone}', '{str(datetime.date.today())}')"""   

    return persistir_dados(sql) 

def deletar(dados):    
    cpf   = codificar_dado(dados['CPF'])

    sql = f"DELETE FROM users WHERE CPF = '{cpf}'"
    return persistir_dados(sql)     

def limpar():
    sql = "DELETE FROM users"
    return persistir_dados(sql)

def consultar(cpf):
    sql = "SELECT * FROM users"

    if cpf:    
        sql = f"SELECT * FROM users WHERE CPF = '{codificar_dado(cpf)}'"
        
    affected_rows = db.cursor.execute(sql)

    if affected_rows > 0:
        columns = [i[0] for i in db.cursor.description]  # Importando todos
        df = pd.DataFrame(db.cursor.fetchall(), columns=columns)        
        
        for key, value in df.items():
            if key == "CPF":
                df['CPF'] = decodificar_dado(value.values[0])
            if key == "Email":
                df['Email'] = decodificar_dado(value.values[0])
            if key == "Phone_number":
                df['Phone_number'] = decodificar_dado(value.values[0])

        json = df.to_json(orient="records")                

        return json
    else:
        raise Exception("Usuário não existe")
    
        