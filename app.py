from flask import Flask, request, jsonify
from produto import Produto

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return("API para crud de produtos em uma base de dados do MongoDB")


@app.route("/mdb_ler", methods=['GET'])
def get():
    pr = Produto()
    data = pr.read()
    return data

@app.route("/mdb_cadastrar", methods=['POST'])
def post():
    data = request.json
    pr = Produto()
    pr.save(data)
    return 'Produto cadastrado'

@app.route("/mdb_editar/<nome>", methods=['PUT'])
def put(nome):
    data = request.json
    pr = Produto()
    pr.update(nome, data)
    return 'Produto editado'

@app.route("/mdb_deletar/<nome>", methods=['DELETE'])
def delete(nome):
    pr = Produto()
    pr.remove(nome)
    return 'Produto deletado'


if __name__ == "__main__":
    app.run()
