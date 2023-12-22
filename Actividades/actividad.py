from Software_cuotas_gimnasio.Actividades.es_pago import Es_pago
from datetime import datetime, time
class Actividad(Es_pago):
    def __init__(self, nombre, precio, instructor) -> None:
        self.__nombre = nombre
        self.__precio = precio
        self.__instructor = instructor
        self.__dias_horarios = {}
    
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
    
    def get_instructor(self):
        return self.__instructor
    def set_instructor(self,i):
        self.__instructor = i
    instructor = property(get_instructor,set_instructor)
    
    def get_dias_horarios(self):
        return self.__dias_horarios
    def set_dias_horarios(self, d):
        self.__dias_horarios = d
    dias_horarios = property(get_dias_horarios,set_dias_horarios)
    
    def agregar_dia_horario(self, dia, horario: time):
        # Asegurarse de que __dias_horarios es un diccionario
        if not isinstance(self.__dias_horarios, dict):
            raise ValueError("El atributo 'dias_horarios' debe ser un diccionario.")
        
        # Verificar si el día ya existe en el diccionario
        if dia in self.__dias_horarios:
            # Si el día ya existe, agregar el nuevo horario a la lista existente
            self.__dias_horarios[dia].append(horario)
        else:
            # Si el día no existe, crear una nueva entrada en el diccionario con una lista que contiene el horario
            self.__dias_horarios[dia] = [horario]
    