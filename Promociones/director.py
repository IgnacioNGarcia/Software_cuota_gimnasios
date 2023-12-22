from Software_cuotas_gimnasio.Promociones.builder import Builder
class Director():
    def __init__(self) -> None:
        self.__builder :Builder = None
    
    def get_builder(self):
        return self.__builder
    def set_builder(self,b):
        self.__builder = b
    builder = property(get_builder,set_builder)
    
    def crear_promo(self, nombre,dcto,id,acts = None):
        self.builder.reset()
        self.builder.set_nombre(nombre)
        self.builder.set_dcto(dcto)
        self.builder.set_id(id)
        self.builder.set_acts(acts)