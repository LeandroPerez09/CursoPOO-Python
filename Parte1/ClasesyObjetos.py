class Celular: 
    #Constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #Metodo
    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')
    #Metodo/self hace referencia al objeto de la clase Celular
    def cortar(self):
        print(f'Cortaste la llamada desde un {self.modelo}')
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 pro", "48MP")

celular2.llamar()
        
