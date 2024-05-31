class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo, salario):
        #el trabajo de Super sirve para espeificar que propiedades de la clase padre quiero heredar a mi clase hija 
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario 

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        #el trabajo de Super sirve para espeificar que propiedades de la clase padre quiero heredar a mi clase hija 
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad 
    

roberto = Empleado("Roberto", 43, "Peruano","Programador",10000) 
print(roberto.nombre)