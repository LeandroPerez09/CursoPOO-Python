class Auto():
    def __init__(self):
        self.estado = "apagado"
        print("El auto esta apgado")
    
    def encender(self):
        self.estado = "encendido"
        print("El auto esta encendido")

    def conducir(self):
        if self.estado == "apagado":
            self.encender()

        print("Conduciendo el Auto")

mi_auto = Auto()
mi_auto.conducir()


