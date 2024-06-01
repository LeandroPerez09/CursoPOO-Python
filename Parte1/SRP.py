#SingleResposabiltyPrinciple
#Cada clase se encarga de una funcionalidad unica
class Auto():
    def __init__(self,tanque):
        self.distanciaTotal = 0
        self.posicon  = 0
        self.tanque = tanque
        self.limite = tanque.get_combustible()*2
    
    def mover(self,distancia):
        if self.tanque.get_combustible() >= distancia/2:
            self.distanciaTotal += distancia
            self.posicon += distancia
            self.tanque.use_combustible(distancia/2)
            print(f"EL auto se movio exitosamente {distancia}km y ahora se encuentra a {self.posicon}km del inicio")
        else:
            
            self.distanciaTotal += distancia
            self.posicon = self.limite
            signo = self.distanciaTotal - self.limite
            if signo >= 0:
                #print(f"El auto recorrio {self.limite} #pero le falto recorrer {distancia - self.#limite}")
                print(f"EL auto se movio exitosamente {self.limite}km, pero le falto recorrer {signo} y ahora se encuentra a {self.posicon}km del inicio")
            else: 
                print(f"EL auto se movio exitosamente {self.limite}km, pero le falto recorrer {signo*-1} y ahora se encuentra a {self.posicon}km del inicio")

    def get_posicion(self):
        return self.posicon


class TanqueCombustible:
    def __init__(self,combustible):
        self.combustible  = combustible


    def add_combustible(self,cantidad):
        self.combustible += cantidad

    #getter
    def get_combustible(self):
        return self.combustible
    
    def use_combustible(self,cantidad):
        self.combustible -= cantidad


tanque = TanqueCombustible(100)
auto = Auto(tanque)

while(auto.distanciaTotal <=auto.limite ):
    
    km = input("Que distacia quieres recorrer con el carro?")
    km = float(km)
    print(auto.mover(km))
    print(km)



