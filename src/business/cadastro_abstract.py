from abc import ABC, abstractmethod
from src.entities.entity import Entity


class CadastroAbtract(ABC):

    @abstractmethod
    def inserir(self, entitie: Entity):
        pass

    @abstractmethod
    def consultar(self, id) -> Entity:
        pass

    @abstractmethod
    def remover(self, entitie) -> Entity:
        pass

    @abstractmethod
    def listar_todos() -> list(Entity):
        pass
