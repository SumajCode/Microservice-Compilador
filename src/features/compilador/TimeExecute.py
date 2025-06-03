import time
from functools import wraps
# * Usar decorador
def tiempoEjecucion():
    def calcularTiempo(funct):
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            tiempoIni = time.time()
            compilacion = funct(self, *args, **kwargs)
            tiempoFin = time.time()
            compilacion.salida['tiempoEjecucion']=tiempoFin - tiempoIni
            return compilacion
        return wrapper
    return calcularTiempo