import traceback
import sys
import io
from functools import wraps

def evaluarSalidaCodigo():
    def obtenerSalida(funct):
        """
        Decorador que captura la salida estándar de una función de compilación.

        Este decorador intercepta y redirige la salida estándar generada durante la ejecución
        de la función de compilación 'funct', almacenándola en la clave 'result' del diccionario 
        de salida del objeto de compilación. En caso de que ocurra una excepción durante la ejecución,
        la traza de la excepción se captura y se almacena en la misma clave.

        Parámetros:
        funct (callable): La función de compilación cuya salida estándar se desea capturar.

        Retorna:
        callable: Una función envuelta que captura y registra la salida estándar.
        """
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            """
            Wrapper que captura la salida estandar de la compilacion y la 
            almacena en la clave 'result' del diccionario de salida del 
            objeto de compilacion.

            Parámetros:
            self (object): El objeto que contiene la compilación.
            *args (tuple): Argumentos de la compilación.
            **kwargs (dict): Argumentos de la compilación.

            Retorna:
            compilacion (Compilador): El objeto de compilación con el resultado actualizado.
            """
            salida = sys.stdout
            capturaDeSalida = io.StringIO()
            sys.stdout = capturaDeSalida
            compilacion = None
            try:
                compilacion = funct(self, *args, **kwargs)
                resultado = capturaDeSalida.getvalue().strip()
                salidaEsperadda = kwargs.get('output')
                sys.stdout = salida
                if resultado is not None:
                    cadenaResultado = ""
                    cadenaResultado += f"Resultado obtenido: {resultado}\n"
                    cadenaResultado += f"Resultado esperado: {salidaEsperadda}\n"
                    if resultado == str(salidaEsperadda):
                        cadenaResultado = f"Resultado esperado correcto.\n{cadenaResultado}"
                        cadenaResultado += "Tu codigo es correcto"
                        self.salida['result'] = cadenaResultado
                    else:
                        cadenaResultado = f"Resultado esperado incorrecto.\n{cadenaResultado}"
                        cadenaResultado += "Mejor revisas o te sacas 0 xd."
                        self.salida['result'] = cadenaResultado
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                preExcep = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
                preExcep = preExcep.split('File')[-1]
                self.salida['result'] = f"File{preExcep}"
            finally:
                sys.stdout = salida
            return compilacion
        return wrapper
    return obtenerSalida