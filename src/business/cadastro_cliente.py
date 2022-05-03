from typing import List
from src.entities.cliente import Cliente
from .cadastro_abstract import CadastroAbtract



class CadastroCliente(CadastroAbtract):

    def __init__(self) -> None:
        super().__init__()
        self.__clientes: List[Cliente] = []

    def inserir(self, cliente: Cliente):
        self.__clientes.append(cliente)
        print(f'inserido {cliente.id}')

    def consultar(self, id) -> Cliente:
        cliente = list(filter(lambda x: x.id == id, self.__clientes))
        print(f'consultado {cliente[0].nome}')

    def remover_por_id(self, id: str) -> Cliente:
        print('removido')

    def remover_por_entidade(self, cliente: Cliente) -> Cliente:
        print('removido')

    def listar_todos() -> List[Cliente]:
        print('listado')
