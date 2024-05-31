#Crear una clase estudiante que tenga los atributos Nombre, Edad y Grado. Ademas agregar un Método que se llame estudiar() e imprima el mensaje "El estudiante (nombre) esta estudiando". Se debe interactuar con el usuario y este debe brindar los atributos de la clase.
class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando.')
    def datos(self):
        print(f'Datos del Alumno {self.nombre}:')
        print(f'Edad: {self.edad}')
        print(f'Grado: {self.grado}')


nombre = input("Nombre : ")
edad = input("Edad: ")
grado = input("Grado: ")

estudiante1 = Estudiante(nombre,edad,grado)
estudiante1.datos()
estudiar =  input("Que accion esta realizando el alumno?")
if(estudiar.lower() == "estudiar"):
    estudiante1.estudiar()
else:
    print(f'{estudiante1.nombre} no esta estudiando')

      
        


