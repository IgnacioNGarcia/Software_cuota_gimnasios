class Socio():
    def __init__(self, nombre, apellido, direccion,telefono,mail,dni) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mail = mail
        self.__actividades = []
        self.__pase = None
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
    
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,a):
        self.__apellido = a
    apellido = property(get_apellido,set_apellido)
    
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self,d):
        self.__direccion = d
    direccion = property(get_direccion,set_direccion)
    
    def get_telefono(self):
        return self.__telefono
    def set_telefono(self,t):
        self.__telefono = t
    telefono = property(get_telefono,set_telefono)
    
    def get_mail(self):
        return self.__mail
    def set_mail(self,m):
        self.__mail = m
    mail = property(get_mail,set_mail)
    
    def get_actividades(self):
        return self.__actividades
    def set_actividades(self,a):
        self.__actividades = a
    actividades = property(get_actividades,set_actividades)
    
    def agregar_actividad(self, a):
        self.actividades.append(a)
    def eliminar_actividad(self,a):
        self.actividades.delete(a)
    'Considerar armar una cartera de actividades que tenga el usuario para estas responsabilidades de actividades'
    def get_pase(self):
        return self.__pase
    def set_pase(self,p):
        self.__pase = p
    pase = property(get_pase,set_pase)
    
    def calcular_cuota(self,promocion):
        return self.pase.calcular_cuota(self,promocion)

    def __eq__(self, other):
        if isinstance(other, Socio):
            return self.__dni == other.__dni
        return False