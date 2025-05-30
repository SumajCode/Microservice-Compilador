import sys
import io
import traceback

from features.sandbox.SandBoxCompilerOnlyPython import SandBox

class Evaluador(SandBox):
    def __init__(self):
        super().__init__()

    # * Buscar sys.argv para usar con lista de valores a evaluar, o mejor sys.stdin
    def Evaluar(self, request):
        try:
            datos = request.get_json() if request.is_json else request.form
            if 'results' in datos.keys() and isinstance(datos['results'], list):
                resultados = datos['results']
                for resultado in resultados:
                    pass
            return ""
        except Exception as e:
            return f"Error encontrado: {e}"