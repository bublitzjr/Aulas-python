from flask import Flask, request, render_template, redirect
from controllers import usuarios

import json

app = Flask(__name__)

@app.route("/listar_usuarios", methods=['GET'])
@app.route("/listar_usuarios/<string:cpf>", methods=['GET'])
def listar_usuarios(cpf=None):    
    return usuarios.listar_usuario(cpf)

@app.route("/limpar_usuarios", methods=['DELETE'])
def limpar_usuarios():    
    return usuarios.limpar_usuarios()

@app.route("/cadastrar_usuarios", methods=['POST'])
def cadastrar_usuarios():    
    raw_request = request.data.decode("utf-8")
    dados = json.loads(raw_request)
    return usuarios.cadastrar_usuarios(dados)

@app.route("/atualizar_usuarios", methods=['PUT'])
def atualizar_usuarios():
    raw_request = request.data.decode("utf-8")
    dados = json.loads(raw_request)    
    return usuarios.atualizar_usuarios(dados)    

@app.route("/deletar_usuarios", methods=['DELETE'])
def deletar_usuarios():
    raw_request = request.data.decode("utf-8")
    dados = json.loads(raw_request)
    return usuarios.deletar_usuarios(dados)

if __name__ == "__main__":
    app.run(debug=True)