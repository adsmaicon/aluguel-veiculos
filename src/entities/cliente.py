from src.entities.entity import Entity


class Cliente(Entity):

    def __init__(self, id: str, endereco: str, telefone: str):
        super().__init__(id)
        self.__endereco: str = endereco
        self.__telefone: str = telefone

    @property
    def endereco(self) -> str:
        return self.__endereco

    @property
    def telefone(self) -> str:
        return self.__telefone
