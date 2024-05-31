class Persona():
    def __init__(self,nombre,edad,trabajo):
        self.nombre = nombre
        self.edad = edad
        self.trabajo = trabajo

    def __str__(self):
        #str funciona como si fuera un print
        #str le ensenna al objeto como mostrarse como texto 
        return f'Persona(Nombre = {self.nombre},edad = {self.edad},trabajo = {self.trabajo})'

    def __repr__(self):
        #Actua como la representacion de 
        return f'Persona("{self.nombre}",{self.edad},"{self.trabajo}")'
    

    def __add__(self,otro):
        #define como se van a comportar los objetos de la Clase persona cuando estos son sumados
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor,self.trabajo + otro.trabajo)


leandro = Persona("Leandro",21,"Programador ")
pepe = Persona("Pepe",30,"IngenieroCivil ")
maria = Persona("Maria",18,"Doctora")
#repr : repre se vuelve la representacion de Leandro y actua como el objeto
repre = repr(leandro)
print(repre)
#eval: eval hace que resultad se hace el objeto
#Cual es la diferencia? con eval puedo llamar a las funciones de este objeto
resultado = eval(repre)
print(resultado.trabajo)

resultado1 = leandro + pepe + maria
print(resultado1.trabajo)
