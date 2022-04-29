from src.business.cadastro_abstract import CadastroAbtract
from src.entities.entity import Entity


class CadastroVeiculo(CadastroAbtract):
    
    def inserir(self, entity: Entity):
        pass

    def consultar(self, id) -> Entity:
        pass

    def remover(self, entity) -> Entity:
        pass

    def listar_todos() -> list(Entity):
        pass
