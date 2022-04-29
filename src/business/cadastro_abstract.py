from abc import ABC, abstractmethod
from src.entities.entity import Entity
from typing import List

class CadastroAbtract(ABC):

    @abstractmethod
    def inserir(self, entity: Entity):
        pass

    @abstractmethod
    def consultar(self, id: str) -> Entity:
        pass

    @abstractmethod
    def remover_por_id(self, id: str) -> Entity:
        pass

    @abstractmethod
    def remover_por_entidade(self, entity: Entity) -> Entity:
        pass

    @abstractmethod
    def listar_todos() -> List[Entity]:
        pass
