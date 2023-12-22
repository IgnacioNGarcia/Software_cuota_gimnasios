from Software_cuotas_gimnasio.Promociones.promocion import Promocion
class Builder():
    def __init__(self) -> None:
        self.__promo = None
        
    def get_promo(self):
        return self.__promo
    def set_promo(self,p):
        self.__promo = p
    promo = property(get_promo,set_promo)
    
    def reset(self):
        promocion = Promocion()
        self.set_promo(promocion)
    
    def set_nombre(self,n):
        self.get_promo().set_nombre(n)
    
    def set_acts(self,a):
        self.get_promo().set_actividades(a)
    def set_dcto(self,d):
        self.get_promo().set_dcto(d)
    
    def set_id(self,i):
        self.get_promo().set_id(i)
        