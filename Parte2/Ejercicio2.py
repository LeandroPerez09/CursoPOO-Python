#Temas: HerenciaMultiple, MRO, Herencia
#Crear un sistema para un escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y tambien tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.

#Deberas utilizar super en el metodo de inicializacion(init) para reutilizar el código de la clase padre(Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para segurarte de que todo funciona correctamente.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
       print(f'Grado: {self.grado}')

#    def listar_datos(self):
#        return f'{self.imprimir_datos()}{self.     imprimir_grado()}'


 
estudiante = Estudiante("Leandro Perez","21","10mo")
estudiante.imprimir_datos()
estudiante.imprimir_grado()