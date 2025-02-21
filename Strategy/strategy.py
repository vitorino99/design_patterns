from abc import ABC, abstractmethod


class VeiculoIPVAStrategy(ABC):
    @abstractmethod
    def calcular_valor(self, preco: float) -> float:
        pass

class CarroIPVA(VeiculoIPVAStrategy):
    def calcular_valor(self, preco: float) -> float:
        return preco * 0.03  

class MotoIPVA(VeiculoIPVAStrategy):
    def calcular_valor(self, preco: float) -> float:
        return preco * 0.02 

class CaminhaoIPVA(VeiculoIPVAStrategy):
    def calcular_valor(self, preco: float) -> float:
        return preco * 0.04 


class Veiculo:
    def __init__(self, preco: float, estrategia: VeiculoIPVAStrategy):
        self.preco = preco
        self.estrategia = estrategia 

    def calcular_ipva(self) -> float:
        return self.estrategia.calcular_valor(self.preco)
