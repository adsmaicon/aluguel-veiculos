from typing import List
import mysql
from src.business.cadastro_abstract import CadastroAbtract
from src.entities.veiculo import Veiculo


class CadastroVeiculo(CadastroAbtract):

    def __init__(self) -> None:
        self.__veiculos: List[Veiculo] = []

    def inserir(self, veiculo: Veiculo):
        cnx = mysql.connector.connect(user='maicon', password='123456',
                                      host='127.0.0.1',
                                      database='aluguel')
        cursor = cnx.cursor()
        adiciona_cliente = (
            """INSERT INTO veiculo
            (placa, km, carga, bagageiro, portas, tipo) 
            VALUES ( %(placa)s, %(km)s, %(carga)s, %(bagageiro)s, %(portas)s, %(tipo)s)"""
        )
        dados = {
            "placa": veiculo.placa,
            "km": veiculo.km,
            "carga": veiculo.carga if hasattr(veiculo, "carga") else '',
            "bagageiro": veiculo.bagageiro if hasattr(veiculo, "bagageiro") else None,
            "portas": veiculo.portas if hasattr(veiculo, "portas") else None,
            "tipo": 'automovel' if hasattr(veiculo, "bagageiro") else 'caminhao'
        }
        cursor.execute(adiciona_cliente, dados)
        cnx.commit()
        cursor.close()
        cnx.close()

    def consultar(self, id: str) -> Veiculo:
        veiculo = list(filter(lambda x: x.id == id, self.__veiculos))
        return veiculo[0]

    def remover_por_id(self, id: str) -> None:
        veiculo = self.consultar(id)
        self.__veiculos.remove(veiculo)

    def remover_por_entidade(self, veiculo: Veiculo) -> None:
        self.__veiculos.remove(veiculo)

    def listar_todos(self) -> List[Veiculo]:
        return self.__veiculos
