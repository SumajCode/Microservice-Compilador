import time
from functools import wraps
def tiempoEjecucion():
    def calcularTiempo(funct):
        """
        Calcula el tiempo de ejecuccion del metodo Compilar de una compilacion y
        lo asigna en la clave 'tiempoEjecucion' del diccionario de salida.
        """
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            """
            Wrapper que mide el tiempo de ejecuccion de la compilacion y
            actualiza el resultado con el tiempo de ejecuccion.

            Par metros:
            self (object): El objeto que contiene la compilaci n.
            *args (tuple): Argumentos de la compilaci n.
            **kwargs (dict): Argumentos de la compilaci n.

            Retorna:
            compilacion (Compilador): El objeto de compilaci n con el resultado actualizado.
            """

            tiempoIni = time.time()
            compilacion = funct(self, *args, **kwargs)
            tiempoFin = time.time()
            compilacion.salida['tiempoEjecucion']=tiempoFin - tiempoIni
            return compilacion
        return wrapper
    return calcularTiempo