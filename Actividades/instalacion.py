from Software_cuotas_gimnasio.Actividades.es_pago import Es_pago
class Instalacion(Es_pago):
    def __init__(self, nombre, precio, instructor) -> None:
        self.__nombre = nombre
        self.__precio = precio
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_precio(self):
        return self.__precio
    def set_precio(self,p):
        self.__precio = p
    precio = property(get_precio,set_precio)