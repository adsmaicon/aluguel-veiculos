from flask import Blueprint, request
from src.business.cadastro_veiculo import CadastroVeiculo
from src.entities.caminhao import Caminhao


veiculos = Blueprint('veiculos', __name__)


@veiculos.route("/veiculo", methods=["POST"])
def inserir_veiculo():
    dados = request.json

    caminhao = Caminhao(
        "",
        dados['placa'],
        dados['km'],
        dados['carga'])
        
    cadastro_veiculo = CadastroVeiculo()

    cadastro_veiculo.inserir(caminhao)

    return "sucesso", 201
