from .config_db import Conexao_bd as db

import datetime
import pandas as pd
import json

def consultar(cpf):
    sql = "SELECT * FROM orders"

    if cpf:    
        sql = f"SELECT * FROM orders WHERE id_user = '{id_user}'"
        
    affected_rows = db.cursor.execute(sql)

    if affected_rows > 0:
        columns = [i[0] for i in db.cursor.description]  # Importando todos
        df = pd.DataFrame(db.cursor.fetchall(), columns=columns)
        json = df.to_json(orient="records")        

        return json
    else:
        raise Exception("Registro não existe")
    
        