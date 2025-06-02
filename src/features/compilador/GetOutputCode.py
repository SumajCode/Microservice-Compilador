import traceback
import sys
import io
from functools import wraps

# * Este debe obtener los errores
def salidaCodigo():
    def obtenerSalida(funct):
        @wraps(funct)
        def wrapper(self, *args, **kwargs):
            salida = sys.stdout
            capturaDeSalida = io.StringIO()
            sys.stdout = capturaDeSalida
            compilacion = None
            try:
                compilacion = funct(self, *args, **kwargs)
                resultado = capturaDeSalida.getvalue().strip()
                sys.stdout = salida
                self.salida['result']=resultado if resultado is not None and resultado != "" else "No se tiene salida de la compilacion."
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                self.salida['result']=''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            finally:
                sys.stdout = salida
            return compilacion
        return wrapper
    return obtenerSalida

