from .config_db import Conexao_bd as db
from Orders.security.criptografia import *

import datetime
import pandas as pd
import json

def persistir_dados(sql):
    affected_rows = db.cursor.execute(sql)
    print(affected_rows)
    if affected_rows > 0:
        return dict(Status=200, Text="Ação realizada com sucesso")
    raise Exception("Não foi possível realizar a ação")        


def consultar(id):
    sql = "SELECT * FROM orders"

    if id:    
        sql = f"SELECT * FROM orders WHERE id_user = '{id}'"
        
    affected_rows = db.cursor.execute(sql)

    if affected_rows > 0:
        columns = [i[0] for i in db.cursor.description]  # Importando todos
        df = pd.DataFrame(db.cursor.fetchall(), columns=columns)
        json = df.to_json(orient="records")        

        return json
    else:
        raise Exception("Registro não existe")

def cadastrar(dados):

    sql = f"""INSERT INTO orders 
            (id_user, item_description, item_quantity, item_price, total_value, created_at) 
            VALUES 
            ('{dados['id_user']}', '{dados['item_description']}', {dados['item_quantity']}, {dados['item_price']}, {dados['total_value']}, '{str(datetime.date.today())}')"""   

    return persistir_dados(sql) 


def atualizar(dados):
    total = dados['item_quantity'] * dados['item_price']

    sql = f"""UPDATE orders SET 
              id_user = {dados['id_user']}, 
              item_description = '{dados['item_description']}', 
              item_quantity = {dados['item_quantity']}, 
              item_price = {dados['item_price']},
              total_value = {total}
              WHERE id = '{dados['id']}'"""

    return persistir_dados(sql)

def deletar(id):
    sql = f"DELETE FROM orders WHERE id = {id}"
    return persistir_dados(sql)     

def limpar():
    sql = f"DELETE FROM orders"
    return persistir_dados(sql)     
    