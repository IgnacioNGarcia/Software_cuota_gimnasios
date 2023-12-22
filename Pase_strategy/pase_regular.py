from Software_cuotas_gimnasio.Pase_strategy.pase_strategy import Pase_strategy
class Pase_regular(Pase_strategy):
    def __init__(self) -> None:
        super().__init__()
    
    def calcular_cuota(self, socio, promocion):
        precio = 0
        matches = 0
        
        for act in socio.get_actividades():
            if act in promocion.get_actividades():
                matches = matches + 1
            precio = precio + act.get_precio()
        
        if matches >= 2:
            precio = precio - (precio * (promocion.get_dcto() / 100))
        
        return precio