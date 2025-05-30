import traceback
import sys
import io
from features.sandbox.SandBoxCompilerOnlyPython import SandBox

class Compilador(SandBox):
    def __init__(self):
        super().__init__()

    def Compilar(self, request):
        try:
            datos = request.get_json() if request.is_json else request.form
            if 'lang' in datos.keys() and 'code' in datos.keys():
                if datos['lang'] == "python":
                    try:
                        salida = sys.stdout
                        capturaDeSalida = io.StringIO()
                        sys.stdout = capturaDeSalida
                        exec(compile(datos['code'], '<String>', 'exec'))
                        resultado = capturaDeSalida.getvalue().strip()
                        sys.stdout = salida
                        return {
                            'result':resultado if resultado is not None else "No se tiene salida de la compilacion.",
                            'tiempoEjecucion':self.tiempoEjecucion(datos['code']),
                            'memoriaUso': self.accederMemoria(datos['code'])
                        }
                    except:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        return {'result':''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))}
                # else:
                #     pass
            return ""
        except Exception as e:
            return f"Error encontrado: {e}"