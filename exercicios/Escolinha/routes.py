from classes.alunos import Alunos
from classes.prova import Prova
from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():    
    return f"<h1>Bem vindo !</h1>"

# CLASSE ALUNOS
@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)
    
    try:
        Alunos().cadastrar_alunos(dict_values) 
        return "sucesso"       
    except Exception as error:
        return str(error)

@app.route("/listar_alunos", methods=["GET"])
@app.route("/listar_alunos/<int:codigo_aluno>", methods=["GET"])
def listar_alunos(codigo_aluno=None):
    try:
        return Alunos().listar_alunos(codigo_aluno)
    except Exception as error:
        return str(error)

@app.route("/solicitar_prova/<string:codigo_prova>", methods=["GET"])
def solicitar_prova(codigo_prova=None):
    try:
        return Alunos().solicitar_prova(codigo_prova)
    except Exception as error:
        return str(error)

@app.route("/responder_prova/<string:codigo_prova>", methods=["POST"])
def responder_prova(codigo_prova=None):    
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)
    dict_values['codigo_prova'] = codigo_prova
    
    return Alunos().responder_prova(dict_values)        
    try:
        pass
    except Exception as error:
        return str(error)

# CLASSE PROVAS
@app.route("/cadastrar_provas", methods=["POST"])
def cadastrar_provas():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        Prova().cadastrar_provas(dict_values) 
        return "sucesso"       
    except Exception as error:
        return str(error)

@app.route("/listar_provas", methods=["GET"])
@app.route("/listar_provas/<string:codigo_prova>", methods=["GET"])
def listar_provas(codigo_prova=None):    
    try:
       return Prova().listar_provas(codigo_prova)           
    except Exception as error:
        return str(error)

if __name__ == "__main__":
    app.run(debug=True)