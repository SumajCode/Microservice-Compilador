import psutil
import os
from functools import wraps
# * Usar decorador
def accederMemoria():
    def calcularMemoria(funct):
        """
        Decorador para calcular el uso de memoria de un compilador.

        Este decorador mide la cantidad de memoria (en MB) utilizada por un
        proceso antes y después de la ejecución de la función compiladora
        proporcionada. La diferencia en el uso de memoria se almacena en la
        clave 'memoriaUso' del diccionario de salida del objeto de compilación.

        Parámetros:
        funct (callable): La función compiladora cuyo uso de memoria se desea medir.

        Retorna:
        callable: Una función envuelta que mide y registra el uso de memoria.
        """
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            """
            Wrapper que mide el uso de memoria de una compilación y
            actualiza el resultado con la diferencia de memoria utilizada.

            Parámetros:
            self (object): El objeto que contiene la compilación.
            *args (tuple): Argumentos de la compilación.
            **kwargs (dict): Argumentos de la compilación.

            Retorna:
            compilacion (Compilador): El objeto de compilación con el resultado actualizado.
            """
            psut = psutil.Process(os.getpid())
            memoriaActual = psut.memory_info().rss / 1024 ** 2
            compilacion = funct(self, *args, **kwargs)
            memoriaDespues = psut.memory_info().rss / 1024 ** 2
            compilacion.salida['memoriaUso']=memoriaDespues - memoriaActual
            return compilacion
        return wrapper
    return calcularMemoria