class Promocion():
    def __init__(self) -> None:
        self.__nombre = None
        self.__actividades = []
        self.__dcto = None
        self.__id = None
    
    def get_nombre(self):
        return self.__nombre
    def get_actividades(self):
        return self.__actividades
    def get_dcto(self):
        return self.__dcto
    def get_id(self):
        return self.__id
    def agregar_act(self,a):
        'Agregar manejo de errores'
        self.__actividades.append(a)
    
    def set_nombre(self,n):
        self.__nombre = n
    def set_actividades(self,a):
        self.__actividades = a
    def set_dcto(self,d):
        self.__dcto = d
    def set_id(self,i):
        self.__id = i
    