from .config_db import Conexao_bd as db

import datetime
import pandas as pd
import json

def persistir_dados(sql):
    affected_rows = db.cursor.execute(sql)

    if affected_rows > 0:
        return dict(Status=200, Text="Ação realizada com sucesso")    
    raise Exception("Não foi possível realizar a ação")        

def atualizar(dados):
    sql = f"""UPDATE users SET 
              Name = '{dados['Name']}', 
              Email = '{dados['Email']}', 
              Phone_number = '{dados['Phone_number']}', 
              Updated_at = '{str(datetime.date.today())}' 
              WHERE CPF = '{dados['CPF']}'"""

    return persistir_dados(sql)

def cadastrar(dados):    
    sql = f"""INSERT INTO users 
            (Name, CPF, Email, Phone_number, Created_at) 
            VALUES 
            ('{dados['Name']}', '{dados['CPF']}', '{dados['Email']}', '{dados['Phone_number']}', '{str(datetime.date.today())}')"""   

    return persistir_dados(sql) 

def deletar(dados):    
    sql = f"DELETE FROM users WHERE CPF = '{dados['CPF']}'"
    return persistir_dados(sql)     

def limpar():
    sql = "DELETE FROM users"
    return persistir_dados(sql)

def consultar(cpf):
    sql = "SELECT * FROM users"

    if cpf:    
        sql = f"SELECT * FROM users WHERE CPF = '{cpf}'"
        
    affected_rows = db.cursor.execute(sql)

    if affected_rows > 0:
        columns = [i[0] for i in db.cursor.description]  # Importando todos
        df = pd.DataFrame(db.cursor.fetchall(), columns=columns)
        json = df.to_json(orient="records")        

        return json
    else:
        raise Exception("Usuário não existe")
    
        