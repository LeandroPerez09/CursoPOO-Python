def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada

# def saludo():
#     print("Hola Dalto como andas ")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola leandro, como estas?")

saludo() 