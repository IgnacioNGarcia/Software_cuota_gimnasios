class Instructor():
    def __init__(self, nombre, dni) -> None:
        self.__nombre = nombre
        self.__dni = dni
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_dni(self):
        return self.__dni
    def set_dni(self,d):
        self.__dni = d
    dni = property(get_dni,set_dni)
    