from flask import Flask, request
from produto import Produto

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return("API para crud de produtos em uma base de dados do MongoDB")


@app.route("/ler", methods=['GET'])
def ler_todos():
    pr = Produto()
    data = pr.read()
    return data

@app.route("/novo", methods=['POST'])
def cadastrar():
    data = request.json
    pr = Produto()
    pr.save(data)
    return 'Produto cadastrado'

@app.route("/editar/<nome>", methods=['PUT'])
def editar(nome):
    data = request.json
    pr = Produto()
    pr.update(nome, data)
    return 'Produto editado'

@app.route("/deletar/<nome>", methods=['DELETE'])
def deletar(nome):
    pr = Produto()
    pr.remove(nome)
    return 'Produto deletado'


if __name__ == "__main__":
    app.run()
