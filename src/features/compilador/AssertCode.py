from domain.code.CompilerCode import Compilador
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.AssertOutputCode import evaluarSalidaCodigo
from scripts.FormaterString import agregarCodigo

class AssertCode(Compilador):
    def __init__(self):
        self.todoDelCodigio = None
        self.functionInvoke = ""
        self.input = None
        self.output = None
        super().__init__()

    @evaluarSalidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def Evaluar(self, codigo: str, **kwargs):
        """
        Evalua el codigo segun el lenguaje y la entrada de datos.

        El metodo evalua el codigo segun el lenguaje y la entrada de datos.
        Si el lenguaje es python, se utiliza el compilador de python,
        si no es asi, se utiliza el compilador del lenguaje especificado.

        codigo: El codigo a evaluar.
        kwargs: Diccionario que contiene el lenguaje y las entradas y salidas.

        return: El objeto de compilacion.
        """

        if self.todoDelCodigio:
            self.code = agregarCodigo(codigo, self.input, self.todoDelCodigio, self.functionInvoke)
            self.output = kwargs.get('output')
            self.Compilar(output=self.output)
            return self