from typing import List
from src.entities.cliente import Cliente
from .cadastro_abstract import CadastroAbtract


class CadastroCliente(CadastroAbtract):

    def __init__(self) -> None:
        self.__clientes: List[Cliente] = []

    def inserir(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def consultar(self, id: str) -> Cliente:
        cliente = list(filter(lambda cliente: cliente.id == id, self.__clientes))
        return cliente[0]

    def remover_por_id(self, id: str) -> None:
        cliente = self.consultar(id)
        self.__clientes.remove(cliente)

    def remover_por_entidade(self, cliente: Cliente) -> None:
        self.__clientes.remove(cliente)

    def listar_todos(self) -> List[Cliente]:
        return self.__clientes
