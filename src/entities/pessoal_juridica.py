from .cliente import Cliente


class PessoaFisica(Cliente):

    def __init__(self, id: str, endereco: str, telefone: str, cnpj: str):
        super().__init__(id, endereco, telefone)
        self.__cnpj = cnpj

    @property
    def cnpj(self) -> str:
        return self.__cnpj
