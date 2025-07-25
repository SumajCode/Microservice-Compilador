from domain.code.CompilerCode import Compilador
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.AssertOutputCode import evaluarSalidaCodigo
from scripts.FormaterString import agregarCodigo

class AssertCode(Compilador):
    def __init__(self):
        self.todoDelCodigio = None
        self.functionInvoke = ""
        self.code = ""
        self.input = None
        self.output = None
        super().__init__()

    @evaluarSalidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def Evaluar(self, codigo: str, **kwargs):
        if self.todoDelCodigio:
            self.code = agregarCodigo(codigo, self.input, self.todoDelCodigio, self.functionInvoke)
            self.output = kwargs.get('output')
            self.Compilar(output=self.output)
            return self
