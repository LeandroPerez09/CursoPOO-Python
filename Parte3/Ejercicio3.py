#l juego consiste en crear personajes un juego y que esos personajes se puedan fusionar para formar personajes mas poderosos que tengan mas poder...
#Para ello deberemos cambiar el comportamiento del operador    "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.
#una posible formula es: el promedio de las habilidades de ambos, al cuadrado!


class Personaje():
    def __init__(self,nombre, fuerza ,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad 
        
    
    def __repr__(self):
        return f"Nombre: {self.nombre}, Fuerza: {self.fuerza}, velocidad: {self.velocidad}"
    
    def __add__(self,otro_pj):
        habilidades = ((self.fuerza + self.velocidad + otro_pj.fuerza + otro_pj.velocidad)/4)**2
        return f'La fusion de {self.nombre} y {otro_pj.nombre} y su nuevo y mejorado poder es: {habilidades}'
    

goku = Personaje("Goku",100,100)
vegetta = Personaje("Vegetta",90,110)

fusion = goku + vegetta
print(fusion)