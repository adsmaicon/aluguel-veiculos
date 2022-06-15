from src.entities.veiculo import Veiculo


class Caminhao(Veiculo):

    def __init__(self, id: str, placa: str, km: float, carga: float):
        super().__init__(id, placa, km)
        self.__carga = carga

    @property
    def carga(self) -> float:
        return self.__carga
