from .cliente import Cliente


class PessoaFisica(Cliente):

    def __init__(self, id: str, endereco: str, telefone: str, cpf: str):
        super().__init__(id, endereco, telefone)
        self.__cpf = cpf

    @property
    def cpf(self) -> str:
        return self.__cpf
