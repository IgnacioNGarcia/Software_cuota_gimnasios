from Software_cuotas_gimnasio.Socio.socio import Socio
from Software_cuotas_gimnasio.Instructor.instructor import Instructor
from Software_cuotas_gimnasio.Promociones.promocion import Promocion
class Gimnasio():
    def __init__(self) -> None:
        self.__actividades = []
        self.__socios = {}
        self.__promocion_activa = None
        self.__instructores = []
        self.__promociones = []
    
    def get_actividades(self):
        return self.__actividades
    def set_actividades(self,a):
        self.__actividades = a
    actividades = property(get_actividades,set_actividades)
    
    def agregar_actividad(self,a):
        self.actividades.append(a)
    def eliminar_actividad(self,a):
        self.actividades.delete(a)
    
    def get_socios(self):
        return self.__socios
    def set_socios(self,s):
        self.__socios = s
    socios = property(get_socios,set_socios)
    
    def agregar_socio(self,s :Socio):
        if isinstance(s,Socio):
            dni = s.get_dni()
            if dni not in self.socios:
                self.socios[dni] = s
            else:
                'raise excepcion de que ya está el socio'
                pass
    
    def get_promocion_activa(self):
        return self.__promocion_activa
    def set_promocion_activa(self,p):
        self.__promocion_activa = p
    promocion_activa = property(get_promocion_activa,set_promocion_activa)
    
    def get_instructores(self):
        return self.__instructores
    def set_instructores(self,i):
        self.__instructores = i
    instructores = property(get_instructores,set_instructores)
    
    def agregar_instructor(self, i):
        if isinstance(i,Instructor):
            dni = i.get_dni()
            if dni not in self.instructores:
                self.instructores.append(i)
            else:
                'Raise exception de que ya labura acá'
                pass
    
    def get_promociones(self):
        return self.__promociones
    def set_promociones(self,p):
        self.__promociones = p
    promociones = property(get_promociones,set_promociones)
    
    def agregar_promocion(self,p):
        if isinstance(p,Promocion):
            self.promociones.append(p)
        else:
            'Raiseo exception de que no es una promocion'
            pass
    
    def obtener_socio(self,dni):
        if dni not in self.socios:
            'raiseo exception de socio inexistente'
        else:
            return self.socios[dni]
    
    def obtener_cuota(self,dni):
        socio = self.obtener_socio(dni)
        cuota = 0
        cuota = socio.calcular_cuota(self.promocion_activa)
        return cuota