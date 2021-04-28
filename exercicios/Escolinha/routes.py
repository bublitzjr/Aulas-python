from alunos import Alunos
from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():    
    return f"<h1>Bem vindo !</h1>"

@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)
    
    try:
        Alunos.cadastrar_alunos(dict_values) 
        return "sucesso"       
    except Exception as error:
        return str(error)

if __name__ == "__main__":
    app.run(debug=True)