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

@app.route("/mdb_editar/<int:id>", methods=['PUT'])
def put(id):
    data = request.json
    pr = Produto()
    pr.update(id, data)
    return 'Produto editado'

@app.route("/mdb_deletar/<int:id>", methods=['DELETE'])
def delete(id):
    pr = Produto()
    pr.remove()
    return 'Produto deletado'


if __name__ == "__main__":
    app.run()
