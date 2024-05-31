import time

def temporizador(mostrar):
    def decorador(func):
        def envoltura(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fin = time.time()
            if mostrar:
                print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} segundos")
            return resultado
        return envoltura
    return decorador

@temporizador(mostrar=True)
def sumar_hasta(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

@temporizador(mostrar=False)
def multiplicar_hasta(n):
    producto = 1
    for i in range(1, n + 1):
        producto *= i
    return producto

# Probar las funciones
print(f"Suma de los primeros 10 números: {sumar_hasta(10)}")
print(f"Producto de los primeros 10 números: {multiplicar_hasta(10)}")
