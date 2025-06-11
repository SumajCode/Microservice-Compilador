import time
from functools import wraps
# * Usar decorador
def tiempoEjecucion():
    def calcularTiempo(funct):
        """
        Calcula el tiempo de ejecuccion del metodo Compilar de una compilacion y
        lo asigna en la clave 'tiempoEjecucion' del diccionario de salida.
        """
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            tiempoIni = time.time()
            compilacion = funct(self, *args, **kwargs)
            tiempoFin = time.time()
            compilacion.salida['tiempoEjecucion']=tiempoFin - tiempoIni
            return compilacion
        return wrapper
    return calcularTiempo