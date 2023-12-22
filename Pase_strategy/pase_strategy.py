from abc import ABC, abstractmethod
class Pase_strategy(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def calcular_cuota(self,socio,promocion):
        pass