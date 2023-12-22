from Software_cuotas_gimnasio.Pase_strategy.pase_strategy import Pase_strategy
class Pase_regular(Pase_strategy):
    def __init__(self) -> None:
        super().__init__()
    
    def calcular_cuota(self, socio, promocion):
        return 1000