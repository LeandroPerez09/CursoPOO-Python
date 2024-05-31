class Persona:
    def __init__(self,nombre,edad):
        # "_" para atributo privado
        # "__"para atributo MuyPrivado
        self.__nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
       

    
leandro = Persona("Leandro",14)
nombre = leandro.nombre
print(nombre)

leandro.nombre = "Pepe"
nombre = leandro.nombre
print(nombre)

del leandro.nombre
nombre = leandro.nombre
print(nombre)






        