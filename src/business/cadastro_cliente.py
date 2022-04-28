from xml.dom.minidom import Entity
from .cadastro_abstract import CadastroAbtract


class CadastroCliente(CadastroAbtract):

    def inserir(self, entitie: Entity):
        pass

    def consultar(self, id) -> Entity:
        pass

    def remover(self, entitie) -> Entity:
        pass

    def listar_todos() -> list(Entity):
        pass
