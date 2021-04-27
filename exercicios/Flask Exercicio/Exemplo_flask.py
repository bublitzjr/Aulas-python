from flask import Flask, request, render_template
from conexao import cursor
import json
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    style = " style='text-align:center' "
    return f"<h1{style}>Hello world !</h1>"

@app.route("/cadastrar", methods=["POST"])
def cadastrar():    
    raw_request = request.data.decode("utf-8")
    dict_value = json.loads(raw_request)

    try:
        sql = f"INSERT INTO exemplotabela VALUES ('{dict_value['Nome']}',default , {dict_value['idade']})"
        affected_rows = cursor.execute(sql)

        if affected_rows > 0:
            return dict(Status=200, Text="Sucesso")            

    except Exception as e:
        return dict(Status=400, Text=e.args)                    

    return dict(Status=400, Text="Falha")                        

@app.route("/deletar", methods=["DELETE"])
@app.route("/deletar/<int:id>", methods=["DELETE"])
def delete(id=None):

    try:
        sql = f"DELETE FROM exemplotabela"  # Limpar tabela

        if id:
            sql += f" WHERE id = {id}"      # Limpar registro
        
        affected_rows = cursor.execute(sql)

        if affected_rows > 0:
            return dict(Status=200, Text="Sucesso")            

    except Exception as e:
        return dict(Status=400, Text=e.args)                    

    return dict(Status=400, Text="Falha")                        


@app.route("/buscar", methods=["GET"])
@app.route("/buscar/<int:id>", methods=["GET"])
def buscar(id=None):

    try:
        sql = "SELECT * FROM exemplotabela" 
        if id:
            sql += f" WHERE id = {id}"     
        
        affected_rows = cursor.execute(sql)

        if affected_rows > 0:
            columns = [i[0] for i in cursor.description]  # Importando todos
            df = pd.DataFrame(cursor.fetchall(), columns=columns)
            json = df.to_json(orient="records")        

            return json

    except Exception as e:
        return dict(Status=400, Text=e.args)                    
    
    return dict(Status=400, Text="Falha")                        

@app.route("/atualizar/<int:id>", methods=["PUT"])
def atualizar(id):
    raw_request = request.data.decode("utf-8")
    dict_value = json.loads(raw_request)
    
    try:
        sql = f"UPDATE exemplotabela SET Nome = '{dict_value['Nome']}', idade = {dict_value['idade']} WHERE id = {id}"        
        affected_rows = cursor.execute(sql)

        if affected_rows > 0:            
            return dict(Status=200, Text="Sucesso")            

    except Exception as e:
        return dict(Status=400, Text=e.args)                    
    
    return dict(Status=400, Text="Falha")                        

if __name__ == "__main__":
    app.run(debug=True)
