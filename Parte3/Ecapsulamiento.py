class Persona:
    def __init__(self,nombre,edad):
        # "_" para atributo privado
        # "__"para atributo MuyPrivado
        self.__nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,new_nombre):
        self.__nombre = new_nombre
    
leandro = Persona("Leandro",14)
nombre = leandro.get_nombre()
print(nombre)

leandro.set_nombre("Nahuel")
nombre = leandro.get_nombre()
print(nombre) 




        