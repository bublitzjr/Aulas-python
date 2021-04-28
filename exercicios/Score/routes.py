from flask import Flask, request, render_template, redirect
from conexao.conexaoBD import cursor

import pandas as pd
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():    
    return f"<h1>Bem vindo !</h1>"

@app.route("/requisitar_pessoa", methods=["GET"])
@app.route("/requisitar_pessoa/<string:cpf>", methods=["GET"])
def requisitar_pessoa(cpf=None):

    try:
        sql =  f"""
                SELECT t.nome_pessoa, t.CPF, t.score, t.divida from (
                    SELECT	
                        a.data_nasc,
                        TIMESTAMPDIFF(YEAR, a.data_nasc, current_date) as Anos,
                        TIMESTAMPDIFF(MONTH, a.data_nasc + INTERVAL TIMESTAMPDIFF(YEAR,  a.data_nasc, current_date) YEAR , current_date) AS Mes,
                        TIMESTAMPDIFF(DAY, a.data_nasc + INTERVAL TIMESTAMPDIFF(MONTH,  a.data_nasc, current_date) MONTH , current_date) AS Dias,
                        a.nome_pessoa as nome_pessoa,
                        a.score as score,
                        a.divida as divida,
                        a.cpf as CPF
                    FROM pessoa a) as t
                WHERE t.Anos >= 18
                """      
        if cpf:
            sql += f" AND t.cpf = {cpf}"

        affected_rows = cursor.execute(sql)

        if affected_rows > 0:
            columns = [i[0] for i in cursor.description]  # Importando todos
            df = pd.DataFrame(cursor.fetchall(), columns=columns)
            json = df.to_json(orient="records")        

            return json
        
    except Exception as error:
        return dict(Status=400, Text=error.args)                    

    return dict(Status=400, Text="Falha")                        


@app.route("/pagar_divida/<cpf>", methods=["PUT"])
def pagar_divida(cpf=None):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    divida_atual = 0  

    sql = f"""SELECT divida FROM pessoa WHERE CPF = {cpf}"""
    affected_rows = cursor.execute(sql)    

    try:        
        if affected_rows > 0:
              
            for i in cursor.fetchall():
                divida_atual = i[0]     

            if divida_atual == dict_values['divida']:            
                sql = f"""UPDATE pessoa SET
                        divida = 0,
                        score = 1000
                        WHERE CPF = '{cpf}'"""
                affected_rows = cursor.execute(sql)
                
                if affected_rows > 0:
                    return "Divida quitada!"

            return "Seu score já é 1000 !"

        return "Não foi encontrado essa pessoa !"

    except Exception as error:
        return str(error.args)

if __name__ == "__main__":
    app.run(debug=True)