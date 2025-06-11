from domain.code.CompilerCode import Compilador
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.GetOutputCode import salidaCodigo
from features.compilador.TaskCode import identificarCodigoEnCodigo
from scripts.FormaterString import agregarCodigo

class AssertCode(Compilador):
    def __init__(self):
        super().__init__()

    @salidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def Evaluar(self, datos: dict):
        todoDelCodigio = identificarCodigoEnCodigo(datos['code'])
        if isinstance(todoDelCodigio, tuple):
            self.salida['result'] = f"{todoDelCodigio[0]}:\n{todoDelCodigio[1]}"
            return self.salida
        nuevoCodigo = agregarCodigo(datos['code'], datos['input'], todoDelCodigio)
        self.code = nuevoCodigo
        self.Compilar()
        if self.salida['result'] != datos['output'] :
            self.salida['result'] = f"Error: {self.salida['result']} != {str(datos['output'])}"
        return self.salida
    
    def tieneClase():
        pass