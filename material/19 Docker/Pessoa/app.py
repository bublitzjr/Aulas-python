from flask import Flask, request
from datetime import date
from DataBase import db
import MySQLdb
import pandas as pd


app = Flask(__name__)


@app.route("/consultar_cpf/", methods=["POST"])
@app.route("/consultar_cpf/<cpf>")
def consultar_divida(cpf=None):
    # Verifica se o cpf foi informado e é válido:
    if not cpf:
        return "Error: CPF não informado!", 400
    elif not len(str(cpf)) == 11:
        return "Error: CPF inválido!", 400

    # Data de nascimento mínima para que a pessoa tenha 18 anos:
    data_minima = date((date.today().year - 18), date.today().month, date.today().day)

    # Monta o sql da consulta:
    sql = f"SELECT cpf, nome, score, divida FROM pessoa WHERE cpf = '{str(cpf)}' AND data_nascimento <= '{data_minima}'"
    # sql = "SELECT  FROM pessoa WHERE cpf = '98465715652' and data_nascimento <= '2003-04-28'"

    try:
        result_rows = db.cursor.execute(sql)
        if result_rows > 0:
            columns = [i[0] for i in db.cursor.description]  # Separa o nome das colunas.
            df = pd.DataFrame(db.cursor.fetchall(), columns=columns)  # Prepara o DataFrame.
            return df.to_json(orient="records")  # Transforma o DataFrame em json e retorna.
    except MySQLdb.OperationalError as op_error:
        print("Error: " + op_error.args[1])
        return "Error: Server error! Please contact support.", 500
    except MySQLdb.ProgrammingError as prog_error:
        print("Error: " + prog_error.args[1])
        return "Error: Server error! Please contact support.", 500

    return "Message: É necessário ter mais que 18 para utilizar esse recurso!", 200