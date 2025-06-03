import psutil
import os
from functools import wraps
# * Usar decorador
def accederMemoria():
    def calcularMemoria(funct):
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            psut = psutil.Process(os.getpid())
            memoriaActual = psut.memory_info().rss / 1024 ** 2
            compilacion = funct(self, *args, **kwargs)
            memoriaDespues = psut.memory_info().rss / 1024 ** 2
            compilacion.salida['memoriaUso']=memoriaDespues - memoriaActual
            return compilacion
        return wrapper
    return calcularMemoria