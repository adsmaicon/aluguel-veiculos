from flask import Blueprint
from flask import jsonify, request, Response
from src.business.cadastro_cliente import CadastroCliente
from src.entities.pessoa_fisica import PessoaFisica
from src.exceptions.cliente_not_found_error import ClienteNotFoundError

clientes = Blueprint('clientes', __name__)

cadastro_cliente = CadastroCliente()


@clientes.route("/cliente", methods=['POST'])
def inserir_cliente():
    dados = request.json

    cliente = PessoaFisica(
        None,
        dados['endereco'],
        dados['telefone'],
        dados['cpf'],
        dados['nome'])
    cadastro_cliente.inserir(cliente)

    return Response("ok", 201, {"x-codigos": "python"})


@clientes.route("/cliente/<id>", methods=['DELETE'])
def delete_cliente(id):
    cadastro_cliente.remover_por_id(id)
    return "", 204


@clientes.route("/cliente")
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


@clientes.route("/cliente/<id>")
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
