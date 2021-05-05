from datetime import date
import MySQLdb

from flask import Flask, request

from DataBase import db

app = Flask(__name__)


@app.route("/pagar_divida", methods=['PUT'])
def pagar_divida():
    # Pega o body request e armazena num dicionário:
    body_request = request.get_json()

    # Verifica o body request:
    if list(body_request.keys()).sort() != ['cpf', 'valor'].sort():
        return "Error: invalid body request!", 400

    # Pega a data de nascimento mínima para que a pessoa tenha 18 anos:
    data_minima = date((date.today().year - 18), date.today().month, date.today().day)

    cpf = str(body_request['cpf'])
    valor = body_request['valor']

    # Monta o SQL para fazer o update:
    sql = f"UPDATE pessoa SET divida = 0.00, score = 1000 WHERE cpf = '{cpf}' AND " \
          f"divida = CAST({valor} AS DECIMAL(65,2)) AND data_nascimento <= '{data_minima}'"

    try:
        result_rows = db.cursor.execute(sql)
        if result_rows > 0:
            return "Message: Dívida paga com sucesso!", 200
    except MySQLdb.OperationalError as op_error:
        print("Error: " + op_error.args[1])
        return "Error: Server error! Please contact support.", 500
    except MySQLdb.ProgrammingError as prog_error:
        print("Error: " + prog_error.args[1])
        return "Error: Server error! Please contact support.", 500

    return "Message: Erro ao pagar dívida!\nVerifique os dados informados.   ", 200
