from flask import Flask, jsonify, request
from src.business.cadastro_cliente import CadastroCliente
from src.entities.pessoa_fisica import PessoaFisica
from src.exceptions.cliente_not_found_error import ClienteNotFoundError

app = Flask(__name__)

cadastro_cliente = CadastroCliente()


@app.route("/cliente", methods=['POST'])
def inserir_cliente():
    dados = request.json

    cliente = PessoaFisica(
        dados['id'],
        dados['endereco'],
        dados['telefone'],
        dados['cpf'],
        dados['nome'])
    cadastro_cliente.inserir(cliente)

    return "ok", 201


@app.route("/cliente/<id>", methods=['DELETE'])
def delete_cliente(id):
    cadastro_cliente.remover_por_id(id)
    return "", 204


@app.route("/cliente")
def consultar_clientes():
    clientes = cadastro_cliente.listar_todos()

    resultado = list(map(lambda x: {
        "id": x.id,
        "endereco": x.endereco,
        "telefone": x.telefone,
        "cpf": x.cpf,
        "nome": x.nome},
        clientes))

    return jsonify(resultado)


@app.route("/cliente/<id>")
def consultar_cliente(id):
    try:
        cliente = cadastro_cliente.consultar(id)
    except ClienteNotFoundError:
        return "Not Found", 404

    resultado = {
        "id": cliente.id,
        "endereco": cliente.endereco,
        "telefone": cliente.telefone,
        "cpf": cliente.cpf,
        "nome": cliente.nome
    }

    return jsonify(resultado)
