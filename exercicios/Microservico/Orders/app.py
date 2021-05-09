from flask import Flask, request, render_template, redirect
from controllers import orders

import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listar_pedidos", methods=['GET'])
@app.route("/listar_pedidos/<int:id>", methods=['GET'])
def listar_pedidos(id=None):    
    pedidos = eval(orders.listar_pedidos(id))
    return render_template("listar_pedidos.html", pedidos=pedidos)

@app.route("/deletar_pedidos", methods=['DELETE'])
def limpar_pedidos():
    return orders.limpar_pedidos()

@app.route("/deletar_pedidos/<int:id>", methods=['DELETE'])
def deletar_pedidos(id=None):
    return orders.deletar_pedidos(id)

@app.route("/atualizar_pedido/<int:id>", methods=['PUT'])
def atualizar_pedido(id=None):    
    raw_request = request.data.decode("utf-8")
    dados = json.loads(raw_request)
    dados['id'] = id
    return orders.atualizar_pedidos(dados)

@app.route("/cadastrar_pedidos", methods=['POST'])
def cadastrar_pedidos():    
    raw_request = request.data.decode("utf-8")
    dados = json.loads(raw_request)
    return orders.cadastrar_pedidos(dados)


if __name__ == "__main__":
    app.run(debug=True)