from typing import List
from src.entities.entity import Entity
from .cadastro_abstract import CadastroAbtract


class CadastroCliente(CadastroAbtract):

    def inserir(self, entity: Entity):
        print(f'inserido {entity.id}')

    def consultar(self, id) -> Entity:
        print('consultado')

    def remover_por_id(self, id: str) -> Entity:
        print('removido')

    def remover_por_entidade(self, entity) -> Entity:
        print('removido')

    def listar_todos() -> List[Entity]:
        print('listado')
