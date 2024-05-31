class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'



class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

    

roberto = EmpleadoArtista("Roberto", 43, "Peruano","Cantar",10000,"Google") 
#Empleado artista es una clase hija de la clase Persona? #SI
herencia = issubclass(EmpleadoArtista,Persona)
#roberto es una instancia de EmpleadoArtista?
#SI
Instancia = isinstance(roberto,EmpleadoArtista)

print(herencia) 
print(Instancia)